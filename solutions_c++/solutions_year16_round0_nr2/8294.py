
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

bool check(string s) {
	rep(i, sz(s)) 
	  if(s[i] == '-') return 0;
	return true;
}

int main() {
	int t; cin >> t;
	int __case = 1 ;
	while(t--) { 
		string s; cin >> s;
		int ans = 0;
		while(!check(s)) {
			ans ++ ;
			int p = 0;
			while(p < sz(s) && s[p] == '+') p ++ ;
			if(p == sz(s) || s[p] == '-') p -- ;
			if(p == -1) {
				p = sz(s) - 1;
				while(p>=0 && s[p] == '+') p -- ;
				rep(i, p+1) {
					if(s[i] == '+') s[i] = '-' ;
					else s[i] = '+' ;
				}
			}
			else {
				while(p>=0) s[p] = '-' , p--;
			}
		}
		printf("Case #%d: %d\n", __case++, ans) ;
	}
	return 0;
}