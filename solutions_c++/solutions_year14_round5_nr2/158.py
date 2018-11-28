#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;
#define DEBUG(x) cerr << '>' << #x << ':' << x << endl;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0; i<(a);++i)
inline bool EQ(double a, double b) {return fabs(a-b) < 1e-9;}

const int INF = 1<<29;
typedef long long ll;

const int MAXN = 120;
const int MAXMOVES = 1100;

int T, N, P, Q;
int H[MAXN], G[MAXN];

int maxScore[MAXN][MAXMOVES];

int roundUp(int a, int b) {
	return (a+b-1) / b;
}

int main() {
	scanf("%d", &T);
	REP(t,T) {
		scanf("%d%d%d", &P, &Q, &N);
		REP(i,N) scanf("%d%d", H+i, G+i);

		REP(i,MAXMOVES) maxScore[0][i] = -1;
		maxScore[0][1] = 0;


		REP(i,N) {
			int towerHitsIdle = roundUp(H[i], Q);
			int rem = (H[i]-1) % Q + 1;
			int dianaHitsGet = roundUp(rem, P);
			int towerHitsGet = roundUp(H[i] - rem, Q);

			REP(j,MAXMOVES) {
				maxScore[i+1][j] = -1;
			}
			REP(j,MAXMOVES) {
				if (maxScore[i][j] != -1) {
					maxScore[i+1][j+towerHitsIdle] = maxScore[i][j];
				}
			}
			REP(j,MAXMOVES) {
				if (maxScore[i][j] != -1) {
					int moves = j + towerHitsGet - dianaHitsGet;
					if (moves < 0) continue;
					maxScore[i+1][moves] =
						max(maxScore[i+1][moves], maxScore[i][j] + G[i]);
				}
			}
		}

		int best = 0;
		REP(i,MAXMOVES) {
			best = max(maxScore[N][i], best);
		}

		printf("Case #%d: %d\n", t+1, best);
	}
	return 0;
}
