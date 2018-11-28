#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <unordered_map>
using namespace std;

const int MAX_N = 55;
const int MAX = 1000000000;
int N;
int grid[MAX_N][MAX_N];
int lists[2 * MAX_N][MAX_N];
unordered_multimap<int, vector<int>> ll;

multiset<int> solve(int m1, int m2) {
	set<pair<int, int>> foundLists;
	foundLists.insert({m1, 0});
	if (m2 != -1) {
		multiset<int> starts;
		foundLists.clear();
		for (int i = 0; i < N; ++i) {
			starts.insert(lists[m1][i]);
			starts.insert(lists[m2][i]);
		}
		for (int i = 0; i < 2 * N - 1; ++i) {
			starts.erase(starts.find(lists[i][0]));
		}
		auto a = *starts.begin();
		set<pair<int, int>> startVals;
		for (int i = 0; i < N; ++i) {
			int corres = -1;
			if (lists[m1][i] == a)
				corres = lists[m2][i];
			if (lists[m2][i] == a)
				corres = lists[m1][i];
			if (corres != -1)
				startVals.insert({corres, i});
		}
		for (auto v : startVals) {
			for (int i = 0; i < 2 * N - 1; ++i) {
				if (lists[i][0] == v.first) {
					foundLists.insert({i, v.second});
				}
			}
		}
	}
	for (auto v : foundLists) {
		multiset<int> starts;
		int level = v.second;
		int foundList = v.first;
		for (int i = 0; i < 2 * N - 1; ++i) {
			starts.insert(lists[i][level]);
		}
		starts.insert(lists[foundList][level]);
		bool good = true;
		for (int i = 0; i < N; ++i) {
			auto iter = starts.find(lists[foundList][i]);
			if (iter == starts.end()) {
				good = false;
				break;
			}
			starts.erase(iter);
		}
		if (!good) continue;

		for (auto i : starts) {
			if (starts.count(i) != 1) {
				good = false;
				break;
			}
		}
		if (good) return starts;
	}
	return {};
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d", &N);
		int m = MAX;
		int m1 = -1, m2 = -1;
		for (int i = 0; i < 2 * N - 1; ++i) {
			for (int j = 0; j < N; ++j) {
				scanf("%d", &lists[i][j]);
			}
			if (lists[i][0] < m) {
				m = lists[i][0];
				m1 = i; m2 = -1;
			} else if (lists[i][0] == m) {
				m2 = i;
			}
		}
		auto aa = solve(m1, m2);
		printf("Case #%d: ", t);
		int idx = 0;
		for (auto i : aa) {
			printf("%d", i);
			if (idx++ != N) printf(" ");
		}
		printf("\n");

	}
}