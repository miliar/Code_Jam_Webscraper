#include <stdio.h>
#include <vector>
#include <string>
#include <map>
// i = 2; j = 3; k = 4
int table[4][4] = {
	1, 2, 3, 4, 
	2, -1, 4, -3,
	3, -4, -1, 2,
	4, 3, -2, -1
};

std::map<char, int> m_s2i;
std::map<int, char> m_i2s;

int reduce(char& res, const char* ch, int L)
{
	int flag = 1;	// positive

	char pre = ch[0];

	int pre_i = m_s2i[pre] - 1;

	for (int j = 1; j < L; j++) {
		int cur = ch[j];

		int idx_j = m_s2i[cur] - 1;

		int table_val = table[pre_i][idx_j];

		if (table_val < 0) {

			flag = !flag;

			table_val = -table_val;
		}

		pre = m_i2s[table_val];
		pre_i = m_s2i[pre] - 1;
	}

	res = pre;

	return flag;
}

int search_forward(const char* ch, int L, int k)
{
	int pos = 0;

	char pre		= ch[pos];
	int  pre_i		= m_s2i[pre] - 1;

	if (pre == 'i')
		return 0;

	for (int i = 1; i < L*k; i++) {
		int idx = i%L;

		char cur	= ch[idx];
		int  idx_j	= m_s2i[cur] - 1;

		int table_val = table[pre_i][idx_j];

		if (table_val < 0) {

			table_val = -table_val;
		}

		pre = m_i2s[table_val];
		pre_i = m_s2i[pre] - 1;

		if (pre == 'i') {
			return i;
		}
	}

	return -1;
}

int search_backward(const char* ch, int L, int k, int stop_pos)
{
	int pos = L*k-1;

	char pre		= ch[pos%L];
	int  pre_i		= m_s2i[pre] - 1;

	if (pre == 'k')
		return pos;

	for (int i = L*k-2; i > stop_pos; i--) {
		int idx = i%L;

		char cur	= ch[idx];
		int  idx_j	= m_s2i[cur] - 1;

		int table_val = table[idx_j][pre_i];

		if (table_val < 0) {
			table_val = -table_val;
		}
		pre = m_i2s[table_val];
		pre_i = m_s2i[pre] - 1;

		if (pre == 'k') {
			return i;
		}
	}

	return -1;
}

int main()
{
	m_s2i['1'] = 1;
	m_s2i['i'] = 2;
	m_s2i['j'] = 3;
	m_s2i['k'] = 4;

	m_i2s[1] = '1'; 
	m_i2s[2] = 'i'; 
	m_i2s[3] = 'j'; 
	m_i2s[4] = 'k'; 

	FILE* fp = fopen("C-small-attempt1.in", "r");
	//FILE* fp = fopen("file_in.txt", "r");
	FILE* fp_w = fopen("file_out_1.txt", "w");

	int t;

	fscanf(fp, "%d", &t);
	//scanf("%d", &t);

	for (int case_i = 1; case_i <= t; case_i++) {
		int L, k;
		//scanf("%d%d", &L, &k);
		fscanf(fp, "%d%d", &L, &k);

		char ch[10004];
		//scanf("%s", ch);
		fscanf(fp, "%s", ch);

		if ( L*k < 3 ) {
			//printf("Case #%d: NO\n", case_i);
			fprintf(fp_w, "Case #%d: NO\n", case_i);
			continue;
		}
		
		// first judge signal
		char res;
		int flag = reduce(res, ch, L);
		
		int repeat = (k-1) % 4;

		char new_ch[4];
		for (int i = 0; i <= repeat; i++) {
			new_ch[i] = res;
		}

		/*printf("res: ");
		if (flag == 0) printf("-");
		printf("%c\n",res);*/

		int flag_2 = reduce(res, new_ch, repeat+1);

		if (!flag && k % 2 == 0) 
			flag = 1;

		flag = flag & flag_2;


		/*printf("after repeat\n");
		printf("res: ");
		if (flag == 0) printf("-");
		printf("%c\n",res);*/

		if ( res != '1' || flag == 1) {
			//printf("Case #%d: NO\n", case_i);
			fprintf(fp_w, "Case #%d: NO\n", case_i);
		}
		else {
			int pos = search_forward(ch, L, k);
			if (pos == -1) {
				//printf("Case #%d: NO\n", case_i);
				//printf("pos: %d\n", pos);

				fprintf(fp_w, "Case #%d: NO\n", case_i);
			}
			else {
				int pos_2 = search_backward(ch, L, k, pos);

				printf("pos_2: %d\n", pos_2);
				if (pos_2 == -1) {
					//printf("Case #%d: NO\n", case_i);
					fprintf(fp_w, "Case #%d: NO\n", case_i);
				}
				else {
					//printf("Case #%d: YES\n", case_i);
					fprintf(fp_w, "Case #%d: YES\n", case_i);
				}
			}
		}

	}

	fclose(fp);
	fclose(fp_w);
	return 0;
}