#include <cstdio>

#define ROWNUM 4
int ts, sselRow, fselRow, dummy;
int f_ans[ROWNUM], s_ans[ROWNUM];

int magic()
{
	int cnt = 0, ans = 0;
	for(int i = 0 ; i < 4; i++)
		for(int j = 0; j < 4; j++)
			if(f_ans[i] == s_ans[j]){
				ans = s_ans[j];
				cnt ++;
			}

	if(cnt == 0)
		return 0;
	else if(cnt == 1)
		return ans;
	else if(cnt > 1)
		return -1;
}


int main()
{
	freopen("A-small-attempt2.in", "r", stdin);
	int case_V = 0;

	FILE *f = fopen("output.txt", "w");
	for(scanf("%d", &ts); ts > 0; ts--)
	{
		case_V++;
		scanf("%d", &fselRow);
		for(int i = 0 ; i < 4; i++)
		{
			f_ans[i] = 0;
			s_ans[i] = 0;
		}

		for(int i = 0; i < 4; i++)
		{
			// ют╥б
			if(i == fselRow - 1){
				scanf("%d %d %d %d", &f_ans[0], &f_ans[1], &f_ans[2], &f_ans[3]);
			}else{
				scanf("%d %d %d %d", &dummy, &dummy, &dummy, &dummy);
			}
		}
		scanf("%d", &sselRow);
		for(int i = 0; i < 4; i++)
		{
			if(i == sselRow - 1){				
				scanf("%d %d %d %d", &s_ans[0], &s_ans[1], &s_ans[2], &s_ans[3]);
			}else{
				scanf("%d %d %d %d", &dummy, &dummy, &dummy, &dummy);
			}
		}
		
		int result = magic();
		if(result == 0)
			fprintf(f, "Case #%d: Volunteer cheated!\n", case_V);
		else if(result == -1)
			fprintf(f, "Case #%d: Bad magician!\n", case_V);
		else
			fprintf(f, "Case #%d: %d\n", case_V, result);
	}
	
	return 0;
}