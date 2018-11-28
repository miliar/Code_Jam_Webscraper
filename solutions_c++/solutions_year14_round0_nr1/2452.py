#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <list>
#include <bitset>
using namespace std;

#define INF 987654321
#define LL long long
#define ULL unsigned long long
#define For(i, n) for(int i = 0; i < n; ++i)

int main()
{
#ifdef _CONSOLE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
	{
		int cache[4][4] = { 0 };
		int n; scanf("%d", &n);
		for (int y = 0; y < 4; ++y)
		{
			for (int x = 0; x < 4; ++x)
			{
				scanf("%d", &cache[y][x]);
			}
		}
		vector<int> v;
		for (int x = 0; x < 4; ++x)
		{
			v.push_back(cache[n - 1][x]);
		}//push
		scanf("%d", &n);
		for (int y = 0; y < 4; ++y)
		{
			for (int x = 0; x < 4; ++x)
			{
				scanf("%d", &cache[y][x]);
			}
		}//and push
		int cnt = 0;
		int ans = 0;
		for (int e = 0; e < 4; ++e)
		{
			for (int f = 0; f < v.size(); ++f)
			{
				if (v[f] == cache[n - 1][e])
				{
					ans = v[f];
					cnt++;
				}
			}
		}
		printf("Case #%d: ", i);
		if (cnt == 1)
		{
			printf("%d\n", ans);
		}
		else if (cnt == 0)
		{
			printf("Volunteer cheated!\n");
		}
		else
		{
			printf("Bad magician!\n");
		}
	}
	return 0;
} 