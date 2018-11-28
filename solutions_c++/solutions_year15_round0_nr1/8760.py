#include <stdio.h>

int main()
{
	int t,tt=1;
	FILE* out = fopen("A_large.txt", "w");
	scanf("%d", &t);
	while (t--){
		int Smax = 0;
		int i, j;
		int res = 0;
		char str[2000] = { 0 };
		int cnt[2000] = { 0 };

		scanf("%d", &Smax);
		scanf("%s", str);
		for (i = 0; i <= Smax; i++){
			str[i] -= '0';
		}
		cnt[0] = str[0];
		for (i = 1; i <= Smax; i++){
			cnt[i] = cnt[i - 1] + str[i];
			//printf("cnt[%d] = %d, ", i, cnt[i]);
		}//printf("\n");
		for (i = 1; i <= Smax; i++){
			if (cnt[i - 1] < i){
				//printf("%d, %d\n", i, i - cnt[i - 1]);
				int gap = i - cnt[i - 1];
				res += (i - cnt[i - 1]);
				for (j = i - 1; j <= Smax; j++){
					cnt[j] += gap;
					//printf("cnt[%d] = %d\n", j, cnt[j]);
				}
			}
		}
		fprintf(out, "Case #%d: %d\n", tt++, res);		
	}
	fclose(out);
	return 0;
}