#include <bits/stdc++.h>
using namespace std;
map<string, int> id;
vector<int> sent[205];
bool belong[2205][2];
int main() {
	int TC;
	scanf("%d", &TC);
	for (int cn = 1; cn <= TC; ++cn) {
		int ans = INT_MAX;
		int N;
		scanf("%d", &N);
		cin.ignore();
		int lastid = 0;
		id.clear();
		for (int i = 0; i < N; ++i) {
			sent[i].clear();
			string line;
			getline(cin, line);
			stringstream ss(line);
			string word;
			while (ss >> word) {
				if (!id[word]) {
					id[word] = lastid = id.size() + 1;
				}
				sent[i].push_back(id[word]);
			}
		}
		for (int i = 0; i < (1 << (N - 2)); ++i) {
			memset(belong, 0, sizeof(belong));
			for (int w : sent[0]) belong[w][0] = true;
			for (int w : sent[1]) belong[w][1] = true;
			for (int j = 0; j < N - 2; ++j) {
				bool lang = (i & (1 << j));
				for (int w : sent[2 + j])
					belong[w][lang] = true;
			}
			int cnt = 0;
			for (int j = 1; j <= lastid; ++j)
				cnt += (belong[j][0] && belong[j][1]);
			ans = min(ans, cnt);
		}
		printf("Case #%d: %d\n", cn, ans);
	}
}

