#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

vector< vector<int> > g;
int m, n;

const int dx[2] = {0, 1}, dy[2] = {1, 0};

void fill_g(int t) {
	for (int i = 0; i < m; ++i)
		for (int j = 0; j < n; ++j)
			if ((i + j) % 2 == t)
				g[i][j] = 1;
			else
				g[i][j] = 0;
}

void work() {
	scanf("%d%d", &m, &n);
	int k; scanf("%d", &k);

	g.clear();

	for (int i = 0; i < m; ++i) {
		vector<int> f;
		for (int j = 0; j < n; ++j)	f.push_back(0);
		g.push_back(f);
	}

	int ans = -1;
	for (int _ = 0; _ < 2; ++_) {
		fill_g(_);

		vector< pair<int, int> > f;
		if (g[0][0] == 0) f.push_back(make_pair(0, 0));
		if (m != 1 && n != 1 && g[0][n - 1] == 0) f.push_back(make_pair(0, n - 1));
		if (m != 1 && n != 1 && g[m - 1][0] == 0) f.push_back(make_pair(m - 1, 0));
		if (g[m - 1][n - 1] == 0) f.push_back(make_pair(m - 1, n - 1));

		for (int i = 1; i + 1 < n; ++i) {
			if (g[0][i] == 0) f.push_back(make_pair(0, i));
			if (m != 1 && g[m - 1][i] == 0) f.push_back(make_pair(m - 1, i));
		}

		for (int i = 1; i + 1 < m; ++i) {
			if (g[i][0] == 0) f.push_back(make_pair(i, 0));
			if (n != 1 && g[i][n - 1] == 0) f.push_back(make_pair(i, n - 1));
		}

		for (int i = 1; i + 1 < m; ++i)
			for (int j = 1; j + 1 < n; ++j)
				if (g[i][j] == 0) f.push_back(make_pair(i, j));

//for (int i = 0; i < f.size(); ++i) printf("(%d, %d)", f[i].first, f[i].second); puts("");

		int p = k;
		for (int i = 0; i < m; ++i) for (int j = 0; j < n; ++j) if (g[i][j] == 1) p--;
		for (int i = 0; i < p; ++i) g[f[i].first][f[i].second] = 1;

		int cnt = 0;
		for (int i = 0; i < m; ++i)
			for (int j = 0; j < n; ++j)
				for (int a = 0; a < 2; ++a)
					if (i + dx[a] < m && j + dy[a] < n && g[i][j] == 1 && g[i + dx[a]][j + dy[a]] == 1)
						cnt++;

		if (_ == 0) ans = cnt; else if (cnt < ans) ans = cnt;
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
