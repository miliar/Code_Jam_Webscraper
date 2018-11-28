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

int N;
double nb[MAX], kb[MAX];

void read_input() {
	scanf("%d", &N);
	REP(i, N) {
		scanf("%lf", &nb[i]);
	}
	REP(i, N) {
		scanf("%lf", &kb[i]);
	}
}

void find_ans() {
	read_input();

	int dwa = 0, wa = 0;

	sort(nb, nb + N);
	sort(kb, kb + N);

	int klb = 0, kub = N - 1;
	REP(i, N) {
		if(nb[i] < kb[klb]) {
			kub--;
		} else {
			klb++;
			dwa++;
		}
	}

	klb = 0;
	REP(i, N) {
		while(klb < N && nb[i] > kb[klb]) {
			wa++;
			klb++;
		}
		if(klb < N) {
			klb++;
		}
	}

	printf("%d %d", dwa, wa);
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
