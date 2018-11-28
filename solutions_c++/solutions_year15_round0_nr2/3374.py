#include<vector>
#include<iostream>
#include<stdio.h>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<math.h>
#include<cstdlib>
#include<ctime>
#include<cstring>
#include<climits>
#include<sstream>
#include<string>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>
#include<deque>
#include<list>
#include<bitset>

#define ll long long
#define FL(i,a,b) for(ll i=a;i<b;i++)
#define FOR(i,n) for(ll i=0;i<n;i++)
#define SORTF(x) sort(x.begin(),x.end(),func);
#define SORT(x) sort(x.begin(),x.end())
#define pb(x) push_back(x)
#define SET(v, val) memset(v, val, sizeof(v)) ;
#define RSORT(v) { SORT(v) ; REVERSE(v) ; }
#define ALL(v) v.begin(),v.end()
#define REVERSE(v) { reverse(ALL(v)) ; }
#define UNIQUE(v) unique((v).begin(), (v).end())
#define RUNIQUE(v) { SORT(v) ; (v).resize(UNIQUE(v) - (v).begin()) ; }
#define fill(x,n) memset(x,n,sizeof(x))
#define sl(x) scanf("%lld",&x)
using namespace std;

int main()
{
	ll t;
	cin >> t;
	ll ca = 1;
	while(t--)
	{
		ll d;
		cin >> d;
		vector<ll> v;
		FOR(i,d)
		{
			ll x;
			cin >> x;
			v.push_back(x);
		}
		ll ans= 1000000000;
		FL(i,1,1001)
		{
			ll temp = i;
			FOR(j,v.size())
			{
				temp += (v[j]-1)/i;
			}
			ans = min(ans,temp);
		}
		cout << "Case #" << ca << ": ";
		cout << ans << endl;
		ca++;
	}
	return 0;	
}