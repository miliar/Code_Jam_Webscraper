#pragma comment(linker, "/STACK:500000000")
#include <algorithm>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <math.h>
#include <set>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <time.h>
#include <queue>
#include <utility>
#include <vector>
using namespace std;

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define y0 y123
#define y1 y1234
#define ll long long
#define PI 3.1415926535897932384626433832795
#define EPS 1e-9
#define INF 2147483647
#define MOD 1000000007
#define N 105
#define M 1305

int gcd(int a, int b) { return (!b) ? a : gcd(b, a % b); }
int lcm(int a, int b) { return a / gcd(a,b) * b; }

int a[N][N], t, n, m;
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &t);
	for(int tt = 1; tt <= t; tt++)
	{
		scanf("%d %d", &n, &m);
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				scanf("%d", &a[i][j]);
		printf("Case #%d: ", tt);
		bool res = 1;
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
			{
				bool ok1 = 1, ok2 = 1;
				for(int k = 0; k < m; k++)
					if(a[i][k] > a[i][j])
					{
						ok1 = 0;  break;
					}
				for(int k = 0; k < n; k++)
					if(a[k][j] > a[i][j])
					{
						ok2 = 0;  break;
					}
				if(!ok1 && !ok2)
				{
					res = 0; i = n; break;
				}
			}
		if(res)
			puts("YES");
		else
			puts("NO");
	}
	return 0;
}