#pragma warning(disable:4996)
#include <stdio.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <tuple>
using namespace std;
typedef long long LL;
typedef function<int(int)> VALF;

#define pb push_back
#define mt make_tuple
#define SZ(V) ((int)((V).size()))

string dyn[13][3];
bool check(string A, int R, int P, int S) {
	for (int i = 0; i < A.size(); i++) {
		switch (A[i]) {
		case 'R':
			R--; break;
		case 'P':
			P--; break;
		case 'S':
			S--; break;
		}
	}
	return R == 0 && P == 0 && S == 0;
}
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, N;
	scanf("%d", &T);

	dyn[0][0] = "R";
	dyn[0][1] = "P";
	dyn[0][2] = "S";
	for (int i = 1; i <= 12; i++) {
		dyn[i][0] = min(dyn[i - 1][0] + dyn[i - 1][2], dyn[i - 1][2] + dyn[i - 1][0]);
		dyn[i][1] = min(dyn[i - 1][1] + dyn[i - 1][0], dyn[i - 1][0] + dyn[i - 1][1]);
		dyn[i][2] = min(dyn[i - 1][1] + dyn[i - 1][2], dyn[i - 1][2] + dyn[i - 1][1]);
	}
	for (int tc = 1; tc <= T; tc++) {
		int R, P, S;
		scanf("%d %d %d %d", &N, &R, &P, &S);
		string sol = "";
		int cnt = 0;
		for (int t = 0; t < 3; t++) {
			if (check(dyn[N][t], R, P, S)) {
				if (cnt == 0) sol = dyn[N][t];
				sol = min(sol, dyn[N][t]);
				cnt++;
			}
		}
		printf("Case #%d: %s\n", tc, cnt==0 ? "IMPOSSIBLE" : sol.c_str());
	}
	return 0;
}