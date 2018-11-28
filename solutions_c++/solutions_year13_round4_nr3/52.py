#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cassert>
#include <ctime>

using namespace std;

#define sqr(a) ((a)*(a))
#define two(a) (1 << (a))
#define has(mask, a) ((mask) & two(a) ? 1 : 0)

int n, a[2005], b[2005], les[2005][2005], was[2005], p[2005];

vector <int> ans;

void load() {
	cin >> n;

	for (int i = 0;i < n;i++) {
	 	cin >> a[i];
	}
	for (int i = 0;i < n;i++) {
	 	cin >> b[i];
	}
}

void dfs (int v) {
	was[v] = 1;
	for (int i = 0;i < n; i++) {
		if (les[v][i] && !was[i])
			dfs (i);
	}
	ans.push_back (v);
}
 
void solve(int test) {
	memset (les, 0, sizeof (les));

	for (int i = 1;i < n;i++) {
	 	for (int j = 0;j < i;j++) {
	 	 	if (a[j] >= a[i]) {
	 	 	 	les[i][j] = 1;
	 	 	}
	 	}
	 	for (int j = i - 1;j >= 0;j--) {
	 	 	if (a[j] == a[i] - 1) {
	 	 	 	les[j][i] = 1;
	 	 	 	break;
	 	 	}
	 	}
	}

	for (int i = n - 2;i >= 0;i--) {
	 	for (int j = i + 1;j < n;j++) {
	 	 	if (b[j] >= b[i]) {
	 	 	 	les[i][j] = 1;
	 	 	}
	 	}

	 	for (int j = i + 1;j < n;j++) {
	 	 	if (b[j] == b[i] - 1) {
	 	 	 	les[j][i] = 1;
	 	 	 	break;
	 	 	}
	 	}
	}

	for (int k = 0;k < n;k++) {
	 	for (int i = 0;i < n;i++) {
	 	 	for (int j = 0;j < n;j++) {
	 	 	 	if (les[i][k] && les[k][j]) {
	 	 	 	 	les[i][j] = 1;
	 	 	 	}
	 	 	}
	 	}
	}

	/*for (int i = 0;i < n;i++) {
	 	for (int j = 0;j < n;j++) {
	 	 	cerr << les[i][j] << " ";
	 	}
	 	cerr << endl;
	}
	cerr << endl;*/

	memset (was, 0, sizeof (was));
	ans.clear();

	for (int i = n - 1;i >= 0;i--) {
		if (!was[i]) {
			dfs (i);
		}
	}
	reverse (ans.begin(), ans.end());

	for (int i = 0;i < n;i++) {
	 	for (int j = 0;j < n - 1;j++) {
	 		if (ans[j] < ans[j + 1]) continue;

	 		if (!les[ans[j]][ans[j + 1]] && !les[ans[j + 1]][ans[j]]) {
	 		 	swap (ans[j], ans[j + 1]);
	 		}
	 	}
	}

	for (int i = 0;i < n;i++) {
		p[ans[i]] = i + 1;
	}
	cerr << test << " ";

	printf ("Case #%d: ", test);
	for (int i = 0;i < n;i++) {
	 	cout << p[i] << " ";
	}
	cout << endl;
}

int main() {
 	freopen ("a.in", "r", stdin);
 	freopen ("a.out", "w", stdout);

 	int t;
 	scanf ("%d\n", &t);

 	for (int i = 1;i <= t;i++) {
 		load();
 		solve(i);
 	}

 	return 0;
}