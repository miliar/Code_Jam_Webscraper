#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;

#define N 110

int n, a, imax, jmax, mote[N], dp[N][N][N];
long long cnt[N][N];

FILE *fp, *fw;

bool cmp(int a, int b) {
	return a < b;
}

int main() {
	int i, j, k, cse, tp, ntp, g = 1;
	fp = fopen("/home/uriel/workspace/A-large.in", "r");
	fw = fopen("/home/uriel/workspace/outAl.txt", "w");
	fscanf(fp, "%d", &cse);
	while(cse--) {
		fscanf(fp, "%d %d", &a, &n);
		for(i = 0; i < n; ++i) {
			fscanf(fp, "%d", &mote[i]);
		}
		sort(mote, mote + n, cmp);
//		for(i = 0; i < n; ++i) {
//			printf("%d\n", mote[i]);
//		}
		memset(dp, 0, sizeof(dp));
		memset(cnt, 0, sizeof(cnt));
		cnt[0][0] = a;
		dp[0][0][0] = 1;
		imax = jmax = 0;
		for(i = 1; i <= n; ++i) {
			for(j = 0; j <= imax; ++j) {
				for(k = 0; k <= j; ++k) {
					if(!dp[i - 1][j][k]) continue;
					if(cnt[j][k] > mote[i - 1]) {
						dp[i][j][k] = 1;
						cnt[j][k] += mote[i - 1];
//						printf("cnt[%d][%d] = %d\n", j, k, cnt[j][k]);
					}
					else if(cnt[j][k] <= mote[i - 1]) {
						if(j < n) {
							dp[i][j + 1][k] = 1;
							cnt[j + 1][k] = cnt[j][k];
							imax = max(imax, j + 1);
						}

						tp = cnt[j][k];
						ntp = 0;
						while(tp > 1 && tp <= mote[i - 1]) {
							tp += tp - 1;
							ntp++;
						}
						if(j + ntp > n || tp <= mote[i - 1]) continue;
//						printf("ntp = %d, tp = %d\n", ntp, tp);
						dp[i][j + ntp][k + ntp] = 1;
						cnt[j + ntp][k + ntp] = tp + mote[i - 1];
						imax = max(imax, j + ntp);
						jmax = max(jmax, k + ntp);
					}
				}
			}
		}
		for(i = 0; i <= imax; ++i) {
			for(j = 0; j <= i; ++j) {
				if(dp[n][i][j]) break;
			}
			if(j <= i) break;
		}
//		printf("dp[%d][%d][%d]=%d\n", n, i, j, dp[n][i][j]);
		fprintf(fw, "Case #%d: %d\n", g++, i);
//		puts("");
	}
	fclose(fp);
	fclose(fw);
	return 0;
}
