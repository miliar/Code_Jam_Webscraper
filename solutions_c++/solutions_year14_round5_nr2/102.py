#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#ifdef HOME
	#define E(c) cerr<<#c
	#define Eo(x) cerr<<#x<<" = "<<(x)<<endl
	#define Ef(...) fprintf(stderr, __VA_ARGS__)
#else
	#define E(c) ((void)0)
	#define Eo(x) ((void)0)
	#define Ef(...) ((void)0)
#endif

const int SIZE = 128;
const int MAXB = 40<<10;
const int HALF = MAXB/2;

int divup(int a, int b) {
	if (a < 0)
		return a / b;
	else
		return (a + (b-1)) / b;
}

int n;
int p, q;
int cost[SIZE];
int hp[SIZE];

int res[SIZE][2][MAXB];

void relax(int &a, int b) {
	if (a < b) a = b;
}

int mymod(int a, int b) {
	if (a % b == 0)
		return b;
	return a % b;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
	    scanf("%d%d%d", &p, &q, &n);
		for (int i = 0; i<n; i++) scanf("%d%d", &hp[i], &cost[i]);


		memset(res, -1, sizeof(res));
		res[0][0][HALF + 0] = 0;
		for (int i = 0; i<=n; i++)
			for (int t = 0; t < 2; t++)
				for (int b = -HALF; b < HALF; b++) {
					int tres = res[i][t][HALF + b];
					if (tres < 0) continue;
//					Ef("%d %d %d -> %d\n", i, t, b, tres);
					assert(b >= 0);
					if (i == n) continue;

					{
						int currhp = hp[i];
						if (t) currhp -= q;
						int towertime = divup(currhp, q);
/*						Eo(i+1);
						Eo(b + towertime);*/
						relax(res[i+1][0][HALF + b + towertime], tres);
					}

					int currhp = hp[i];
					{
						int blows = divup(currhp, p);
						if (b >= blows)
							relax(res[i+1][t][HALF + b - blows], tres + cost[i]);
					}

					if (t) currhp -= q;
					if (currhp <= 0) continue;

					int bal = b;
/*					if (bal < 0) {
						currhp -= (-bal) * q;
						bal = 0;
					}
					if (currhp <= 0) continue;*/

					if (p >= q) {
						while (currhp > q) {
							currhp -= q;
							bal++;
						}
						relax(res[i+1][1][HALF + bal], tres + cost[i]);
					}
					else {
						bool ok = true;
						while (mymod(currhp, q) > p) {
//							Ef("%d %d\n", currhp, bal);
							if (bal > 0) {
								bal--;
								currhp -= p;
							}
							else {
								currhp -= p;
								currhp -= q;
							}
							if (currhp <= 0)
								ok = false;
						}
						if (!ok) continue;

						while (currhp > p) {
							currhp -= q;
							bal++;
						}
						relax(res[i+1][1][HALF + bal], tres + cost[i]);
	                }
				}

		int ans = 0;
		for (int t = 0; t < 2; t++)
			for (int b = -HALF; b < HALF; b++) {
				int tres = res[n][t][HALF + b];
				relax(ans, tres);
			}
		
		printf("Case #%d: %d\n", tt, ans);
		fflush(stdout);
	}
	return 0;
}
