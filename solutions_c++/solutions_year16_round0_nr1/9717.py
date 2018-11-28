#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <vector>
#include <iostream>
#include <iomanip>
#include <complex>
#define MP make_pair
#define PUF push_front
#define POF pop_front
#define PUB push_back
#define POB pop_back
#define RESET(i, x) memset(i, x, sizeof(i))
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;

	int arr[15];
	int cases;
	LL cnt, x, n, tmp;

int main() {
	freopen("in.txt", "r+", stdin);
	freopen("out.txt", "w+", stdout);
	scanf("%d", &cases);
	for (int tc = 1; tc <= cases; ++tc) {
		scanf("%lld", &n);
		printf("Case #%d: ", tc);
		if (n == 0) {
			puts("INSOMNIA");
			continue;
		}
		RESET(arr, 0);
		x = n;
		for (int i = 0; i < 150; ++i) {
			tmp = x;
			while (tmp > 0) {
				arr[tmp % 10] = 1;
				tmp /= 10;
			}
			cnt = 0;
			for (int j = 0; j < 10; ++j)
				cnt += arr[j];
			if (cnt == 10)
				break;
			x += n;
		}
		printf("%lld\n", x);
	}
	return 0;
}
/*
4
10 5
10 1
3 2
3 4
*/
