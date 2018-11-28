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
#include<string.h>
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
#define mp make_pair
#define mod 1000000007
 
#include <iostream>
using namespace std;

int main() {
	ll t;
	cin >> t;
	ll count = 1;
	ll flag[11];
	while(t--) {
		ll n;
		cin >> n;
		fill(flag,0);
		cout << "Case #" << count << ": "; 
		if(n == 0) {
			cout << "INSOMNIA" << endl;
			count++;
			continue;
		}

		ll c = 2;
		ll n1 = n;
		while(true) {
			ll temp = n1;
			while(temp != 0) {
				ll rem = temp%10;
				flag[rem] = 1;
				temp = temp/10;
			}

			ll ans = 0;
			FOR(i,10) {
				if(flag[i]) ans++;
			}
			if(ans == 10) {
				cout << n1 << endl;
				count++;
				break;
			}
			n1=n*c;
			c++;
		}

	}










	return 0;
}