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


bool can[32];
int matr[8][8];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		for (int i = 1; i<=16; i++)
			can[i] = true;

		for (int q = 0; q<2; q++) {
			int r;
			scanf("%d", &r);

			for (int i = 1; i<=4; i++)
				for (int j = 1; j<=4; j++) {
					scanf("%d", &matr[i][j]);
					if (i != r)
						can[matr[i][j]] = false;
				}
		}

		int some = -1;
		int cc = 0;
		for (int i = 1; i<=16; i++) if (can[i]) {
			some = i;
			cc++;
		}

		printf("Case #%d: ", tt);
		if (cc == 0) printf("Volunteer cheated!\n");
		else if (cc > 1) printf("Bad magician!\n");
		else printf("%d\n", some);
		fflush(stdout);
	}
	return 0;
}
