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
#define E(c) cerr<<#c
#define Eo(x) cerr<<#x<<" = "<<(x)<<endl

const int SIZE = 64;

int n;
int64 budget;
int64 arr[SIZE];
int64 tmp[SIZE];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%I64d%d", &budget, &n);
		for (int i = 0; i<n; i++) scanf("%I64d", &arr[i]);
		for (int i = n; i<37; i++) arr[i] = 0;
		n = 37;
		sort(arr, arr+n);

		double ans = 0;

		for (int a = 1; a<=n; a++)
			for (int b = 0; a+b<=n; b++) {
				memcpy(tmp, arr, sizeof(arr));
				int64 rem = budget;
				int64 lvl = max(tmp[a-1], tmp[a+b-1] - 1);

				for (int i = 0; i<a; i++) {
					int64 t = lvl - tmp[i];
					rem -= t;
					tmp[i] += t;
				}

				for (int i = a; i<a+b; i++) {
					int64 t = lvl+1 - tmp[i];
					if (t <= 0) continue;
					rem -= t;
					tmp[i] += t;
				}

				if (rem < 0) continue;

				int64 q = rem / (a+b);
				for (int i = 0; i<a+b; i++) {
					tmp[i] += q;
					rem -= q;
				}

				int64 mint = tmp[0];
				for (int i = 0; i<n; i++) mint = min(mint, tmp[i]);

				double tres = 0;
				int cc = 0;
				for (int i = 0; i<n; i++) if (mint == tmp[i]) {
					tres += 36 * (tmp[i] - arr[i]);
					cc++;
				}
				tres /= cc;
				tres += rem - budget;

				if (ans < tres)
					ans = tres;

			}


		printf("Case #%d: %0.15lf\n", tt, ans);
		fflush(stdout);
	}
	return 0;
}
