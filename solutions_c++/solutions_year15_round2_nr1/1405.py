/* In the name of ALLAH, most gracious, most merciful */
#include <iostream>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <ios>
#include <map>
#include <set>
#include <algorithm>
#include <cstring>
#include <ctime>
#include <queue>
#include <cassert>
#include <cmath>
#include <string>
#include <stack>

using namespace std;

typedef long long ll;

int reverse(int a)
{
	int ret=0;
	while(a)
	{
		ret*=10;
		ret+=a%10;
		a/=10;
	}
	return ret;
}
int dp[1000009];
int solve(int n)
{
	if(n==1)
		return dp[1]=1;
	int &ret=dp[n];
	if(ret!=-1)
		return ret;
	ret=1+solve(n-1);
	int t=reverse(n);
	if(n%10!=0 && t<n)
	{
		ret=min(ret,1+solve(t));
	}
	return ret;
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("2.in", "r", stdin);
	freopen("2.out", "w", stdout);
#endif
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    memset(dp,-1,sizeof dp);
    for(int i=1;i<=1000000;i++)
    	dp[i]=solve(i);

    int tc;
    cin>>tc;
    int ic=1;
    while(tc--)
    {
    	int a;
    	cin>>a;
    	cout<<"Case #"<<ic++<<": "<<dp[a]<<endl;
    }


    return 0;
}
