#include <cstdio>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <memory.h>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <functional>
#include <ctime>

#define FOR(i, n) for (int i = 0; i < n; i++)

#pragma comment(linker, "/STACK:250777216")

using namespace std;

typedef long long LL;
typedef vector<int> vint;
typedef vector<vint> vvint;
const int MOD = int(1e9) + 7;
const int HMOD = (1 << 22) - 1;
const int BASE = int(1e9);

int t;
int n, m;
int a[110][110] = {};

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &t);
	for (int k = 0; k < t; k++)
	{
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				scanf("%d", &a[i][j]);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
			{
				bool flag1 = true, flag2 = true;
				for (int q = 0; q < m; q++)
					if (a[i][q] > a[i][j])
						flag1 = false;
				for (int q = 0; q < n; q++)
					if (a[q][j] > a[i][j])
						flag2 = false;
				if (!flag1 && !flag2)
				{
					printf("Case #%d: NO\n", k + 1);
					goto label1;
				}
			}
		printf("Case #%d: YES\n", k + 1);
		label1:;
	}
	return 0;
}