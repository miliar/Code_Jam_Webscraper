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

int main()
{
	LL tc,tc1;
	SI(tc);
	tc1=1;
	while(tc--)
	{
		LL x;
		SI(x);
		LL a[4][4],b[4][4];
		REP(i,4)
			REP(j,4)
				SI(a[i][j]);
		LL y;
		SI(y);
		REP(i,4)
			REP(j,4)
				SI(b[i][j]);
		LL ct=0,ans;
		REP(i,4)
		{
			REP(j,4)
			{
				if(a[x-1][i]==b[y-1][j])
				{
					ct++;
					ans=a[x-1][i];
					break;
				}
			}
		}
		if(ct==0)
			cout << "Case #" << tc1 << ": " << "Volunteer cheated!" << endl;
		else if(ct==1)
			cout << "Case #" << tc1 << ": " << ans << endl;
		else
			cout << "Case #" << tc1 << ": " << "Bad magician!" << endl;
		tc1++;
	}
	return 0;
}
