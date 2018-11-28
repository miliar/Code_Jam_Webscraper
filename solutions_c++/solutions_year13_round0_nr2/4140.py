#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

int n, m;
int ntest;
int a[110][110], l[110][110], r[110][110], d[110][110], u[110][110];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> ntest;
	for (int test = 0; test < ntest; test++) {
		cin >> m >> n;
		memset(l, 0, sizeof(l));
		memset(r, 0, sizeof(r));
		memset(d, 0, sizeof(d));
		memset(u, 0, sizeof(u));
		for (int i = 1; i <= m; i++)
			for (int j = 1; j <= n; j++) {
			 	cin >> a[i][j];
			 	u[i][j] = max(u[i - 1][j], a[i][j]);
			 	l[i][j] = max(l[i][j - 1], a[i][j]);
			}
		bool possible = true;
		for (int i = m; i > 0; i--)
			for (int j = n; j > 0; j--) {
				d[i][j] = max(d[i + 1][j], a[i][j]);
				r[i][j] = max(r[i][j + 1], a[i][j]);
				if ((a[i][j] >= u[i - 1][j] && a[i][j] >= d[i + 1][j]) || (a[i][j] >= l[i][j - 1] && a[i][j] >= r[i][j + 1])) continue;
				possible = false;
				goto print;
			}
		print:
		cout << "Case #" << test + 1 << ": ";
		if (possible) cout << "YES"; else cout << "NO"; cout << endl;
	}
}
