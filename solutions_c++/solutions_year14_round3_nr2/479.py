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

int n;
char str[MAX][MAX];
int ans, use[MAX], tmp[MAX];

void read_input() {
	scanf("%d", &n);
	REP(i, n) {
		scanf("%s", str[i]);
	}
}

void run(int index) {
	if(index == n) {
		char last = 0;
		int _map[26];
		REP(i, 26)_map[i] = 0;
		REP(i, n) {
			for(int j = 0; str[tmp[i]][j] != 0; j++) {
				if(str[tmp[i]][j] == last)continue;
				last = str[tmp[i]][j];
				if(_map[last - 'a'] == 1)return;
				_map[last - 'a'] = 1;
			}
		}
		ans++;
		return;
	}

	REP(i, n) {
		if(use[i])continue;

		use[i] = 1;
		tmp[index] = i;
		run(index + 1);
		use[i] = 0;
	}
}

void find_ans() {
	read_input();

	ans = 0;
	run(0);
	printf("%d", ans);
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
