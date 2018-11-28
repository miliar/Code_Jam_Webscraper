#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>
#include <bitset>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;
const string task = "";

template <class T> T sqr (T x) {return x * x;}

const int nmax = 2100;

int n, m;
int a[nmax], b[nmax], deg[nmax], us[nmax], res[nmax], w[nmax], used[nmax];
vector<int> g[nmax], inp[nmax];
bitset<nmax> t[nmax], buf;

void go(int v, int u) {
	t[u][v] = 1;
	forn(i, g[v].size())
		if (!t[u][g[v][i]])
			go(g[v][i], u);
}

void calc(int v) {
	t[v].reset();
	go(v, v);
}

void add(int v, int u) {
	if (t[v][u]) return;
	forn(j, n)
		if (t[j][v])
			t[j] |= t[u];
	g[v].pb(u);
	inp[u].pb(v);
}

void solve(){
	cin >> n;
	forn(i, n)
		cin >> a[i];
	forn(i, n)
		cin >> b[i];
	forn(i, n) {
		g[i].clear();
		inp[i].clear();
	}
	memset(us, 0, sizeof us);
	memset(used, 0, sizeof us);
	memset(w, 0, sizeof us);
	forn(i, n)
		for (int j = i + 1; j < n; j ++) {
			if (a[j] <= a[i]) {
				g[i].pb(j);
				inp[j].pb(i);
			}
			if (b[j] >= b[i]) {
				g[j].pb(i);
				inp[i].pb(j);
			}
		}
	forn(i, n)
		calc(i);
	forn(i, n) {
		int bst = n + 1;
		int pos = -1;
		if (b[i] == 1) continue;
		bool done = 0;
		for (int j  = i + 1; j < n; j ++)
			if (b[j] + 1 == b[i] && t[i][j]) {
				done = 1;
				break;
			}
		if (done) continue;
		for (int j  = i + 1; j < n; j ++)
			if (b[j] + 1 == b[i]) {
				buf = (t[j] | t[i]);
				int now = buf.count();
				if (now < bst) {
				 	bst = now;
				 	pos = j;
				}
			}
		add(i, pos);
	}
	
	forn(i, n)
		deg[i] = g[i].size();
	m = 0;
	forn(i, n) {
		memset(us, 0, sizeof us);
		int now = 0;
		for (int j = i; j < n; j ++)
			if (t[i][j]) now ++;
		int sm = n;
		forn(j, i)
			if (a[j] + 1 == a[i])
				sm = min(sm, res[j]);
		if (a[i] == 1) sm = -1;
		forn(j, n) {
			if (used[j]) continue;
			now --;
			if (now <= 0 && j > sm) {
				res[i] = j;
				used[j] = 1;
				break;
			}
		}
 		w[i] = 1;
	}
/*	forn(i, n) {
//		forn(j, n)
//			cerr << deg[j] << " ";
//		cerr << endl;
		int pos = n;
		forn(j, n)
			if (deg[j] == 0 && !us[j]) {
				pos = j;
				break;
			}
		res[pos] = i + 1;
		us[pos] = 1;
		forn(j, inp[pos].size())
			deg[inp[pos][j]] --;
    	}*/
    	forn(i, n)
    		cout << res[i] + 1<< " ";
    	cout << endl;


}

int main ()
{
//	freopen("input.txt", "r", stdin);
//   freopen("res", "w", stdout);

	int n;
	cin >> n;

	forn(i, n){
		printf("Case #%d: ", i + 1);
		solve();
	//	puts("");
		cerr << i << " " << clock() << endl;
	}

	
	return 0;
}
