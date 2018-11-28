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

int d[3][111];

int calc(string cur) {
	
}

void solve(int tst) {
	string s; cin >> s;
	vector < bool > v(sz(s));
	rep(i, 0, sz(s)-1) if(s[i] == '+') v[i] = 1; else v[i] = 0;
	memset(d, 0x3f, sizeof d);
	d[v[0]][0] = 0;
	d[v[0]^1][0] = 1;
	rep(i, 1, sz(s)-1) {
		if(v[i]) {
			int j = i-1;
			updmin(d[1][i], d[1][j]);
			while(j > 0 && v[j] == 1) {
				updmin(d[1][i], d[0][j-1]+1);
				j--;
			}
			updmin(d[0][i], d[1][i-1]+1);
			/*j = i-1;
			while(j > 0 && v[j] == 1) {
				updmin(d[0][i], d[1][j-1]+1);
				j--;
			}*/
		} else {
			int j = i - 1;
			updmin(d[0][i], d[0][i-1]);
			while(j > 0 && v[j] == 0) {
				updmin(d[0][i], d[1][j-1]+1);
				j--;
			}
			updmin(d[1][i], d[0][i-1]+1);
			/*j = i - 1;
			while(j > 0 && v[j] == 1) {
				updmin(d[1][i], d[0][j-1]+1);
				updmin(d[1][i], d[1][j-1]);
				j--;
			}*/
		}
	}
	int res = min(d[1][sz(s)-1], d[0][sz(s)-1]+1);
	printf("Case #%d: %d\n", tst, res);
}

int main() {
	#ifdef accepted
		freopen(".in", "r", stdin);
		freopen("A.out", "w", stdout);
	#endif
	//string now = "abab";
	//reverse(now.begin(), now.begin()+2);
	//cout << now << nxtl;
	int t; scanf("%d", &t);
	rep(i, 1, t) solve(i);
	
	return 0;
}
