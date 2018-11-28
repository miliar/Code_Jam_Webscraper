#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <string>

#define pb push_back
#define mp make_pair
#define ll long long
#define FOR(i, A, N) for(int (i) = (A); (i) < (N); (i)++)
#define REP(i, N) for(int (i) = 0; (i) < (N); (i)++)

using namespace std;
int P[1111111];
int mem[1111][1111];
int calc(int X, int lim) {
	if(X <= lim)
		return 0;
	int& ans = mem[X][lim];
	if(ans == -1) {
		for(int i = 1; i <= X/2; i++) {
			int k = calc(i, lim)+calc(X-i, lim)+1;
			if(ans == -1 || k <= ans) {
				ans = k;
			}
		}
	}
	return ans;
}

int main() {
	memset(mem, -1, sizeof(mem));
	int T;
	scanf("%d", &T);
	for(int testc = 1; testc <= T; testc++) {
		int D;
		scanf("%d", &D);
		int most = 0;
		REP(i, D) {
			scanf("%d", P+i);
			most = max(most, P[i]);
		}
		int ans = most;
		for(int normalRounds = 1; normalRounds <= most; normalRounds++) {
			int cans = normalRounds;
			REP(i, D) cans += calc(P[i], normalRounds);
			ans = min(ans, cans);
		}
		printf("Case #%d: %d\n", testc, ans);
	}
	return 0;
}
