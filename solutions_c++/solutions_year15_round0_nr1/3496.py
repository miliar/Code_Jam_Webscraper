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
		ll n;
		cin >> n;
		string s;
		cin >> s;
		ll sum = s[0] - '0';
		ll ans = 0;
		FL(i,1,n+1)
		{
			if(sum >= i)
			{
				sum += s[i] - '0';
			}
			else{
				ans = ans + (i - sum);
				sum = sum + (i-sum) + (s[i] - '0');
			}
		}
		cout << "Case #" << ca << ": ";
		cout << ans << endl;
		ca++;

	}
	return 0;	
}