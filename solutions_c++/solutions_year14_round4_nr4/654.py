#include <map>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
#define MAXN (1 << 5)
using namespace std;

int n, m;
string str[MAXN];
int ans, amount;

int lcp[MAXN][MAXN];
int srv[MAXN];
vector<string> vec[MAXN];

map<string, int> pos;

void calc() {
	for (int i=0; i < m; ++i) vec[i].clear();
	for (int j=0; j < n; ++j) {
		vec[ srv[j] ].push_back( str[j] );
		//cout << srv[j] << ' ' << str[j] << endl;;
	}


	for (int i=0; i < m; ++i) {
		sort(vec[i].begin(), vec[i].end());
	}

	int curans = 0;
	for (int i=0; i < m; ++i) {
		curans += vec[i][0].size() + 1;
		for (int j=0; j+1 < vec[i].size(); ++j)
			curans += vec[i][j+1].size() - lcp[ pos[ vec[i][j] ] ][ pos[ vec[i][j+1] ] ];
	}

	//cout << "FOUND " << curans << endl;
	//cout << endl;

	if (curans > ans) {
		ans = curans;
		amount = 0;
	}

	if (curans == ans)
		amount ++;
}

void go(int cur, int servermask) {
	if (cur == n) {
		if (servermask+1 != (1 << m))
			return; // empty servers
		calc();
		return;
	}

	for (int i=0; i < m; ++i) {
		srv[cur] = i;
		go(cur+1, servermask | (1 << i));
	}
}

inline void findLcp() {
	for (int i=0; i < n; ++i)
		pos[str[i]] = i;

	for (int i=0; i < n; ++i)
		for (int j=0; j < n; ++j) {
			int to = min(str[i].size(), str[j].size());

			int found = 0;
			for (int k=0; k < to; ++k)
				if (str[i][k] != str[j][k]) {
					lcp[i][j] = k;
					found = 1;
					break;
				}
			if (!found) {
				lcp[i][j] = to;
			}
		}

	/*cout << "LCPs:\n";
	for (int i=0; i < n; ++i)
		for (int j=0; j < n; ++j)
			printf("%d%c", lcp[i][j], (j+1 == n)? '\n' : ' ');*/
}

inline void clear() {
	pos.clear();
	ans = amount = 0;
}

inline void solve() {
	clear();
	findLcp();
	go(0, 0);
	printf("%d %d\n", ans, amount);
}

inline void read() {
	cin >> n >> m;
	for (int i=0; i < n; ++i)
		cin >> str[i];
}

int main() {
	int brt;
	scanf("%d", &brt);

	for (int test=0; test < brt; ++test) {
		printf("Case #%d: ", test+1);
		read();
		solve();
	}
	return 0;
}