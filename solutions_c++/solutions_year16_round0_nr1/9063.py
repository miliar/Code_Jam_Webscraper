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

#define dbg	cout << "" 

#define endl '\n'

typedef long long ll;
typedef pair<int, int> pii;

const int mod = 1000000007; 
const int MAX = 100005 ;

// }} include

set <int> st;

int main(){
#ifdef HOME
	freopen("a.in","r",stdin);
#endif
	int t, cnt = 1; cin >> t;
	while(t--){
		int n; cin >> n;
		if(n == 0){
			cout << "Case " << '#' << cnt++ << ": " << "INSOMNIA" << endl;
			cc;
		}
		int i = 1;
		while(sz(st) != 10){
			int ex = n * (i++);
			while(ex){
				st.insert(ex % 10);
				ex /= 10;
			}
		}
		cout << "Case " << '#' << cnt++ << ": " << n * (--i) << endl;
		st.clear();
	}
	return 0;
}