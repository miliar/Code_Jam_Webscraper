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

const int SIZE = 1<<20;

int n, w;
int arr[SIZE];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d%d", &n, &w);
		for (int i = 0; i<n; i++) scanf("%d", &arr[i]);

		sort(arr, arr+n);
		reverse(arr, arr+n);
		int ans = 0;

		while (n > 0) {
			int mx = 0;
			int best = -1;
			for (int j = 0; j<n; j++) if (arr[0] + arr[j] <= w)
				if (mx < arr[j]) {
					mx = arr[j];
					best = j;
				}

			ans++;
			if (best >= 0) {
				n--;
				for (int j = best; j < n; j++) arr[j] = arr[j+1];
			}
			n--;
			for (int j = 0; j < n; j++) arr[j] = arr[j+1];
		}

		printf("Case #%d: %d\n", tt, ans);
		fflush(stdout);
	}
	return 0;
}
