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

char pattern[MAX];

int n, ans;
int _map[MAX][MAX], p_len;
bool fegla_won;

int _count(int pos, int d) {
	int c = 0;
	REP(i, n) {
		c += abs(_map[i][pos] - d);
	}
	return c;
}

void find_ans() {
	char tmp[MAX];
	int len, pos;
	ans = 0;
	fegla_won = false;
	scanf("%d", &n);
	REP(i, n) {
		scanf("%s", tmp);
		len = strlen(tmp);
		if(i == 0) {
			p_len = 1;
			pattern[0] = tmp[0];
			pattern[1] = 0;
			_map[i][0] = 1;
			FOR(j, 1, len - 1) {
				if(tmp[j - 1] != tmp[j]) {
					pattern[p_len] = tmp[j];
					pattern[p_len + 1] = 0;
					_map[i][p_len] = 1;
					p_len++;
				} else {
					_map[i][p_len - 1]++;
				}
			}
		} else {
			REP(j, p_len)_map[i][j] = 0;
			pos = 0;
			REP(j, len) {
				if(tmp[j] == pattern[pos]) {
					_map[i][pos]++;
				} else {
					pos++;
					if(tmp[j] == pattern[pos]) {
						_map[i][pos]++;
					} else {
						fegla_won = true;
					}
				}
			}
		}
	}

	REP(i, n) {
		REP(j, p_len) {
			if(_map[i][j] == 0) {
				fegla_won = true;
			}
		}
	}

	REP(j, p_len) {
		double sum = 0;
		REP(i, n) {
			sum += _map[i][j];
		}
		int f = floor(sum / n);
		int c_f = _count(j, f);
		int c = ceil(sum / n);
		int c_c = _count(j, c);
		ans += min(c_f, c_c);
	}

//	printf("%s\n", pattern);
//	REP(i, n) {
//		REP(j, p_len) {
//			printf("%3d", _map[i][j]);
//		}
//		printf("\n");
//	}

	if(fegla_won) {
		printf("Fegla Won");
	} else {
		printf("%d", ans);
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
