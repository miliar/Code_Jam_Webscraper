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

int a[MAX];

void find_ans() {
	int r, t, c = 0, ans;

	FOR(i, 1, 16)a[i] = 0;

	scanf("%d", &r);
	FOR(i, 1, 4) {
		FOR(j, 1, 4) {
			scanf("%d", &t);
			if(i == r) {
				a[t]++;
			}
		}
	}

	scanf("%d", &r);
	FOR(i, 1, 4) {
		FOR(j, 1, 4) {
			scanf("%d", &t);
			if(i == r) {
				if(a[t] > 0) {
					ans = t;
					c++;
				}
			}
		}
	}

	if(c == 1) {
		printf("%d", ans);
	} else if(c == 0) {
		printf("Volunteer cheated!");
	} else {
		printf("Bad magician!");
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
