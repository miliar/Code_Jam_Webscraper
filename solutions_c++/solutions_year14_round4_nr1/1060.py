#include<iostream>
#include<string>
#include<algorithm>
#include<stdio.h>
#include<queue>
#include<vector>
#include<stack>
#include<cstdlib>
#include<sstream>
#include<cassert>
#include<fstream>
#include<ctime>
#include<list>
#include<cmath>
#include<set>
#include<map>
#include<cstring>

using namespace std;

#define s(n)					scanf("%d",&n)
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define ss(n) 					scanf("%s",n)
#define INF						(int)1e9
#define LINF					(long long)1e18
#define EPS						1e-9
#define maX(a,b)				((a)>(b)?(a):(b))
#define miN(a,b)				((a)<(b)?(a):(b))
#define abS(x)					((x)<0?-(x):(x))
#define FOR(i,a,b)				for(int i=a;i<=b;i++)
#define rep(i,n)				FOR(i,0,n-1)
#define foreach(v,c)            for( typeof((c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define mp						make_pair
#define FF						first
#define SS						second
#define XX						first
#define YY						second.first
#define ZZ						second.second
#define pb						push_back
#define fill(a,v) 				memset(a,v,sizeof(a))
#define all(x)					x.begin(),x.end()
#define sz(v)					((int)(v.size()))
#define INDEX(arr,ind)			(lower_bound(all(arr),ind)-arr.begin())

typedef long long int lli;
typedef pair<int,int> pii;
typedef pair<lli,lli> pll;
typedef vector<int> vi;
typedef vector<lli> vlli;
typedef vector<pii> vii;

const int MAXN = 200015;
const int MOD  = 1000000007;

/*Main code begins now */

int main()
{
	int t,n,x;
	int a[MAXN];
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	#endif	
	s(t);
	FOR(q,1,t)
	{
		s(n);s(x);
		rep(i,n)
		s(a[i]);
		sort(a,a+n);
		int i = 0;
		int j = n-1;
		int ans = 0;
		while(i<=j)
		{
			if(i==j)
			{
				i++;
				ans++;
			}
			else if(a[i] + a[j] <=x)
				{
					i++,j--;
					ans++;
				}
			else
				{
					j--;
					ans++;
				}
		}

		printf("Case #%d: %d\n",q,ans);
	}
	return 0;
}
