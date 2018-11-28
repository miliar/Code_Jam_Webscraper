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
                         
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef double D;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;

template<class T> T abs(T x) { re x > 0 ? x : -x; }

int n;
int m;
vii v[10000];
map<string, int> all;
int o;
int e;
char h[20000];

int q[10000];
int was[10000];
int prev[10000];
int preve[10000];
int cf[100000];
int ct;

int addedge (int a, int b, int c) {
	v[a].pb (mp (b, e));
	cf[e] = c;
	e++;
	v[b].pb (mp (a, e));
	cf[e] = 0;
	e++;
	re 0;
}

int get (string s) {
	if (all.find (s) != all.end ()) re all[s];
	v[o].clear ();
	v[o + 1].clear ();
	addedge (o, o + 1, 1);
	all[s] = o;
	o += 2;
	re o - 2;
}

int go (int S, int T) {
	ct++;
	int l = 0, r = 1;
	q[0] = S;
	while (l < r) {
		int x = q[l++]; 
		if (x == T) re 1;
		for (int i = 0; i < sz (v[x]); i++) {
			int y = v[x][i].fi;
			int z = v[x][i].se;
			if (cf[z] > 0 && was[y] != ct) {
				was[y] = ct;
				prev[y] = x;
				preve[y] = z;
				q[r++] = y;
			}
		}
	}
	re 0;
}


int main () {
	int tt;
	cin >> tt;
	for (int it = 1; it <= tt; it++) {
		all.clear ();
		scanf ("%d", &n);
		for (int i = 0; i < n; i++) v[i].clear ();
		e = 0;
		o = n;
		gets (h);
		for (int i = 0; i < n; i++) {
			gets (h);
			stringstream in (h);
			string s;
			while (in >> s) {
				int x = get (s);
				addedge (i, x, 1e9);
				addedge (x + 1, i, 1e9);
			}
		}
		int ans = 0;
		while (go (0, 1)) {
			ans++;
			int i = 1;
			while (i != 0) {
				int j = prev[i];
				int k = preve[i];
				cf[k]--;
				cf[k ^ 1]++;
				i = j;
			}
		}
		cout << "Case #" << it << ": " << ans;
		cout << endl;
		fprintf (stderr, "%d / %d = %.2f | %.2f\n", it, tt, (double)clock () / CLOCKS_PER_SEC, ((double)clock () / it * tt) / CLOCKS_PER_SEC);
	}
	return 0;
}