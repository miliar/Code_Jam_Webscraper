#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <cstdio>
#include <cstdlib>	
#include <cmath>
#include <cstring>
#include <climits>
using namespace std;

const int mx = 10000+10;
int a[mx];

int main ()
{
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int TC; scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++)
	{
		int n, size; scanf("%d%d", &n, &size);
		for (int i = 0; i < n; i++) scanf("%d", &a[i]);
		sort(a, a+n);
		int cnt = 0;
		for (int i = 0, j = n - 1; i <= j;)
		{
			if (i == j) {cnt++; break;}
			if (a[i]+a[j] <= size) {i++; j--; cnt++;}
			else {cnt++; j--;}
		}
		printf("Case #%d: %d\n", tc, cnt);
	}

}