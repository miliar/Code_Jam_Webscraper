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

double c, f, x;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%lf%lf%lf", &c, &f, &x);

		double ans = 1e+100;

		double sum = 0.0;
		int k;
		for (k = 0; ; k++) {
			double res = sum + x / (2.0 + k*f);
			if (res < ans)
				ans = res;
			else
				break;
			sum += c / (2.0 + k*f);
		}
		Eo(k);

		printf("Case #%d: %0.15lf\n", tt, ans);
		fflush(stdout);
	}
	return 0;
}
