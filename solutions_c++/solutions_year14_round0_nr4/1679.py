#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;

int n, cnt1, cnt2;
double a[1111];
double b[1111];

bool cmp(const int &a, const int &b)
{
	return a > b;
}

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%lf", &a[i]);
		for (int i = 0; i < n; ++i)
			scanf("%lf", &b[i]);
		sort(a, a + n);
		sort(b, b + n);

		cnt1 = cnt2 = 0;

		int j = n - 1;
		for (int i = n - 1; i >= 0; --i) {
			while (j >= 0 && a[i] < b[j]) j--;
			if (j >= 0) {
				cnt1++;
				j--;
			}
		}

		j = 0;
		for (int i = 0; i < n; ++i) {
			while (j < n && a[i]>b[j]) j++;
			if (j >= n)  cnt2++;
			else j++;
		}
		printf("Case #%d: %d %d\n", cas, cnt1, cnt2);
	}
	return 0;
}

