#include <bits/stdc++.h>
using namespace std;


#define Size(s) ((int)s.size())
#define rep(i, n) for(int i=0; i<n; ++i)
#define Foreach(i, x) for (__typeof(x.begin()) i = x.begin(); i != x.end(); i++)
#define F first
#define S second
#define X real()
#define Y imag()
#define MP make_pair

template<class P, class Q> inline bool mmin(P &a, Q b) { if (a > b){ a = b; return true;} return false;}
template<class P, class Q> inline bool mmax(P &a, Q b) { if (a < b){ a = b; return true;} return false;}

typedef long long LL;
typedef pair<int, int> pii;

const int N = 8, M = 4, MOD = 1e9 + 7;
int n, m, o1, o2;
string s[N];
LL dp[1<<N][M+1];
LL nm[1<<N][M+1];
bool mark[1<<N][M+1];
LL f[1<<N];
vector<string> v;

void get(int x, int y)
{
	if(mark[x][y]) return;
	mark[x][y] = true;
	if(y==0) {
		if(x)
			dp[x][y] = -MOD, nm[x][y] = 0;
		else
			dp[x][y] = 0, nm[x][y] = 1;
		return;
	}
	if(x==0) {
		dp[x][y] = -MOD, nm[x][y] = 0;
		return;
	}

	dp[x][y] = -MOD;
	for(int j=x; j>0; j = (j-1) & x) {
		get(x^j, y-1);
		LL val = dp[x^j][y-1] + f[j];
		if(dp[x][y] < val)
			dp[x][y] = val, nm[x][y] = nm[x^j][y-1];
		else if(dp[x][y]==val)
			nm[x][y] = (nm[x][y] + nm[x^j][y-1]) % MOD;
	}
	return;
}

inline void solve()
{
	rep(i, 1<<n) {
		v.clear();
		rep(j, n) if(i & (1<<j)) rep(k, Size(s[j]))
			v.push_back(s[j].substr(0, k+1));
		sort(v.begin(), v.end());
		v.resize(unique(v.begin(), v.end()) - v.begin());
		f[i] = Size(v) + 1;
	}

	rep(i, 1<<n) rep(j, m+1) mark[i][j] = 0;

	get((1<<n)-1, m);

	o1 = dp[(1<<n)-1][m];
	o2 = nm[(1<<n)-1][m];
}

int main()
{
	ios_base::sync_with_stdio(false);

	int nq;
	cin >> nq;
	rep(ii, nq) {
		cin >> n >> m;
		rep(i, n)
			cin >> s[i];
		solve();
		cout << "Case #" << ii+1 << ": " << o1 << ' ' << o2 << endl;
	}

	return 0;
}
