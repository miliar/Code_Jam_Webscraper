#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <memory.h> 
#include <math.h> 
#include <assert.h> 
#include <stack> 
#include <queue> 
#include <map> 
#include <set> 
#include <algorithm> 
#include <string> 
#include <functional> 
#include <vector> 
#include <deque> 
#include <utility> 
#include <bitset> 
#include <limits.h>  
#include <unordered_map>

using namespace std;
typedef long long ll;
typedef unsigned long long llu;
typedef double lf;
typedef unsigned int uint;
typedef long double llf;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;

int TC, TCC;

int R, C;
const int SZ = 150;
char S[SZ][SZ];
bool V[SZ][SZ];
char op[200];

void precalc() {
	op['<'] = '>';
	op['>'] = '<';
	op['^'] = 'v';
	op['v'] = '^';
}

void init() {
	for (int i = 0; i < R; i++) for (int j = 0; j < C; j++) V[i][j] = false;
}

void solve() {
	scanf("%d%d", &R, &C);
	for (int i = 0; i < R; i++) scanf("%s", S[i]);

	int ans = 0;
	bool good = true;
	for (int i = 0; i < R && good; i++) {
		for (int j = 0; j < C && good; j++) if(S[i][j] != '.') {
			int x = i, y = j; bool chk = false;
			while (x >= 0 && x < R && y >= 0 && y < C) {
				if (S[i][j] == '<') --y; else if (S[i][j] == '>') ++y;
				else if (S[i][j] == '^') --x; else if (S[i][j] == 'v') ++x;
				if ((x >= 0 && x < R && y >= 0 && y < C)  && S[x][y] != '.') { chk = true; break; }
			}
			if (!chk) {
				int t = 0; char d = S[i][j]; S[i][j] = '.';
				for (int k = 0; k < C; k++) if (S[i][k] != '.') t = 1;
				for (int k = 0; k < R; k++) if (S[k][j] != '.') t = 1;
				S[i][j] = d;
				if (t == 0) good = false;
				else ++ans;
			}
		}
	}

	if (good)
		printf("Case #%d: %d\n", TCC, ans);
	else
		printf("Case #%d: IMPOSSIBLE\n", TCC);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	fprintf(stderr, "precalc start\n");
	precalc();
	fprintf(stderr, "precalc finished\n");

	scanf("%d", &TC);
	while (++TCC <= TC) {
		fprintf(stderr, "Case #%d: \n", TCC);
		fprintf(stderr, " - Init Start\n", TCC);
		init();
		fprintf(stderr, " - Init End\n", TCC);
		fprintf(stderr, " - Call Solve()\n", TCC);
		solve();
		fprintf(stderr, " - Printed!\n", TCC);
	}
	return 0;
}