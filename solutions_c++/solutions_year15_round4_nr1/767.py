//*
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <functional>
#include <map>
#include <set>
#include <time.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#pragma warning(disable:4996)
using namespace std;

typedef long long ll;
typedef double db;
typedef long double ldb;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef pair <char, char> pcc;
typedef pair <int, char> pic;
typedef pair <int, ll> pil;
typedef pair <ll, int> pli;

const int IT_MAX = 32768;
const int MOD = 1000000007;
const int INF = 2034567891;
const ll LL_INF = 1234567890123456789ll;

char in[105][105];
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		int R, C, i, j, k;
		scanf("%d %d", &R, &C);
		for (i = 0; i < R; i++) scanf("%s", in[i]);

		int ANS = 0;
		for (i = 0; i < R; i++) {
			for (j = 0; j < C; j++) {
				if (in[i][j] == '.') continue;
				bool c1 = false, c2 = false, c3 = false, c4 = false;
				for (k = i - 1; k >= 0; k--) if (in[k][j] != '.') break;
				if (k >= 0) c1 = true;
				for (k = i + 1; k < R; k++) if (in[k][j] != '.') break;
				if (k < R) c3 = true;
				for (k = j - 1; k >= 0; k--) if (in[i][k] != '.') break;
				if (k >= 0) c2 = true;
				for (k = j + 1; k < C; k++) if (in[i][k] != '.') break;
				if (k < C) c4 = true;

				if ((!c1)&(!c2)&(!c3)&(!c4)) break;
				if (in[i][j] == '^' && !c1) ANS++;
				if (in[i][j] == '<' && !c2) ANS++;
				if (in[i][j] == 'v' && !c3) ANS++;
				if (in[i][j] == '>' && !c4) ANS++;
			}
			if (j < C) break;
		}

		printf("Case #%d: ", tc);
		if (i < R) printf("IMPOSSIBLE\n");
		else printf("%d\n", ANS);

		// Initialize
		for (i = 0; i < R; i++) for (j = 0; j < C; j++) in[i][j] = 0;
	}
	return 0;
}
//*/

