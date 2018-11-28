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

const int SIZE = 1024;

int n;
int arr[SIZE];
int pos[SIZE];
int res[SIZE][SIZE];

void relax(int &a, int b) {
	if (a > b) a = b;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d", &n);
		for (int i = 0; i<n; i++) scanf("%d", &arr[i]);

		for (int i = 0; i<n; i++) pos[i] = i;
		sort(pos, pos+n, [](int a, int b) -> bool { return arr[a] < arr[b]; });

		memset(res, 63, sizeof(res));
		res[0][0] = 0;
		for (int a = 0; a<n; a++)
			for (int b = 0; a+b<n; b++) {
				int tres = res[a][b];
				if (tres > 1000000000) continue;

				int pp = pos[a+b];
				int curr = arr[pp];

				int left = 0, right = 0;
				for (int u = 0; u<n; u++)
					if (arr[u] > curr)
						(u < pp ? left : right)++;
	
				relax(res[a+1][b], tres + left);
				relax(res[a][b+1], tres + right);
			}

		int ans = 1000000000;
		for (int a = 0; a<=n; a++) {
			int b = n-a;
			relax(ans, res[a][b]);
		}

		printf("Case #%d: %d\n", tt, ans);
		fflush(stdout);
	}
	return 0;
}
