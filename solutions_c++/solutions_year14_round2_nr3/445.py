#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>

#define REP(i, n) for(int i = 0; i < (n); i++)
#define FOR(i, x, y) for(int i = (x); i <= (y); i++)
#define RFOR(i, x, y) for(int i = (x); i >= (y); i--)

#define REMIN(x, y) x = (x < (y)) ? x : (y)
#define REMAX(x, y) x = (x > (y)) ? x : (y)

//#define DEBUG

#ifndef DEBUG
#define ISDEBUG false
#define PRINT(x)
#else
#define ISDEBUG true
#define PRINT(x) cout << #x << ": " << x << endl
#endif
#define IFDEBUG() if(ISDEBUG)

using namespace std;

#define MAX 1024

int n, m, postal[MAX], _map[MAX][MAX];
int ans[MAX], use[MAX], tmp[MAX], tt[MAX][MAX];

void read_input() {
	REP(i, MAX)ans[i] = 0;
	scanf("%d %d", &n, &m);
	FOR(i, 1, n) {
		scanf("%d", &postal[i]);
		use[i] = 0;
		FOR(j, 1, n) {
			_map[i][j] = 0;
		}
	}
	int x, y;
	REP(i, m) {
		scanf("%d %d", &x, &y);
		_map[x][y] = 1;
		_map[y][x] = 1;
	}
}

void run(int x, int index) {
	if(ans[index - 1] != 0) {
		if(postal[ans[i]] > postal[tmp[i]])break;
	}
	if(index == n) {
		if(ans[0] == 0) {
			REP(i, n)ans[i] = tmp[i];
			return;
		}
		REP(i, n) {
			if(postal[ans[i]] < postal[tmp[i]])return;
			if(postal[ans[i]] > postal[tmp[i]])break;
		}
		REP(i, n)ans[i] = tmp[i];
		return;
	}
	FOR(i, 1, n) {
		if(use[i])continue;
		if(_map[x][i]) {
			REP(k, index) {
				tt[index][k] = tt[index - 1][k];
			}
			tt[index][index] = 0;

			tmp[index] = i;
			use[i] = 1;
			run(i, index + 1);
			use[i] = 0;
		}

		RFOR(j, index - 1, 0) {
			if(tt[index - 1][j])continue;
			if(_map[tmp[j]][i]) {
				REP(k, index) {
					tt[index][k] = tt[index - 1][k];
				}
				RFOR(k, index - 1, j + 1) {
					tt[index][k] = 1;
				}
				tt[index][index] = 0;

				tmp[index] = i;
				use[i] = 1;
				run(i, index + 1);
				use[i] = 0;
			}
		}
	}
}

void find_ans() {
	read_input();

	FOR(i, 1, n) {
		tt[0][0] = 0;

		tmp[0] = i;
		use[i] = 1;
		run(i, 1);
		use[i] = 0;
	}

	REP(i, n) {
		printf("%d", postal[ans[i]]);
	}
}

int main() {
	int i, c;

	scanf("%d", &c);
	for(i = 1; i <= c; i++) {
		printf("Case #%d: ", i);
		find_ans();
		printf("\n");
	}

	return 0;
}
