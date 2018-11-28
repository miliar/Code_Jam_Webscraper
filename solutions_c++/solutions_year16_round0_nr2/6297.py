#include<stdio.h>

char str[128];
int A[128];

int dp[128][2];

int min(int a, int b) {
	return a>b? b:a;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t<=T; t++) {
		scanf("%s\n", str);
		int len=0;
		for(len=0; str[len]!=0; len++) {
			if( '-' == str[len]) {
				A[len] = 0;
			} else {
				A[len] = 1;
			}
		}	

		if(0 == A[0]) {
			dp[0][0] = 0;
			dp[0][1] = 1;
		} else {
			dp[0][0] = 1;
			dp[0][1] = 0;
		}

		for(int i = 1; i<len; ++i) {
			if(0 == A[i]) {
				// 000 0
				// 111 0
				dp[i][0] = min(dp[i-1][0], dp[i-1][1]+1);
				dp[i][1] = min(dp[i-1][0]+1, dp[i-1][1]+2);
			} else {
				dp[i][0] = min(dp[i-1][0]+2, dp[i-1][1]+1);
				dp[i][1] = min(dp[i-1][0]+1, dp[i-1][1]);
			}
		}
		printf("Case #%d: %d\n", t, dp[len-1][1]);
	}
}
