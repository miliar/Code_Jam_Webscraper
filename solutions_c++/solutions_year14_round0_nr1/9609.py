/*	Karan Dhamele	    */
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

using namespace std;

/* General Declarations */

#define INF		1000000007
#define LL		long long int
#define SI(n)		scanf("%lld",&n);
#define SC(c)		scanf("%c",&c);
#define SS(s)		scanf("%s",s);
#define FOR(x,a,b)	for(LL x=a;x<b;x++)
#define REP(i,n)	for(LL i=0;i<n;i++)
#define MP		make_pair
#define PB		push_back


/* Container's */

#define	VI		vector<LL>
#define PLL             pair<LL,LL>  /* A Single Pair  */
#define VP		vector<PLL> /* Vector of Pairs */
#define VS		vector<string>
#define VVI		vector<VI>
#define VVS		vector<VS>

template<class T>inline T GCD(T a,T b){return b?GCD(b,a%b):a;}
template<class T> inline T LCM(T a,T b){if(a<0)return LCM(-a,b);if(b<0)return LCM(a,-b);return a*(b/GCD(a,b));}
template<class T>inline T POW1(T a,T b,T m){long long x=1,y=a;while(b > 0){if(b%2 == 1){x=(x*y);if(x>m) x%=m;}y = (y*y);if(y>m) y%=m;b /= 2;}return x;}
template<class T>inline T INV(T n,T m){return POW1(n,m-2,m);}
template<class T>inline T SUB(T a,T b,T m){return (a%m-b%m+m)%m;}
template<class T>inline T ADD(T a,T b,T m){return (a%m+b%m)%m;}
template<class T>inline T MUL(T a,T b,T m){return (a%m*b%m)%m;}
template<class T>inline T DIV(T a,T b,T m){return (a%m*(INV(b,m))%m)%m;}
int main()
{
	LL tc;
	SI(tc);
	REP(i,tc)
	{
		LL a,b;
		SI(a);
		LL arr1[4][4];
		REP(ii,4)
		{
			REP(j,4)
				SI(arr1[ii][j]);
		}
		SI(b);
		LL arr2[4][4];
		REP(ii,4)
		{
			REP(j,4)
				SI(arr2[ii][j]);
		}
		LL ans=0;
		LL lat;
		REP(ii,4)
		{
			REP(j,4)
			{
				if(arr1[a-1][ii]==arr2[b-1][j])
				{
					ans++;
					lat=arr2[b-1][j];
					arr2[b-1][j]=-1;
				}
			}
		}
		if(ans==0)
		{
			cout << "Case #" << i+1 << ": Volunteer cheated!\n";
		}
		else if(ans==1)
		{
			cout << "Case #" << i+1 << ": " << lat << endl;
		}
		else
		{
			cout << "Case #" << i+1 << ": Bad magician!\n";
		}
	}
	return 0;
}
