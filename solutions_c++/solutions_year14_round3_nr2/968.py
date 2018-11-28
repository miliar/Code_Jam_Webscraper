#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include<cassert>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include<bitset>

#define REP(i,b,n) for(int i=b;i<(int)n;i++)
#define rep(i,n)   REP(i,0,n)
#define ALL(C)     (C).begin(),(C).end()
#define FOR(it,o)  for(__typeof((o).begin()) it=(o).begin(); it!=(o).end(); ++it)
#define dbg(x) cout << __LINE__ << ' ' << #x << " = " << (x) << endl


typedef long long ll;

using namespace std;

const int N = 10;

map<char, string> NEXT;
map<char, int> simple;
set<char> S, used, input;

const int MOD = 1000000007;

ll fact(ll n){
	ll ret = 1;
	REP(i, 1, n+1){
		ret *= i;
		ret %= MOD;
	}
	return ret;
}
int main(){
	int T;
	cin >> T;
	rep(tc, T){
		cout << "Case #" <<tc +1 <<": ";
		NEXT.clear();simple.clear();
		used.clear();
		S.clear();
		input.clear();
		int n;
		cin >> n;
		for(char c ='a'; c<='z';c++)S.insert(c);
		try{
			rep(i, n){
				string s;
				cin >> s;
				rep(j, s.length()-1){
					input.insert(s[j]);
					if(s[j] != s[j+1]){
						if(NEXT.count(s[j])){
							throw 0;
						}
						NEXT[s[j]]=s;
						S.erase(s[j+1]);
					}
				}
				input.insert(s[s.length()-1]);
				if(s[0] == s[s.length()-1]){
					simple[s[0]]++;
				}
			}
			int cnt = 0;
			FOR(it, S){
				if(input.count(*it) == 0)continue;
				char c = *it;
				used.insert(c);
				while(NEXT.count(c)){
					FOR(it2, NEXT[c])used.insert(*it2);
					c = NEXT[c][NEXT[c].length()-1];
				}
				cnt++;
			}
			if(used.size() != input.size()){
				throw 1;
			}
			ll res = 1;
			res *= fact(cnt);
			res %= MOD;
			FOR(it, simple){
				res *= fact(it->second);
				res %= MOD;
			}
			cout << res << endl;
		}
		catch(int a){
			cout << 0 <<endl;
		}
	}
  return 0;
}
