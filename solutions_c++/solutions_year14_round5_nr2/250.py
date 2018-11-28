#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

const int N = 105;

int n, p, q;
int h[N], g[N];
map<vector<int>, int> mem;

int dfs(vector<int> a) {
	if (mem.count(a)) return mem[a];
	int flag = 0;
	for (int i = 0; i < n; i++) flag |= a[i] >= 1;
	if (!flag) return 0;
	
	int ans = 0;
	for (int i = 0; i < n; i++)
	if (a[i] >= 1) {
		a[i] -= p;
		int re = 0;
		if (a[i] < 1) re += g[i];
		int j = 0;
		while (j < n && a[j] < 1) j++;
		a[j] -= q;
		ans = max(ans, dfs(a) + re);
		a[j] += q;
		a[i] += p;
	}
	{
		int re = 0;
		int j = 0;
		while (j < n && a[j] < 1) j++;
		a[j] -= q;
		ans = max(ans, dfs(a)) + re;
		a[j] += q;
	}
	
	return mem[a] = ans;
}

void solve() {
	cin >> p >> q >> n;
	for (int i = 0; i < n; i++) cin >> h[i] >> g[i];
	mem.clear();
	vector<int> tmp;
	for (int i = 0; i < n; i++) tmp.push_back(h[i]);
	cout << dfs(tmp);
}

int main() {
	//ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
	}
}