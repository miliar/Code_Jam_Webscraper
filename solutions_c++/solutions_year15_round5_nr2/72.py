#include <bits/stdc++.h>

using namespace std;

const int M = 1010;

int n, k, s[M];
vector<int> d[M];

void read() {
	cin >> n >> k;
	for (int i = 0; i < n - k + 1; ++i)
		cin >> s[i];
}

void kill() {
	for (int i = 0; i < k; ++i)
		d[i].clear();
	for (int i = 0; i < k; ++i)
		d[i].push_back(0);

	for (int i = 0; i < n - k; ++i)
		d[i % k].push_back(s[i + 1] - s[i]);
	for (int i = 0; i < k; ++i)
		for (int j = 1; j < (int) d[i].size(); ++j)
			d[i][j] += d[i][j - 1];
	int ans = 0, sum = 0, gap = 0;
	std::vector<int> decs;
	for (int i = 0; i < k; ++i) {
		int mi = *min_element(d[i].begin(), d[i].end());
		int ma = *max_element(d[i].begin(), d[i].end());
		sum -= mi;
		decs.push_back(ma - mi);
		ans = max(ans, ma - mi);
	}

	//sort(decs.begin(), decs.end());
	
	for (int d : decs)
		gap += ans - d;

	int r = (s[0] - sum) % k;

	if (r < 0)
		r += k;

	if (r > gap)
		++ans;

	cout << ans << "\n";
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		read();
		kill();
		//cerr << "Test #" << i << " done.\n";
	}
	return 0;
}