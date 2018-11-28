#pragma comment(linker, "/STACK:64000000")
#include <algorithm>
#include <memory.h>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <cassert>
#include <map>
#include <set>
#include <vector>
#include <queue>

using namespace std;
#define prev privet1
#define next privet2
#define y1 privet3
#define rank privet4
#define left privet5
#define right privet6
#define y0 privet7

const double pi = 3.141592653589793238;

void ensureLimit(long long n, long long l, long long r)
{
	assert(l <= n && n <= r);
}

double a[1111], b[1111];

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	scanf("%d", &tc);
	for (int cases = 1; cases <= tc; cases++) {
		printf("Case #%d: ", cases);
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%lf", &a[i]);
		for (int i = 0; i < n; i++) 
			scanf("%lf", &b[i]);
		int ans2 = 0;
		sort(b, b + n);
		bool used[1111] = {};
		for (int i = 0; i < n; i++) {
			int mn = -1;
			for (int j = 0; j < n; j++)
				if (!used[j] && b[j] > a[i]) {
					mn = j;
					break;
				}
			if (mn == -1) {
				for (int j = 0; j < n; j++)
					if (!used[j]) {
						used[j] = true;
						break;
					}
				ans2++;
				continue;
			}
			used[mn] = true;
		}
		int ans1 = 0;
		sort(a, a + n);
		memset(used, false, sizeof(used));
		for (int i = 0; i < n; i++) {
			int mn = -1, mx = -1;
			for (int j = 0; j < n; j++) 
				if (!used[j]) {
					if (mn == -1) mn = j;
					mx = j;
				}
			if (a[i] > b[mn]) {
				used[mn] = true;
				ans1++;
				continue;
			}
			used[mx] = true;
		}
		printf("%d %d\n", ans1, ans2);
	}
}
