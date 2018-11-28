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

#define ff first
#define ss second
#define mp make_pair
#define sqr(x) ((x)*(x))
#define map shit

typedef long long ll;
typedef pair <int, int> pie;

const int maxN = (1 << 20) + 10;
const int maxK = 200 + 10;
const int maxM = 40 + 10;

int a[maxN][maxM], n, k;
int map[maxK];
int key[maxM];
vector <int> v[maxM];
int reach[maxN], valid[maxN];
int res[maxN];

void printRes (int mask) {
	if (mask == (1 << n) - 1) return;
	printRes (mask ^ (1 << res[mask]));
	cout << res[mask] + 1 << ' ';
}

int find (int mask) {
	if (reach[mask]) return reach[mask];
	if (!valid[mask]) return reach[mask] = -1;
	if (mask == 0) return reach[mask] = 1;
	for (int i = 0; i < n; i++) if (mask & (1 << i)) {
		if (a[mask][map[key[i]]] == 0) continue;
		if (find (mask ^ (1 << i)) == -1) continue;
		res[mask ^ (1 << i)] = i;
		return reach[mask] = 1;
	}
	return reach[mask] = -1;
}

main() {
	ios::sync_with_stdio (false);
	
	int o; cin >> o;
	for (int t = 0; t < o; t++) { 
		memset (reach, 0, sizeof reach);
		memset (valid, 0, sizeof valid);
		memset (res, 0, sizeof res);
		memset (a, 0, sizeof a);

		cin >> k >> n;
		vector <int> init; set <int> s;
		for (int i = 0; i < k; i++) { int x; cin >> x; init.push_back (x); s.insert (x); }
		for (int i = 0; i < n; i++) {
			v[i].clear();
			cin >> key[i]; s.insert (key[i]);
			int t, x; cin >> t;
			while (t --> 0)
				cin >> x, v[i].push_back (x), s.insert (x);
		}

		int tmp = 0;
		for (set <int>::iterator it = s.begin(); it != s.end(); it++) {
			map[*it] = tmp;
			tmp++;
		}
		cerr << "Test " << t + 1 << ' ' << k << ' ' << n << ' ' << tmp << endl;

		for (int i = 0; i < init.size(); i++) a[(1 << n) - 1][map[init[i]]]++;

		for (int i = (1 << n) - 1, j; i >= 0; i--) {
			valid[i] = true;
			for (j = 0; j < n; j++)
				if ((i & (1 << j)) == 0) {
					for (int k = 0; k < tmp; k++)
						a[i][k] = a[i + (1 << j)][k];
					a[i][map[key[j]]]--;
					for (int k = 0; k < v[j].size(); k++) a[i][map[v[j][k]]]++;
					for (int k = 0; k < tmp; k++)
						if (a[i][k] < 0) valid[i] = false;
				}
		}

		cout << "Case #" << t + 1 << ": ";
		if (find ((1 << n) - 1) == -1) cout << "IMPOSSIBLE";
		else printRes (0); cout << endl;
	}

	return 0;
}
