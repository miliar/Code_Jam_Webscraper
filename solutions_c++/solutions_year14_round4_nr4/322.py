#include <bits/stdc++.h>
#define all(x) begin(x), end(x)
using namespace std;
void E(){}template<class A,class...B>void E(A _,B...$){cerr<<' '<<_;E($...);}
#define E($...) E(#$,'=',$,'\n')

int m, n;
vector<string> s;

int bestnodes;
int bestvars;

vector<set<string>> server;

void rec(int i) {
	if (i >= m) {
		int nodes = 0;
		for (auto &serv: server) {
			if (serv.empty()) return;
			nodes += serv.size();
		}
		if (nodes > bestnodes) {
			bestnodes = nodes;
			bestvars = 0;
		}
		if (nodes == bestnodes) ++bestvars;
		return;
	}
	int l = s[i].length();
	for (int q = 0; q < n; ++q) {
		int j;
		for (j = l; j >= 0; --j) {
			bool ins;
			tie(ignore, ins) = server[q].insert(s[i].substr(0, j));
			if (!ins) break;
		}
		rec(i + 1);
		for (++j; j <= l; ++j) {
			server[q].erase(s[i].substr(0, j));
		}
	}
}

void process() {
	cin >> m >> n;
	s.resize(m);
	server.assign(n, set<string>{});
	for (auto &ss: s) cin >> ss;
	bestvars = bestnodes = -1;
	rec(0);
	printf("%d %d\n", bestnodes, bestvars);
}

int main() {
	ios_base::sync_with_stdio(false);
	int tcases;
	cin >> tcases;
	for (int tcase = 1; tcase <= tcases; ++tcase) {
		printf("Case #%d: ", tcase);
		process();
	}
	return 0;
}
