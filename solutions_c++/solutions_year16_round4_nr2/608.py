#include<stdio.h>
#include<algorithm>
double p[201], p2[201];
double max(double a, double b){ return a>b?a:b; }
double max(double a, double b, double c){ return max(a, max(b, c)); }
double dp[102][102];
int n,k;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int TT=1; TT<=T; TT++)
	{
		scanf("%d%d", &n, &k);
		for(int i=1; i<=n; i++) scanf("%lf",p+i);
		std::sort(p+1, p+1+n);
		double ans = 0;
		for(int f = 0; f<=k; f++)
		{
			int r = n-(k-f)+1;
			for(int i=1; i<=f; i++) p2[i] = p[i];
			for(int i=r; i<=n; i++) p2[i-r+1+f] = p[i];
			dp[1][1] = 1;
			for(int i=1; i<=k; i++)
			{
				for(int j=0; j<=i; j++)
				{
					if(j>k/2 || (i-j)>k/2) continue;
					dp[j + 1][i-j + 1] = dp[j][i-j+1]*p2[i] + dp[j+1][i-j]*(1-p2[i]);
				}
			}
			if(ans < dp[k/2+1][k/2+1]) ans = dp[k/2+1][k/2+1];
		}
		int c = 0, f=1, r=n;
		printf("Case #%d: %.10f\n", TT, ans);
	}
	return 0;
}