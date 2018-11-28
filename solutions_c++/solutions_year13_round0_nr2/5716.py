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
#include <queue>
#include <utility>
#include <vector>
using namespace std;

#define EPS 1e-9
#define ll long long
#define N 1048581


int  n,m,a[105][105], i, j, k, open,t, x, y, xx, yy, ok, b[105][105], st[105], sl[105];
char s[10][10];
int gcd(int a, int b){while(b) b^=a^=b^=a%=b;return a;}
int main()
{
	freopen("B-large.in.txt", "rt", stdin);
    freopen("B-small-attempt4.out.txt", "wt", stdout);
	scanf("%d", &t);
	n = 4;
	for(int g = 1;g<=t;g++)
	{
		
		scanf("%d %d", &n, &m);
		ok = 1;
		for(i = 0;i<=max(n,m);i++)
			st[i] = sl[i] = 0;
		for(i = 1;i<=n;i++)
			for(j = 1;j<=m;j++)
				scanf("%d", &a[i][j]), b[i][j] = 0, st[i] = max(st[i], a[i][j]), sl[j] = max(sl[j], a[i][j]);
		
		for(i = 1;i<=n;i++)
		{ 
			for(j = 1;j<=m;j++)
				if(a[i][j]<st[i])
					b[i][j]=1;
		}
		for(i = 1;i<=m;i++)
			for(j = 1;j<=n;j++)
				if(b[j][i] && a[j][i]<sl[i])
				{
					printf("Case #%d: NO\n", g);
					i = m;
					ok = 0;
					break;
				}
		
		if(ok)
			printf("Case #%d: YES\n", g);
	}
	return 0;
}
