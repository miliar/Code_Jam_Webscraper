#include <iostream>

#define REP(i,n) for(int i = 0; i < (n); i++)
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)

using namespace std;

char map[200][200];
bool bs[200][200];
int sr[200], sc[200];

int solve() {
	int r, c;
	cin >> r >> c;
	int res = 0;
	REP(i, 200) {
		sr[i] = 0;
		sc[i] = 0;
	}
	REP(i, r) REP(j, c) {
		scanf(" %c", &map[i][j]);
		bs[i][j] = false;
		if (map[i][j] != '.') {
			sr[i]++;
			sc[j]++;
		}
	}
	REP(i, r) REP(j, c) {
		if (map[i][j] != '.') {
			if (map[i][j] == '<') bs[i][j] = true;
			break;
		}
	}
	REP(i, r) FORD(j, c-1, 0) {
		if (map[i][j] != '.') {
			if (map[i][j] == '>') bs[i][j] = true;
			break;
		}
	}
	REP(j, c) REP(i, r) {
		if (map[i][j] != '.') {
			if (map[i][j] == '^') bs[i][j] = true;
			break;
		}
	}
	REP(j, c) FORD(i, r-1, 0) {
		if (map[i][j] != '.') {
			if (map[i][j] == 'v') bs[i][j] = true;
			break;
		}
	}
	REP(i, r) REP(j, c) {
		if (bs[i][j]) {
			res++;
			if (sr[i] <= 1 && sc[j] <= 1) return -1;
		}
	}
	return res;
}

int main() {
	int t;
	cin >> t;
	REP(i, t) {
		cout << "Case #" << i + 1 << ": ";
		int s = solve();
		if (s == -1) {
			cout << "IMPOSSIBLE";
		} else {
			cout << s;
		}
		cout << endl;
	}
}