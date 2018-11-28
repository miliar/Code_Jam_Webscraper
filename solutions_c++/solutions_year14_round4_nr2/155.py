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

const int MAXN = 1100;

int T, N, A[MAXN];

int main() {
	scanf("%d", &T);
	REP(t,T) {
		scanf("%d", &N);
		REP(i,N) scanf("%d", A+i);

		int steps = 0;
		int begin = 0;
		int end = N;
		REP(i,N) {
			int min = A[begin];
			int minI = begin;
			FOR(j, begin+1, end-1) {
				if (A[j] < min) {
					min = A[j];
					minI = j;
				}
			}
			int d1 = end-1 - minI;
			int d2 = minI - begin;
			if (d1 < d2) {
				FOR(j, minI, end-2) {
					A[j] = A[j+1];
				}
				steps += d1;
				--end;
			} else {
				FORD(j, minI, begin+1) {
					A[j] = A[j-1];
				}
				steps += d2;
				++begin;
			}
		}
		printf("Case #%d: %d\n", t+1, steps);
	}
	return 0;
}
