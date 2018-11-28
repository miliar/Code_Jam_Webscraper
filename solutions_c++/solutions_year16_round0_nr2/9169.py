#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <sstream>
#include <map>
#include <numeric>
#include <cstring>
#include <cmath>
#include <iomanip>
#include <queue>
#include <stack>

using namespace std;

// {{ includes
#define rep1(i, s, e) for(int i = (s) ; i < (e) ; ++i)
#define rep(i, n)  for(int i = (0) ; i < (n) ; ++i)
#define clr(a, val)  memset(a, val, sizeof a)

#define all(v) v.begin(), v.end()
#define sz(v) (int)v.size()
#define pb  push_back
#define mkp make_pair

#define fi first
#define se second

#define cc continue 
#define bb break


typedef long long ll;
typedef pair<int, int> pii;

// }} include


bool check(string s) {
	rep(i, sz(s)) 
	  if(s[i] == '-') return 0;
	return true;
}


int main(){
#ifdef HOME
	freopen("a.in","r",stdin);
#endif
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