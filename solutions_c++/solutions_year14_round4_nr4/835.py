#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <cstring>

using namespace std;

const int MX = 15;

int m, n, ile0, ile1;
char s[MX][MX];

vector<int> t;

void check() {
	bool mam[MX];
	fill(mam, mam+MX, false);
	map<string, bool> T[MX];
	for (int i = 0; i < m; i++) {
		mam[t[i]] = true;
		int l = strlen(s[i+1]+1);
		string tmp = "";
		for (int j = 1; j <= l; j++) {
			tmp = tmp + s[i+1][j];
			T[t[i]][tmp] = true;
		}
	}
	for (int i = 0; i < n; i++) if (!mam[i]) return;
	int w = n;
	for (int i = 0; i < n; i++) w = w + T[i].size();
	if (w > ile0) {
		ile0 = w;
		ile1 = 0;
	}
	if (w == ile0) ile1++;
}

void gen() {
	if (int(t.size()) == m) check();
	else {
		for (int i = 0; i < n; i++) {
			t.push_back(i);
			gen();
			t.pop_back();
		}
	}
}

void solve(int testcase) {
	ile0 = ile1 = 0;
	scanf("%d%d", &m, &n);
	for (int i = 1; i <= m; i++) {
		scanf("%s", s[i]+1);
	}
	gen();
	printf("Case #%d: %d %d\n", testcase, ile0, ile1);
}

int main() {
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) solve(i);
	return 0;
}