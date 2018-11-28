#pragma comment(linker, "/STACK:100000000")
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
#define eps 1e-7

double a[1005], b[1005];
int used[1005];

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		int n;
		scanf("%d", &n);
		for(int i = 0; i < n; i++)
			scanf("%lf", &a[i]);
		for(int i = 0; i < n; i++)
			scanf("%lf", &b[i]);
		sort(a, a + n);
		sort(b, b + n);
		int la = 0, ra = n - 1;
		int lb = 0, rb = n - 1;
		int res1;
		while(true)
		{
			bool ok = true;
			for(int i = la, j = lb; i <= ra, j <= rb; i++, j++)
				if(!(a[i] - b[j] > eps))
					ok = false;
			if(ok)
			{
				res1 = ra - la + 1;
				break;
			}
			else
			{
				la++;
				rb--;
			}
		}

		memset(used, 0, sizeof(used));
		int res2 = 0;
		for(int i = 0; i < n; i++)
		{
			bool naomi = true;
			for(int j = 0; j < n; j++)
				if(b[j] - a[i] > eps && !used[j])
				{
					used[j] = 1;
					naomi = false;
					break;
				}
			if(naomi)
			{
				res2++;
				for(int j = 0; j < n; j++)
					if(used[j] == 0)
					{
						used[j] = 1;
						break;
					}
			}
		}
		printf("Case #%d: %d %d\n", t, res1, res2);
	}
	return 0;
}
