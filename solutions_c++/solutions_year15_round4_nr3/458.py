#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <memory.h>
#include <vector>
#include <sstream>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <complex>

using namespace std;

#define REP(a,b) for (int a=0; a<(int)(b); ++a)
#define FOR(a,b,c) for (int a=(b); a<(int)(c); ++a)

int n;
vector <string> lines;
vector <string> words[201];
set <string> swords[201];

vector <string> tokenize(string s) {
	vector < string > res;
	string tok;

	stringstream ss(s);

	while (ss >> tok) res.push_back(tok);

	return res;
}

void read_input() {
	string s;
	cin >> n;
	getline(cin, s);

	lines.clear();
	REP(i, n) {
		getline(cin, s);
		lines.push_back(s);
		words[i].clear();
		words[i] = tokenize(s);
		swords[i].clear();
		swords[i].insert(words[i].begin(), words[i].end());
	}
}


void solve() {
	int res = 9999999;
	
	set <string> allw;
	REP(i, n) REP(j, words[i].size()) allw.insert(words[i][j]);
	
	vector <int> wmask;
	for (string w : allw) {
		int msk = 0;
		REP(i, n) if (swords[i].count(w) > 0) msk |= 1 << i;
		wmask.push_back(msk);
	}



	REP(mask, 1 << (n - 2)) {
		int engmsk = (mask << 2) | 1;
		int framsk = ((1 << n) - 1) ^ engmsk;
		int cnt = 0;
		for (int msk : wmask)
			if ((msk&engmsk) && (msk&framsk)) ++cnt;
		res = min(res, cnt);
	}
	
	cout << res << endl;
}


int main(int argc, char* argv[]) {
	int nt, single_tc = 0;

	if (argc > 1) {
		sscanf(argv[1], "%d", &single_tc);
	}

	scanf("%d", &nt);
	for (int t = 1; t <= nt; ++t) {
		read_input();
		if (single_tc == 0 || single_tc == t) {
			printf("Case #%d: ", t);
			solve();
		}
		cerr << t << endl;
	}

	return 0;
}