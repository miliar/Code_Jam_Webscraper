#include <algorithm>
#include <iostream>
#include <cstring>
#include <sstream>
#include <vector>
#include <cmath>
#include <set>
#include <map>

using namespace std;

#define int long long
#define double long double

#define ff first
#define ss second
#define mp make_pair
#define sqr(x) ((x)*(x))

typedef long long ll;
typedef pair <int, int> pie;

const int maxN = 2000 + 100;

int n, a[maxN], b[maxN];
int g[maxN][maxN], deg[maxN];
int res[maxN];

void solve() {
	memset (g, 0, sizeof g);
	memset (deg, 0, sizeof deg);

	cin >> n;
	for (int i = 0; i < n; i++) cin >> a[i];
	for (int i = 0; i < n; i++) cin >> b[i];
	
	for (int i = 0; i < n; i++) {
		int fs = -1, fb = -1;
		for (int j = 0; j < i; j++) {
			if (a[j] == a[i]) fs = j;
			if (a[j] == a[i] - 1) fb = j;
		}
		if (fs != -1) g[i][fs] = 1;// cerr << i << ' ' << fs << endl;
		if (fb != -1) g[fb][i] = 1;// cerr << fb << ' ' << i << endl;
	}
	for (int i = n - 1; i >= 0; i--) {
		int fs = -1, fb = -1;
		for (int j = n - 1; j > i; j--) {
			if (b[j] == b[i]) fs = j;
			if (b[j] == b[i] - 1) fb = j;
		}
		if (fs != -1) g[i][fs] = 1;// cerr << i << ' ' << fs << endl;;
		if (fb != -1) g[fb][i] = 1;// cerr << fb << ' ' << i << endl;;
	}

	set <int> source;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++)
			deg[i] += g[j][i];
		if (!deg[i]) source.insert (i);
	}

	for (int i = 1; source.size(); i++) {
		int x = *source.begin();
		source.erase (x);
		for (int j = 0; j < n; j++)
			if (g[x][j]) {
				deg[j]--;
				if (deg[j] == 0) source.insert (j);
			}
		res[x] = i;
	}

	for (int i = 0; i < n; i++) cout << res[i] << ' '; cout << endl;
}

main() {
	ios::sync_with_stdio (false);
	
	int tests; cin >> tests;
	for (int o = 1; o <= tests; o++) {
		cout << "Case #" << o << ": ";
		solve();
	}

	return 0;
}
