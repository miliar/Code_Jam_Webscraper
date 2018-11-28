#include <iostream>
#include <fstream>
#include <cstdio>
#include <climits>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <string>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <cmath>

using namespace std;

#define ll long long
#define vt vector
#define inf 1000000000
#define mod 1000000007

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int tests = 1; tests <= t; tests++)
	{
		int k, c, s;
		cin >> k >> c >> s; 
		/*printf("Case #%d: ", tests);
		for (int i = 1; i <= s; i++)
			printf("%d ", i);
		printf("\n");*/
		printf("Case #%d: ", tests);
		if (c == 1)
		{
			if (s == k)
			{
				for (int i = 1; i <= s; i++)
					printf("%d ", i);
				printf("\n");
			}
			else
				printf("IMPOSSIBLE\n");
		}
		else if(s>=(k+1)/2)
		{
			for (int i = 1; i <= (k+1)/2; i++)
			{
				printf("%d ", k*i-(i-1));
			}
			printf("\n");
		}
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}