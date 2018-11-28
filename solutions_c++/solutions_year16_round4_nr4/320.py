#include <bits/stdc++.h>

const int N = 30;

int n;
int edgeState;

void init() {
	std::cin >> n;
	std::string ss;
	for (int i = 0; i < n; i ++) {
		std::string str;
		std::cin >> str;
		ss += str;
	}
	edgeState = 0;
	for (int i = 0; i < (int)ss.length(); i ++) {
		if (ss[i] == '1') {
			edgeState |= 1 << i;
		}
	}
}

int bit(int state, int x, int y) {
	return (state >> ((x - 1) * n + y - 1)) & 1;
}

bool dfs(int order[], int x, bool visit[], int state) {
	if (x == n + 1) {
		return true;
	}
	bool tag = false;
	for (int i = 1; i <= n; i ++) {
		if (visit[i] == false && bit(state, order[x], i)) {
			tag = true;
			visit[i] = true;
			if (!dfs(order, x + 1, visit, state)) {
				return false;
			}
			visit[i] = false;
		}
	}
	return tag;
}

bool check(int state) {
	static int order[N];
	static bool visit[N];
	
	for (int i = 1; i <= n; i ++) {
		order[i] = i;
	}
	
	do {
		memset(visit, false, sizeof(visit));
		if (!dfs(order, 1, visit, state)) {
			return false;
		}
	} while (std::next_permutation(order + 1, order + n + 1));
	
	return true;
}

void work() {
	int answer = n * n + 100;
	for (int state = 0; state < (1 << (n * n)); state ++) {
		if ((edgeState & state) != 0) {
			continue;
		}
		if (check(edgeState | state)) {
			answer = std::min(answer, __builtin_popcount(state));
		}
	}
	std::cout << answer << std::endl;
}

int main() {
	freopen("d0.in", "r", stdin);
	freopen("d0.out", "w", stdout);
	
	int testCnt;
	std::cin >> testCnt;
	for (int i = 1; i <= testCnt; i ++) {
		printf("Case #%d: ", i);
		init();
		work();
	}
	
	return 0;
}
