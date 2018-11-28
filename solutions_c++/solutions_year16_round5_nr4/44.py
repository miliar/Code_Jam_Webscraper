#pragma warning(disable:4996)

#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <complex>
#include <iterator>
#include <random>
#include <time.h>
#include <tuple>
#include <functional>
#include <list>
#include <limits.h>
#define mp make_pair
#define ni(x) scanf("%d", &(x))
#define nii(x,y) scanf("%d%d",&(x),&(y))
#define mul(x,y) ((ll)(x)*(y)%mod)
#define mtp make_tuple
#define add(x,y) ((ll)(x)+(y))%mod
#define F(i,n) for(int i = 0; i < n; i++)
#define FF(i,n) for(int i = 1; i <= n; i++)

using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
const int mod = 1000000007;
const int inf = 2012345678;
const double pi = 3.1415926535897932384626433832795;
//----------------------------------------------------------------------------//

char buf[100];

int main() {
#ifndef __GNUG__
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	srand((unsigned int)time(0));
	int T; ni(T);
	FF(tt, T) {
		printf("Case #%d: ", tt);
		//------------------------------------------//
		int N, L; nii(N, L);
		bool bad = false;
		F(i, N) {
			scanf("%s", buf);
			bool good = false;
			F(i, L) {
				if (buf[i] == '0') {
					good = true;
					break;
				}
			}
			if (!good) {
				bad = true;
			}
		}
		scanf("%s", buf);
		if (bad) {
			puts("IMPOSSIBLE");
			continue;
		}

		if (L == 1) {
			puts("? 0");
			continue;
		}
		F(i, L - 1) printf("%c",'?');
		printf(" ");
		printf("10?");
		F(i, 49) printf("10");
		puts("");

		//------------------------------------------------------------------//
		fprintf(stderr, "Case %d complete\n", tt);
	}
	return 0;
}
