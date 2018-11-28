#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <memory.h>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>

using namespace std;

int main(void)
{
	freopen("input.txt","r", stdin);
	freopen("output.txt","w",stdout);
	
	int t;
	scanf("%d", &t);
	for (int q = 1; q <= t; q++)
	{
		int a, b, k;
		int cnt = 0;
		scanf("%d%d%d", &a, &b, &k);
		for (int i = 0; i < a; i++)
			for (int j = 0; j < b; j++)
			{
				int tmp = i & j;
				if (tmp < k)
					cnt++;
			}
		printf("Case #%d: %d\n", q, cnt);
	}
	return 0;
}