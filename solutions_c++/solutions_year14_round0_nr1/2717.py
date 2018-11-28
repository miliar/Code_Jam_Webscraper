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


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	scanf("%d", &tc);
	for (int cases = 1; cases <= tc; cases++) {
		printf("Case #%d: ", cases);
		int x;
		scanf("%d", &x);
		int a[5][5], b[17] = {};
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++) {
				scanf("%d", &a[i][j]);
				if (i + 1 == x) b[a[i][j]]++;
			}
		scanf("%d", &x);
		int cnt = 0, ans = 0;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++) {
				scanf("%d", &a[i][j]);
				if (i + 1 == x) b[a[i][j]]++;
				if (b[a[i][j]] == 2) cnt++, ans = a[i][j];
			}
		if (cnt == 0) printf("Volunteer cheated!\n");
		else if (cnt == 1) printf("%d\n", ans);
		else printf("Bad magician!\n");
	}
}
