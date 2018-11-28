#include <bits/stdc++.h>
using namespace std;
const int maxl = 100000, maxn = 22;

char buf[maxl];
vector<string> word[maxn];
vector<int> ids[maxn];
int n;

int main() {
	int Tc;
	scanf("%d", &Tc);
	for (int Tn = 1; Tn <= Tc; ++Tn) {
		scanf("%d ", &n);
		for (int i = 0; i < n; ++i) {
			word[i].clear();
			ids[i].clear();
			gets(buf);
			istringstream sin(buf);
			string w;
			while (sin >> w) {
				word[i].push_back(w);
			}
		}
		unordered_map<string, int> s2id;
		int curid = 0;
		for (int i = 0; i < n; ++i) {
			for (const auto &w : word[i]) {
				if (s2id.find(w) != s2id.end())
					ids[i].push_back(s2id[w]);
				else {
					s2id[w] = curid++;
					ids[i].push_back(s2id[w]);
				}
			}
		}

		int ms = 1 << (n - 2);
		int ans = word[0].size();

#pragma omp parallel for reduction(min: ans)
		for (int i = 0; i < ms; ++i) {
			int ti = (i << 2) | 1;
			unordered_set<int> s1, s2;
			for (int j = 0; j < n; ++j)
				if (ti & (1 << j)) {
					s1.insert(ids[j].begin(), ids[j].end());
				} else {
					s2.insert(ids[j].begin(), ids[j].end());
				}
			int cnt = 0;
			if (s1.size() < s2.size()) {
				for (const auto &w : s1) {
					if (s2.find(w) != s2.end())
						cnt++;
				}
			} else {
				for (const auto &w : s2) {
					if (s1.find(w) != s1.end())
						cnt++;
				}
			}
			if (cnt < ans)
				ans = cnt;
		}

		printf("Case #%d: ", Tn);
		printf("%d\n", ans);
		fflush(stdout);
	}
	return 0;
}
