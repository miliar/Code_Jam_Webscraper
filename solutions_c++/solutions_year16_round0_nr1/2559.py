#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <deque>
#include <queue>
using namespace std;
//-----------------------------------------------------------
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const ull inf64 = ((ull) 1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

#define bit(i) ((ull)1 << i)
#define MAXN 3010
//-----------------------------------------------------------
ull N;

int main() {
	int cases;
	int casenum = 1;

	freopen("input.txt", "r", stdin);
	//	freopen("output", "w", stdout);

	scanf("%d", &cases);
	while (cases--) {
		ull mask = 0;
		ull full = 0x3FF;

		scanf("%llu", &N);
		if (N == N * 2) {
			printf("Case #%d: INSOMNIA\n", casenum++);
			continue;
		}
		for(ull i = 1;; ++i) {
			ull n = N * i;
			do {
				ull d = n % 10;
				mask |= bit(d);
				n = n / 10;
			} while (n > 0);
			if (mask == full) {
				printf("Case #%d: %llu\n", casenum++, N * i);
				break;
			}
		}


		//printf("Case #%d: %lf\n", casenum++, ans);
		fflush(stdout);
	}
	return 0;
}
