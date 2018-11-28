#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

typedef pair<int, int> PII;

vector<PII> f[111];
int n;

inline int calc(vector<int>& g, int k) {
	int ret = 0;
	for (size_t i = 0; i < g.size(); ++i)
		ret += abs(g[i] - k);
	return ret;
}

void work() {
	cin >> n;
	for (int i = 0; i < n; ++i) {
		f[i].clear();
		string str; cin >> str;
		for (size_t k = 0; k < str.size(); ) {
			int p = str[k] - 'a'; size_t j = k;
			while (j < str.size() && str[j] == str[k]) ++j;
			f[i].push_back(make_pair(p, j - k)); k = j;
		}
	}

	size_t s = f[0].size();
	for (int i = 0; i < n; ++i) {
		if (f[i].size() != s) {
			puts("Fegla Won"); return ;
		}
	}

	int ans = 0;
	for (size_t k = 0; k < s; ++k) {
		vector<int> g;
		int p = f[0][k].first;
		for (int i = 0; i < n; ++i) {
			if (f[i][k].first != p) {
				puts("Fegla Won"); return ;
			}
			g.push_back(f[i][k].second);
		}
		sort(g.begin(), g.end());
		ans += min(calc(g, g[n / 2]), calc(g, g[n / 2 - 1]));
	}

	printf("%d\n", ans);
}

int main() {
	int T; scanf("%d", &T);

	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: ", t);
		work();
	}

	return 0;
}
