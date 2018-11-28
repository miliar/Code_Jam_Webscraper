#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
using namespace std;

int oper[1005][1005];
int a[1005];
int n;

void precalc () {
	for (int i = 1; i <= 1000; i++) {
		for (int j = 1; j <= i; j++) {
			oper[i][j] = i / j;
			if (i % j == 0)
				oper[i][j]--;
		}
	}
}

void solve ()
{
	int maxA = 0;
	for (int i = 0; i < n; i++) {
		maxA = max(maxA, a[i] );
	}

	int ans = maxA;

	for (int i = maxA - 1; i >= 1; i--) {
		int curAns = 0;
		for (int j = 0; j < n; j++) {
			curAns += oper[a[j] ][i];
		}
		curAns += i;

		ans = min(ans, curAns);
	}

	printf("%d", ans);
}

int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int test_amount, test_num;

	scanf("%d\n", &test_amount);
	for (test_num = 0; test_num < test_amount; test_num++)
	{
		if (test_num)
			printf("\n");

		printf("Case #%d: ", test_num + 1);

		// precalc

		precalc();

		// input

		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i] );
		}

		// #input

		solve();
	}

	return 0;
}