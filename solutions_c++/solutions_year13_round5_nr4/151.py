#define _CRT_SECURE_NO_DEPRECATE

#pragma comment(linker,"/STACK:267386880")

#include <iostream>
#include <functional>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <memory>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <utility>
#include <iterator>
#include <bitset>
#include <sstream>
#include <numeric>
#include <complex>

#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define pdd pair<double,double>
#define LL long long
#define ULL unsigned LL
#define VI vector<int>
#define X first
#define Y second
#define sz(_v) ((int)_v.size())
#define all(_v) (_v).begin(),(_v).end()
#define FOR(i,a,b) for (int i(a); i<=(b); ++i)
#define rep(i,a) FOR(i,1,a)
#define rept(i,a) FOR(i,0,(int)(a)-1)
#define x1 X1
#define y1 Y1
#define sqr(a) ((a)*(a))
#define C(a) memset((a),0,sizeof (a))
#define MS(a,x) memset((a),(x),sizeof (a))
#define INF 1000000000
#define PI 3.141592653589
#define eps 0.00000000001
#define MOD 1000000007
#define PRIME 1000003

using namespace std;

double dp[1<<21];
int n;

double countDP(int mask)
{
	if (dp[mask]>-0.5)
		return dp[mask];
	if (mask==((1<<n)-1))
		return 0;
	double ans(0);
	rept(i,n)
	{
		int hm=0;
		int cur=i;
		while ((mask&(1<<cur))!=0)
		{
			--cur;
			++hm;
			if (cur<0)
				cur=n-1;
		}
		ans+=n-hm+countDP(mask|(1<<cur));
	}
	ans/=n;
	return dp[mask]=ans;
}

int main()
{
#ifndef ONLINE_JUDGE
	{
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	}
#endif
	int tst;
	scanf("%d\n",&tst);
	rept(t,tst)
	{
		printf("Case #%d: ",t+1);
		string s;
		getline(cin,s);
		n=s.length();
		int mask=0;
		rept(i,1<<n)
			dp[i]=-1.;
		rept(i,s.length())
			mask=mask*2+(s[i]=='X');
		printf("%.11lf\n",countDP(mask));
	}
	return 0;
}