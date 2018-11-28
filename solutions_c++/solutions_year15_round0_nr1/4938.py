#include <stdio.h>
#include <vector>
int main()
{
	FILE* fp = fopen("A-large.in", "r");

	FILE* fp_w = fopen("file_out.txt", "w");

	if (NULL == fp)
		return -1;

	int m, n;

	fscanf(fp, "%d",&m);

	//scanf("%d",&m);

	for (int case_i = 1; case_i <= m; case_i++) {
		int n;

		fscanf(fp,"%d",&n);

		//scanf("%d",&n);

		char ch[1005];

		fscanf(fp, "%s", ch);

		//scanf("%s", ch);

		std::vector<int> c(n+1);
		for (int i = 0; i <= n; i++) {
			c[i] = ch[i]-'0';
		}

		if (n == 0) {
			//printf("Case #%d: 0\n", case_i);
			fprintf(fp_w, "Case #%d: 0\n", case_i);
		}
		else {
			std::vector<int> cnt(n+1,0);
			cnt[0] = 0;
			for (int i = 1; i <= n; i++) {
				cnt[i] = cnt[i-1]+c[i-1];
			}

			int pre_sum = cnt[0];
			for (int i = 1; i <= n; i++) {
				if (cnt[i]+pre_sum < i) {
					pre_sum = i - cnt[i];
				}
			}
			//printf("Case #%d: %d\n", case_i, pre_sum-cnt[0]);
			fprintf(fp_w, "Case #%d: %d\n", case_i, pre_sum-cnt[0]);
		}
	}

	fclose(fp);
	
	return 0;
}
