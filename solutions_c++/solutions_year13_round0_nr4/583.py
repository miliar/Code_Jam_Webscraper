#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>

using namespace std;

const int MAXN = 20;
const int MAXK = 200;

int n, k;
int startKeys[MAXK];
int need[MAXN];
vector<int> keys[MAXN];

string opt[1 << MAXN];
int visited[1 << MAXN];

string solve() {
	int S = (1 << n);
	fill(visited, visited + S, false);

	opt[0] = "";
	visited[0] = true;

	int holding[MAXK];
	char buf[100];

	for (int s = 0; s < S; ++s) if (visited[s]) {
		copy(startKeys, startKeys + MAXK, holding);
		for (int i = 0; i < n; ++i) if (s & (1 << i)) {
			holding[need[i]]--;
			for (int j = 0; j < (int)keys[i].size(); ++j)
				holding[keys[i][j]]++;
		}

		for (int i = 0; i < n; ++i) if ((s & (1 << i)) == 0) {
			if (holding[need[i]] == 0) continue;
			sprintf(buf, "%02d", i);
			string way = opt[s] + string(buf);

			int ns = s + (1 << i);
			if (!visited[ns] || opt[ns] > way) {
				visited[ns] = true;
				opt[ns] = way;
			}
		}
	}

	if (!visited[S - 1]) return "IMPOSSIBLE";
	else {
		string res = "";
		for (int i = 0; i < n; ++i) {
			if (i > 0) res += " ";
			string si = opt[S - 1].substr(i * 2, 2);

			int k = (si[0] - '0') * 10 + (si[1] - '0');
			k++;
			sprintf(buf, "%d", k);
			res += buf;
		}
		return res;
	}
}

int main() {
	int t;
	scanf("%d", &t);
	for (int c = 1; c <= t; ++c) {
		scanf("%d%d", &k, &n);
		fill(startKeys, startKeys + MAXK, 0);
		for (int i = 0; i < k; ++i) {
			int key;
			scanf("%d", &key);
			startKeys[key]++;
		}

		for (int i = 0; i < n; ++i) {
			int hasCount;
			scanf("%d%d", need + i, &hasCount);
			keys[i].clear();
			while (hasCount--) { int x; scanf("%d", &x); keys[i].push_back(x); }
		}

		printf("Case #%d: %s\n", c, solve().c_str());
	}
}
