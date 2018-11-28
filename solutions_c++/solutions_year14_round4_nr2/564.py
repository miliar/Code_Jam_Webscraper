#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
#define LL long long

int n,a[1111],b[1111],r[1111];
int dp[1005][1005],cnt[1005][2];

int cmp(int x,int y) {
	return a[x] < a[y];
}

int main() {
	int tc;
    scanf("%d",&tc);
    for (int t=1; t<=tc; t++) {
		scanf("%d",&n);
		for (int i=0; i<n; i++) {
			scanf("%d",&a[i]);
			r[i] = i;
		}
		sort(r,r+n,cmp);
		/*
		for (int i=0; i<n; i++)
			printf("%d ",r[i]);
		puts("");
		*/
		memset(cnt,0,sizeof(cnt));
		for (int i=0; i<n; i++)
			for (int j=i+1; j<n; j++)
				if (r[j] > r[i]) cnt[i][0]++;
				else cnt[i][1]++;
		memset(dp,127,sizeof(dp));
		dp[0][0] = 0;
		for (int i=0; i<n; i++) {
			for (int j=0; j<=i; j++) {
				dp[i+1][j+1] = min(dp[i+1][j+2],dp[i][j]+cnt[i][0]);
				dp[i+1][j] = min(dp[i+1][j],dp[i][j]+cnt[i][1]);
			}
		}
		int best = (1<<30);
		for (int i=0; i<=n; i++)
			best = min(best,dp[n][i]);
		printf("Case #%d: %d\n",t,best);
    }
	return 0;
}
