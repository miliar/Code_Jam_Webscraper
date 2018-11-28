#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <queue>
#include <functional>
#include <list>
#include <set>
#include <sstream>
#define ll long long

using namespace std;

double prob[205];
int n,K;
double dp[205][205];

double calc(vector<double> &P)
{
	memset(dp,0,sizeof(dp));
	dp[0][0]=1.0;
	for(int i=0;i<=K;i++)
		for(int j=0;j<=i;j++)
		{
			dp[i+1][j] += dp[i][j]*(1.0-P[i]);
			dp[i+1][j+1] += dp[i][j] * P[i];
		}
	return dp[K][K/2];
}

int main()
{
	ios::sync_with_stdio(false);

	int T;
	cin>>T;
	cout<<setprecision(8)<<setiosflags(ios::fixed);
	for(int cas=1;cas<=T;cas++)
	{
		double ans=0.0;
		cin>>n>>K;
		for(int i=0;i<n;i++)
			cin>>prob[i];
		sort(prob,prob+n);
		for(int i=0;i<=K;i++)
		{
			vector<double> tmp;
			for(int j=0;j<i;j++)
				tmp.push_back(prob[j]);
			for(int j=n-K+i;j<n;j++)
				tmp.push_back(prob[j]);
			ans=max(ans,calc(tmp));
		}
		cout<<"Case #"<<cas<<": "<<ans<<endl;
	}

	return 0;
}
