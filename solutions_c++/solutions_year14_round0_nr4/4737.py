/*	Jayesh Lahori	    */
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<sstream>
#include<iomanip>

using namespace std;

/* General Declarations */

#define INF		1000000007
#define LL		long long int
#define SI(n)		scanf("%lld",&n)
#define SC(c)		scanf("%c",&c)
#define FOR(x,a,b)	for(LL x=a;x<b;x++)
#define REP(i,n)	for(LL i=0;i<n;i++)
#define MP		make_pair
#define PB		push_back
#define F		first
#define S		second
#define TR(container,it) for(typeof(container.begin()) it = container.begin();it != container.end(); it++)


/* Container's */

#define	VI		vector<LL>
#define PLL		pair<LL,LL>  /* A Single Pair  */
#define VP		vector<PLL> /* Vector of Pairs */
#define VS		vector<string>
#define VVI		vector<VI>
#define VVS		vector<VS>

#define EPS		0.0000001

bool foo(double a,double b)
{
	return (a>b);
}
int main()
{
	LL tc,tc1=1;
	SI(tc);
	while(tc--)
	{
		LL n;
		SI(n);
		vector<double> v1(n),v2(n);
		VI mark1(n,0),mark2(n,0);
		REP(i,n)
			cin >> v1[i];
		REP(i,n)
			cin >> v2[i];
		sort(v2.begin(),v2.end());
		LL ans1=0,ans2=0;
		REP(i,n)
		{
			LL flag=0;
			REP(j,n)
			{
				if(v2[j]>v1[i] && mark2[j]!=1)
				{
					mark2[j]=1;
					flag=1;
					break;
				}
			}
			if(flag==0)
				ans2++;
		}
		sort(v2.begin(),v2.end(),foo);
		REP(i,n)
		{
			LL flag=0;
			REP(j,n)
			{
				if(v2[j]<v1[i] && mark1[j]!=1)
				{
					mark1[j]=1;
					flag=1;
					break;
				}
			}
			if(flag==1)
				ans1++;
		}
		cout << "Case #" << tc1 << ": " << ans1 << " " << ans2 << endl;
		tc1++;
	}
	return 0;
}
