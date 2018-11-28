#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/stack:16777216")
#include <string>
#include <vector>
#include <map>
#include <numeric>
#include <list>
#include <iterator>
#include <set>
#include <queue>
#include <iostream>
#include <cstring>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <functional>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <time.h>
#include <iomanip>

using namespace std;

#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define ford(i, b, a) for(int i = (b) - 1; i >= (a); --i)
#define rep(i, N) FOR(i, 0, N)
#define FILL(A,value) memset(A,value,sizeof(A))

#define all(V) V.begin(), V.end()
#define sz(V) (int)V.size()
#define pb  push_back
#define mkp make_pair

#define fi first
#define se second

typedef long long ll;
typedef vector <int> vi;
typedef pair <int, int> pii;

const int INF = 1000000000;
const int MAX = 1010;
const int MOD = 1000000007 ;


int main() {
//	freopen("a.txt","r",stdin);
	//freopen("a.txt","w",stdout);
	int t; cin >> t;
	int __case = 1;
	vector <ll> res; 
	while(t--) {
		ll sum = 0, ans = 0;
		int k ; string s ; cin >> k  >> s;
		rep(i, k+1) {
			if(i > 0){
				if(sum < i) {
					ans += (i - sum) ; 
					sum += (i - sum);
				}
			}
			sum += (s[i]-48);
			//cout << sum << endl;
		}
		res.pb(ans);
	}
	rep(i, sz(res)) {
		cout << "Case #"<< __case++ << ": " << res[i] << endl;
	}
  return 0;
}
