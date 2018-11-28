#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

#define REP(x, n) for(int x = 0; x < (n); ++x)
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define VAR(v, n) __typeof(n) v = (n)
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define SIZE(x) ((int)(x).size())
#define PB push_back
#define PF push_front
#define MP make_pair
#define FI first
#define SE second

const int INF = 1000000001;
const double EPS = 10e-9;


int main() {

	const int TIMES = 2;

	int testCases;
	scanf("%d", &testCases);

	FOR(testCase, 1, testCases) {
		int f[17]; REP(i,17) f[i]=0;

		REP(q,TIMES) {

			int r;
			scanf("%d", &r);

			FOR(i,1,4) {
				FOR(j,1,4) {
					int x;
					scanf("%d", &x);

					if(i==r) f[x]++;
				}
			}

		}

		int results = 0;
		int x = -1;

		REP(i,17) {
			if(f[i] == TIMES) {
				results++;
				x = i;
			}
		}



		printf("Case #%d: ", testCase);

		if(results == 1) {
			printf("%d", x);
		} else {
			printf("%s", (results == 0) ? "Volunteer cheated!" : "Bad magician!");
		}

		printf("\n");
	}

	return 0;
}
