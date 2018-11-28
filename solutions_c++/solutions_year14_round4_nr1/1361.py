#pragma	comment(linker, "/STACK:100000000")
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;

typedef long long ll;
#define mod 1000000007
#define pi acos(-1.0)
#define eps 1e-9

int a[10005];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		int n, x;
		scanf("%d %d", &n, &x);
		for(int i = 0; i < n; i++)
			scanf("%d", &a[i]);
		sort(a, a + n);
		int cnt = 0;
		int L = 0, R = n - 1;
		while(L <= R)
		{
			if(a[L] + a[R] <= x)
				L++;
			R--;
			cnt++;
		}
		printf("Case #%d: %d\n", t, cnt);
	}
	return 0;
}