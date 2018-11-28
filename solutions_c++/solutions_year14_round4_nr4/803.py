#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
using namespace std;

vector<string> ss;
int dist[8];
int M, N;
int mx, mc;

void ev() {
	vector<set<string>> pre;
	for (int i = 0; i < N; i++) pre.push_back(set<string>());
	for (int i = 0; i < M; i++) {
		int d = dist[i];
		string s;
		pre[d].insert(s);
		for (int j = 0; j < ss[i].size(); j++) {
			s += ss[i][j];
			pre[d].insert(s);
		}
	}
	int t = 0;
	for (auto p : pre) {
		t += p.size();
	}
	if (t>mx) {
		mx = t;
		mc = 1;
	}
	else if (t == mx) {
		mc++;
	}
}

void dfs(int p) {
	if (p == M) {
		ev();
		return;
	}
	int &d = dist[p];
	for (d = 0; d < N; d++) {
		dfs(p + 1);
	}
}

void solve() {
	ss.clear();
	mx = 0; mc = 0;
	scanf("%d%d", &M, &N);
	for (int i = 0; i < M; i++) {
		char str[12];
		scanf("%s", str);
		ss.push_back(str);
	}
	dfs(0);

	printf("%d %d\n", mx, mc);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int c = 1; c <= T; c++) {
		printf("Case #%d: ", c);
		solve();
	}
}