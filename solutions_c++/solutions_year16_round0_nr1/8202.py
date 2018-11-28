// No man has a good enough memory to be a successful liar. 
// Life is the art of drawing without an eraser.

#include <bits/stdc++.h>

using namespace std; 

// {{ templetes

#define rep1(i, s, e) for(int i = (s) ; i < (e) ; ++i)
#define rep(i, n)  for(int i = (0) ; i < (n) ; ++i)
#define clr(a, val)  memset(a, val, sizeof a)

#define all(v) v.begin(), v.end() 
#define sz(v) (int)v.size()
#define pb  push_back
#define mkp make_pair

#define fi first
#define se second

#define dbg cerr << "OK!!!\n" 
#define endl '\n'

typedef long long ll;
typedef pair<int, int> pii;

const int mod = 1000000007 ;
const int MAX = 200005 ;

// }}

int main() {
	int t; cin >> t;
	int __case = 1 ;
	while(t--) { 
		ll p = 1; 
		ll n ; cin >> n;
		if(n == 0) {
			printf("Case #%d: INSOMNIA\n",__case++) ;
			continue ;
		}
		ll ans = 1 ;
		ll nn = n;
		set <int> st ;
		for(ll i = 1 ; ; i++) {
			n = nn * i ;
		//	cout << n << endl;
			while(n) {
				st.insert(n % 10) ;
				n/=10 ;
			}
			if(sz(st) == 10) {ans = i * nn ; break; }
		}
		printf("Case #%d: %lld\n",__case++, ans) ;
	}
	return 0;
}