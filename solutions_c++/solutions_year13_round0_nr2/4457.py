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

typedef long long ll;
typedef pair <int, int> pie;

const int maxN = 100 + 1;

int n, m, a[maxN][maxN], r[maxN], c[maxN];

main() {
	ios::sync_with_stdio (false);
	
	int o; cin >> o;
	for (int t = 0; t < o; t++) {
		int n, m; cin >> n >> m;
		memset (r, 0, sizeof r);
		memset (c, 0, sizeof c);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				cin >> a[i][j], r[i] = max (r[i], a[i][j]), c[j] = max (c[j], a[i][j]);
		bool valid = true;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (a[i][j] < r[i] && a[i][j] < c[j]) valid = false;
		cout << "Case #" << t + 1 << ": " << (valid ? "YES" : "NO") << endl;
	}

	return 0;
}
