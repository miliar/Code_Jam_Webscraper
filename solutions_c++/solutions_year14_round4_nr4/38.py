#include <cstdio>
#include <numeric>
#include <iostream>
#include <vector>
#include <set>
#include <cstring>
#include <string>
#include <map>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <queue>
#include <sstream>
#include <deque>

using namespace std;

#define mp make_pair
#define pb push_back
#define rep(i,n) for(int i = 0; i < (n); i++)
#define re return
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x) * (x))
#define sqrt(x) sqrt(abs(x))
#define y0 y3487465
#define y1 y8687969
#define fill(x,y) memset(x,y,sizeof(x))
#define prev PREV                         
#define next NEXT

typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef double D;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;

template<class T> T abs(T x) { re x > 0 ? x : -x; }

const int mod = 1000*1000*1000+7;

int n;
int m;

int next[100001][26];
int o;
string s[1000];
int fin[100001];

int add (string s) {
	int x = 0;
	fin[0]++;
	for (int i = 0; i < sz (s); i++) {
		int c = s[i] - 'A';
		int y = next[x][c];
		if (y == 0)
			y = next[x][c] = o++;
		x = y;
		fin[x]++;
	}
	re 0;
}

int ct;
ll cnk[1001][1001];
ll f[1001];
int ans = 0;
int was[2001][101];
ll res[2001][101];

int go (int x) {
	ans += min (fin[x], m);
	int ok = 0, sum = 0;
	vii v;
	for (int i = 0; i < 26; i++) {
		int y = next[x][i];
		if (y == 0) continue;
		v.pb (mp (fin[y], go (y)));
		sum += fin[y];
		if (fin[y] > m) ok = 1;
	}
	for (int i = 0; i < fin[x] - sum; i++) v.pb (mp (1, 1));
	if (ok) {
		int cur = 1;
		for (int i = 0; i < sz (v); i++)
			if (v[i].fi > m)
				cur = ((ll)cur * v[i].se) % mod;
			else {
				cur = ((ll)cur * cnk[m][v[i].fi]) % mod;
				cur = ((ll)cur * f[v[i].fi]) % mod;
			}
//		printf ("ok %d = %d = %d\n", x + 1, fin[x], cur);
		re cur;
	}
	if (fin[x] <= m) re 0;
	ct++;
	was[0][0] = ct;
	res[0][0] = 1;
	sum = 0;
	for (int i = 0; i < sz (v); i++) {
//		printf ("%d %d\n", v[i].fi, v[i].se);
		for (int j = sum; j >= 0; j--)
			if (was[i][j] == ct) {
//				printf ("%d %d = %d\n", i, j, res[i][j]);
				for (int t = 0; t <= min (j, v[i].fi); t++) {
					int nj = j + v[i].fi - t;
					if (nj <= m) {
						if (was[i + 1][nj] != ct) {
							was[i + 1][nj] = ct;
							res[i + 1][nj] = 0;
						}
//						int tmp = ((ll)f[v[i].fi] * cnk[v[i].fi][t]) % mod;
						int tmp = ((ll)f[v[i].fi] * cnk[j][t]) % mod;
						tmp = ((ll)tmp * cnk[m - j][v[i].fi - t]) % mod;
						tmp = ((ll)tmp * res[i][j]) % mod;
//						printf ("%d = %d\n", nj, tmp);
						res[i + 1][nj] = ((ll)res[i + 1][nj] + tmp) % mod;
					}
				}
			}	
		sum = min (sum + v[i].fi, m);
	}
//	printf ("res = %d = %d = %d\n", x + 1, fin[x], res[sz (v)][m]);
	re res[sz (v)][m];
}

int main () {
	for (int i = 0; i <= 1000; i++)
		for (int j = 0; j <= i; j++)
			if (i == 0 || j % i == 0)
				cnk[i][j] = 1;
			else
				cnk[i][j] = ((ll)cnk[i - 1][j] + cnk[i - 1][j - 1]) % mod;
	f[0] = 1;
	for (int i = 1; i <= 1000; i++) f[i] = ((ll)f[i - 1] * i) % mod;
	int tt;
	cin >> tt;
	for (int it = 1; it <= tt; it++) {
		cin >> n >> m;
		memset (next, 0, sizeof (next));
		memset (fin, 0, sizeof (fin));
		o = 1;
		for (int i = 0; i < n; i++) {
			string s;
			cin >> s;
			add (s);
		}
		ans = 0;
		int res = go (0);
		if (fin[0] <= m) res = ((ll)cnk[m][fin[0]] * f[fin[0]]) % mod;
		cout << "Case #" << it << ": " << ans << " " << res;
		cout << endl;
		fprintf (stderr, "%d / %d = %.2f | %.2f\n", it, tt, (double)clock () / CLOCKS_PER_SEC, ((double)clock () / it * tt) / CLOCKS_PER_SEC);
	}
	return 0;
}