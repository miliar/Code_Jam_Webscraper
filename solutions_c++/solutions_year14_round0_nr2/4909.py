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

double C,F,X;
double foo(double i)
{
	if((X/i)-((C/i) + X/(i+F))<=EPS)
		return X/i;
	else
		return min(double(X/i),double(C/i+foo(i+F)));
}
int main()
{
	LL tc;
	SI(tc);
	LL tc1=1;
	while(tc--)
	{
		cin >> C >> F >> X;
		printf("Case #%lld: %0.7lf\n",tc1,foo(2.0));
		tc1++;
	}
	return 0;
}
