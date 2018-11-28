// Round2.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include "iostream"
#include "vector"
#include "algorithm"
using namespace std;
double test(vector<double> g)
{
	double dp[202][404]={};
	dp[0][201]=1.0;
	for(int i=0;i<g.size();i++)
	{
		for(int j=1;j<404;j++)
		{
			dp[i+1][j+1]+=dp[i][j]*g[i];
			dp[i+1][j-1]+=dp[i][j]*(1.0-g[i]);
		}
	}
	return dp[g.size()][201];
}
int main()
{
	//freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	for(int tc=0;tc<T;tc++)
	{
		int N,K;
		cin>>N>>K;
		vector<double> g(N);
		for(int i=0;i<N;i++)
		{
			cin>>g[i];
		}
		sort(g.begin(),g.end());
		double ans = 0;
		for(int i=0;i<=K;i++)
		{
			vector<double> p;
			for(int j=0;j<i;j++) p.push_back(g[j]);
			for(int j=N-1;j>=N-K+i; j--) p.push_back(g[j]);
			double r = test(p);
			ans=max(ans,r);
		}
		cout<<"Case #"<<tc+1<<": ";
		printf("%.12lf\n",ans);
	}
	return 0;
}

