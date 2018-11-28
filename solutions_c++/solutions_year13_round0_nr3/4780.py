#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;
#define MAXN 100 + 5
#define MAXV 10000000 + 5
#define INF 1e9
#define eps 1e-9
int n, m;
int cnt;
int a, b;
int isParli(int a)
{
	if(a / 10 == 0)
		return a;
	int temp[20];
	int k = 0;
	int res = 0;
	while(a != 0)
	{
		temp[++k] = a % 10;
		a = a / 10;
	}
	for(int i = 1; i <= k; i++)  
	{  
		res *= 10;  
		res += temp[i];
	}
	return res;
}
int isSqare(int n)
{
	double m = sqrt((double)n);
	if(floor(m + 0.5) == m)
	{
		if(isParli((int)m) == (int)m)
			return 1;
	}
	return 0;
}
int main()
{
#ifdef LOCAL
	freopen("data.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	getchar();
	for(int ncas = 1; ncas <= T; ncas++)
	{
		cnt = 0;
		scanf("%d%d", &a, &b);
		printf("Case #%d: ", ncas);
		for(int i = a; i <= b; i++)
		{
			if(isSqare(i))
			{
				if(isParli(i) == i)
				{
					cnt++;
				}
			}
		}
		printf("%d\n", cnt);
	}
	return 0;
}