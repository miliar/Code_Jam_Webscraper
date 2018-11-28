#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define mp make_pair
typedef pair<int, int> pii;

#define MAX_VERT 10000005
#define MAX_ARC 100001000
#define INF 1<<30
typedef int flowtype;
const int kFirst = MAX_VERT - 3, kLast = MAX_VERT - 2;
const int kInf = INF;

int Cost(const vector<string> &S) {
	set<string> s;
	for (int i = 0; i < S.size(); ++i) {
		for (int k = 0; k < S[i].size(); ++k) {
			s.insert(S[i].substr(0, k + 1));
		}
	}
	return s.size() + 1;
}


void Solve() {
	vector<string> V;
	int ret = 0, qret = 0;
	int n, m;
	string s;
	cin >> n >> m;
	for (int i = 0; i < n; ++i) {
		cin >> s;
		V.push_back(s);
	}
	int p[20] = {};
	while (true) {
		int cur = 0;
		while (p[cur] == m) {
			++p[cur + 1];
			p[cur] = 0;
			++cur;
		}
		if (p[n] != 0) {
			break;
		}
		int tret = 0;
		bool bad = false;
		for (int i = 0; i < m; ++i) {
			vector<string> vv(0);
			for (int j = 0; j < n; ++j) {
				if (p[j] == i) {
					vv.push_back(V[j]);
				}
			}
			if (vv.empty()) {
				bad = true;
			}
			tret += Cost(vv);
		}
		if (!bad) {
			if (tret > ret) {
				ret = tret;
				qret = 1;
			} else if (tret == ret) {
				++qret;
			}
		}
		++p[0];
		if (1 == m) {
			break;
		}
	}
	printf("%d %d\n", ret, qret);
}


int main() {
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int I = 0; I < T; ++I) {
		printf("Case #%d: ", I + 1);
		Solve();
	}
	return 0;
}