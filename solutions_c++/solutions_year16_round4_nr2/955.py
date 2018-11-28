#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
const int MAXN = 202;
double dp[MAXN][MAXN];
double calc(vector<double> a)
{
	int N = a.size();
	dp[0][0]= 1-a[0];
	dp[0][1]= a[0];
	for(int i=1; i<N; i++)
	{
		dp[i][0]=dp[i-1][0]*(1-a[i]);
		for(int j=1;j<=i;j++)
			dp[i][j]=dp[i-1][j]*(1-a[i])+dp[i-1][j-1]*a[i];
		dp[i][i+1]=dp[i-1][i]*a[i];
	}
	return dp[N-1][N/2];
}
double tmain()
{
	int K, N;
	scanf("%d%d",&N, &K);
	vector<double> x;
	for(int i=0; i<N; i++)
	{
		double f;
		scanf("%lf",&f);
		x.push_back(f);
	}
	sort(x.begin(), x.end());
	double ans = 0;
	for(int i=0; i<=K; i++)
	{
		//puts("ok");
		vector<double> ss;
		for(int j=0; j<i; j++)
		{
			ss.push_back(x[j]);
		}
		for(int j=N-(K-i);j<N; j++)
		{
			ss.push_back(x[j]);
		}
		double val = calc(ss);
		if(ans<val) ans= val;
	}
	return ans;
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int i=1; i<=T; i++)
		printf("Case #%d: %.12lf\n",i, tmain());
	return 0;
}