#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define sz(s) ((int)(s.size()))
#define all(s) s.begin(),s.end()
#define rep(i,a,n) for(int i=a;i<=n;++i)
#define per(i,n,a) for(int i=n;i>=a;--i)

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

const int MAXN = 3e5 + 256;
const char nxtl = '\n';
const double eps = (double)1e-9;
template<typename T> inline bool updmin(T &a, const T &b) {return a > b ? a = b, 1 : 0;}
template<typename T> inline bool updmax(T &a, const T &b) {return a < b ? a = b, 1 : 0;}

int t;

void solve(int cs) {
	string s; cin >> s;
	list < char > res;
	int id = 0;
	while(id < sz(s)) {
		if(res.empty()) {
			res.pb(s[id]); id++; continue;
		}
		if(s[id] >= res.front()) res.push_front(s[id]);
		else res.pb(s[id]);
		id++;
	}
	printf("Case #%d: ", cs);
	for(auto &to : res) {  cout << to; }
	puts("");
}

int main() {
	#ifdef accepted
		freopen(".in", "r", stdin);
		freopen("A.out", "w", stdout);
	#endif
	cin >> t;
	rep(i, 0, t-1) {
		solve(i+1);
	}
	return 0;
}
