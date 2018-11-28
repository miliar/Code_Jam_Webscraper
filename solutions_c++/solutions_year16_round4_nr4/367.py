// run: $exec < d-small1.in > d-small1.out
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <string>

int const maxn = 30;
std::string da[maxn];
int n;
std::vector<int> v;
std::set<int> all[maxn];
bool vis[maxn];

bool dfs(std::vector<int> const& v, int d)
{
	if (d >= n) return true;
	bool ok = false;
	for (auto i : all[v[d]]) {
		if (vis[i]) continue;
		ok = true;
		vis[i] = true;
		if (!dfs(v, d + 1)) return false;
		vis[i] = false;
	}
	return ok;
}

bool judge()
{
	std::vector<int> v;
	for (int i = 0; i < n; i++) v.push_back(i);
	do {
		for (int i = 0; i < n; i++) vis[i] = false;
		if (!dfs(v, 0)) return false;
	} while (std::next_permutation(v.begin(), v.end()));
	return true;
}

int main()
{
	int T; std::cin >> T;
	for (int ti = 1; ti <= T; ti++) {
		std::cout << "Case #" << ti << ": ";
		std::cin >> n;
		v.clear();
		for (int i = 0; i < n; i++) all[i].clear();
		for (int i = 0; i < n; i++) {
			std::cin >> da[i];
			for (int j = 0; j < n; j++)
				if (da[i][j] == '0') v.push_back(i * n + j);
				else all[i].insert(j);
		}
		int ans = 1 << 30;
		int len = v.size();
		for (int s = 0; s < (1 << len); s++) {
			int one = 0, ts = s;
			for (; ts; ts /= 2) one += (ts & 1);
			if (one > ans) continue;
			ts = s;
			for (int t = 0; ts; ts /= 2, t++)
				if (ts & 1) all[v[t] / n].insert(v[t] % n);
			if (judge()) ans = one;
			ts = s;
			for (int t = 0; ts; ts /= 2, t++)
				if (ts & 1) all[v[t] / n].erase(v[t] % n);
		}
		std::cout << ans << '\n';
	}
}

