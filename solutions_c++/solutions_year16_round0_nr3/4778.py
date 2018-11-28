#include<stdio.h>
#include<math.h>
int t, n, j,cnt,count;
long long tmp[11],ans[11],tt,num;
char binary[20];
int main() {
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		count = 0;
		scanf("%d %d", &n, &j);
		printf("Case #%d:\n", i);
		for (int k = (1 << n-1) + 1; k < (1 << n); k++) {
			if ((k & 1) == 0 || ((k >> (n-1)) & 1) == 0)continue;
			num = k;
			cnt = 0;
			while (num) {
				binary[cnt++] = num % 2+'0';
				num = num / 2;
			}
			for (int l = 0; l < cnt / 2; l++) {
				char temp = binary[l];
				binary[l] = binary[cnt - l - 1];
				binary[cnt - l - 1] =temp;
			}
			binary[cnt] = '\0';
			for (int l = 2; l <= 10; l++) {
				tt = 1;
				for (int m = cnt - 1; m >= 0;m--){
					tmp[l] = tmp[l] + (binary[m]-'0')*tt;
					tt = tt*l;
				}
				for (long long m = 2; m <= sqrt(tmp[l]); m++) {
					if (tmp[l] % m == 0) {
						ans[l] = m; break;
					}
				}
				if (ans[l] == 0)break;
			}
			int flag = 0;
			for (int l = 2; l <= 10; l++)
				if (ans[l] == 0) {
					flag = 1; break;
				}
			if (!flag) {
				printf("%s ", binary);
				for (int l = 2; l <= 10; l++)printf("%lld ", ans[l]);
				printf("\n");
				count++;
			}
			for (int l = 2; l <= 10; l++)tmp[l]=ans[l] = 0;
			if (count == j)break;
		}
	}
	return 0;
}