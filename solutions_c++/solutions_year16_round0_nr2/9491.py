#include <bits/stdc++.h>
using namespace std;

const int N=1e2+10;
int dp[N][2];

int main() {
	int T=1, t;
	char s[N];
	scanf("%d", &t);
	while(t--) {
		scanf("%s", s);
		int n=strlen(s);
		dp[0][0]=(s[0]=='+' ? 0 : 1);
		dp[0][1]=(s[0]=='-' ? 0 : 1);
		for(int i=1; i<n; i++) {
			if(s[i]=='+') {
				dp[i][0]=min(dp[i-1][0], dp[i-1][1]+1);
				dp[i][1]=min(dp[i-1][0]+1, dp[i-1][1]+2);
			}
			else {
				dp[i][0]=min(dp[i-1][0]+2, dp[i-1][1]+1);
				dp[i][1]=min(dp[i-1][0]+1, dp[i-1][1]);
			}
		}
		printf("Case #%d: %d\n", T++, dp[n-1][0]);
	}
	return 0;
}
