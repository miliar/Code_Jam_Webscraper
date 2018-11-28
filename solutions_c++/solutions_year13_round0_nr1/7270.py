#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <stdio.h>
#include <sstream>
#include <string>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <time.h>
#include <cstring>

using namespace std;

#define FOR(i,s,e) for (int i = int(s); i < int(e); i++)
#define FORIT(i,c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define ISEQ(c) (c).begin(), (c).end()
#define sz(v) (int) v.size()
#define mp make_pair
#define pb push_back
#define all(s) s.begin(), s.end()
#define foreach(i,c) for(__typeof((c).begin()) i = (c).begin() ; i != (c).end() ; i++)

int main() {
	freopen("A-large.in", "rt", stdin);
	freopen("out.out", "wt", stdout);
	int T, count = 1;
	string str;
	cin >> T;
	while (T--) {
		vector<string> v(4);
		bool X = 0, O = 0, dot = 0;
		FOR(i, 0, 4) {
			cin >> v[i];
		}
		FOR(i, 0, 4) {
			int cntX = 0, cntO = 0;
			FOR(j, 0, 4) {
				if (v[i][j] == 'X' || v[i][j] == 'T')
					cntX++;
				if (v[i][j] == 'O' || v[i][j] == 'T')
					cntO++;
				if (v[i][j] == '.')
					dot = 1;
			}
			if (cntX == 4)
				X = 1;
			if (cntO == 4)
				O = 1;
		}
		FOR(j, 0, 4) {
			int cntX = 0, cntO = 0;
			FOR(i, 0, 4) {
				if (v[i][j] == 'X' || v[i][j] == 'T')
					cntX++;
				if (v[i][j] == 'O' || v[i][j] == 'T')
					cntO++;
			}
			if (cntX == 4)
				X = 1;
			if (cntO == 4)
				O = 1;
		}
		int cntX = 0, cntO = 0;
		FOR(i, 0, 4) {
			if (v[i][i] == 'X' || v[i][i] == 'T')
				cntX++;
			if (v[i][i] == 'O' || v[i][i] == 'T')
				cntO++;
		}
		if (cntX == 4)
			X = 1;
		if (cntO == 4)
			O = 1;
		cntX = 0;
		cntO = 0;
		for (int i = 0, j = 3; i < 4; i++, j--) {
			if (v[i][j] == 'X' || v[i][j] == 'T')
				cntX++;
			if (v[i][j] == 'O' || v[i][j] == 'T')
				cntO++;
		}
		if (cntX == 4)
			X = 1;
		if (cntO == 4)
			O = 1;

		cout << "Case #" << count++ << ": ";
		if (X)
			cout << "X won" << endl;
		else if (O)
			cout << "O won" << endl;
		else if (!dot)
			cout << "Draw" << endl;
		else
			cout << "Game has not completed" << endl;
	}
	return 0;
}
