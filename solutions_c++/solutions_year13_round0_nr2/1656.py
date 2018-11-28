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

int n, m, _map[MAX][MAX];

void reset() {

}

void read_input() {
	scanf("%d %d", &n, &m);
	REP(i, n) {
		REP(j, m) {
			scanf("%d", &_map[i][j]);
		}
	}
}

bool find_ans() {
	read_input();

	bool pass;
	REP(i, n) {
		REP(j, m) {
			pass = true;
			REP(ii, n) {
				if(_map[ii][j] > _map[i][j]) {
					pass = false;
					break;
				}
			}
			if(pass)continue;

			pass = true;
			REP(jj, m) {
				if(_map[i][jj] > _map[i][j]) {
					pass = false;
					break;
				}
			}
			if(pass)continue;

			return false;
		}
	}

	return true;
}

int main() {
	int i, c;

	scanf("%d", &c);
	for(i = 1; i <= c; i++) {
		printf("Case #%d: ", i);
		if(find_ans()) {
			printf("YES");
		} else {
			printf("NO");
		}
		printf("\n");
	}

	return 0;
}
