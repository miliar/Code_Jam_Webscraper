#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <vector>

using namespace std;

typedef vector < int > Array;

#define maxn 1048576

Array ans[maxn];
Array a, b, x;
int n;
int used[maxn];

int proc(int id, int cnt) {
	//cerr << "proc " << id << " " << cnt << endl;
	if (used[id] != -1)
		return used[id];
	if (cnt == 0) {
		used[id] = 1;
		ans[id] = Array(n, 2 * n);
		return 1;
	}
	used[id] = 0;
	ans[id] = Array(n, 2 * n);
	for (int i = 0; i < n; ++i) {
		if (id & (1 << i)) {
			if (!proc(id ^ (1 << i), cnt - 1)) continue;
			int mask = id ^ (1 << i);
			int aa = 1, bb = 1;
			for (int j = 0; j < i; ++j)
				if (mask & (1 << j))
					if (a[j] + 1 > aa)
						aa = a[j] + 1;
			for (int j = n - 1; j > i; --j)
				if (mask & (1 << j))
					if (b[j] + 1 > bb)
						bb = b[j] + 1;
			if (a[i] == aa && b[i] == bb) {
				used[id] = 1;
				if (ans[mask] < ans[id])
					ans[id] = ans[mask];
			}
		}
	}
	if (used[id] == 1) {
		for (int i = 0; i < n; ++i)
			if ((id & (1 << i)) && ans[id][i] == 2 * n) {
				ans[id][i] = cnt; break;
			}
	}
	return used[id];
}

int solve(int id) {
	cout << "Case #" << id << ": ";
	cerr << "case #" << id << ":" << endl;
	cin >> n;
	a.assign(n, 0);
	b.assign(n, 0);
	for (int i = 0; i < n; ++i) cin >> a[i];
	for (int i = 0; i < n; ++i) cin >> b[i];
	memset(used, -1, (1 << n) * sizeof(int));
	proc((1 << n) - 1, n);
	Array x = ans[(1 << n) - 1];
	for (int i = 0; i < n; ++i) cout << x[i] << " ";
	cout << '\n';
	return 0;
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
		solve(i + 1);
	return 0;
}
