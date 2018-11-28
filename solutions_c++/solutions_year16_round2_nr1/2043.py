#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <string>
#include <cassert>
#include <cmath>
#include <cstring>
#include <functional>
#include <iostream>
using namespace std;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef long long ll;
#define REP(i,a,n) for (int i = (a); i < (n); i++)

int N;
char s[2001];
int c[30];
int d[11];

void docase() {
	scanf("%s", s);
	REP(i, 0, 30) {
		c[i] = 0;
	}

	REP(i, 0, strlen(s)) {
		char _c = s[i];
		c[_c-'A']++;
	}
	
	d[0] = c['Z'-'A'];		
	d[2] = c['W'-'A'];
	d[4] = c['U'-'A'];
	d[3] = c['R'-'A'] - d[0] - d[4];
	d[5] = c['F'-'A'] - d[4];
	d[7] = c['V'-'A'] - d[5];
	d[6] = c['X'-'A'];
	d[8] = c['G'-'A'];
	d[1] = c['O'-'A'] - d[0] - d[2] - d[4];
	d[9] = c['I'-'A'] - d[6] -d[8] - d[5];

	REP(i, 0, 10) {
		REP(j, 0, d[i]) {
			printf("%d", i);
		}
	}
	printf("\n");
}

int main() {
	int T;
	scanf("%d ", &T);
	for (int test = 0; test < T; test++) {
		printf("Case #%d: ", test+1);
		docase();
	}
	return 0;
}
