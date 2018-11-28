#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cassert>

#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <bitset>

using namespace std;

typedef long long ll;
typedef long long li;
typedef unsigned int uint;
typedef unsigned long long ull;

#define TASKNAME "delete"

void Solution();

int main()
{
#ifdef DEBUG
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#else
#endif
	Solution();
	return 0;
}

int used[20];

void Solution()
{
	int tests; scanf("%d", &tests);
	for (int test = 1; test <= tests; test++)
	{
		fill(used, used + 16, 0);
		int x; scanf("%d", &x);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				int y; scanf("%d", &y); y--;
				if (i == x - 1) used[y]++;
			}
		scanf("%d", &x);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				int y; scanf("%d", &y); y--;
				if (i == x - 1) used[y]++;
			}
		int best = -1;
		for (int i = 0; i < 16; i++)
			if (used[i] == 2)
				best = (best == -1 ? i : -2);
		printf("Case #%d: ", test);
		if (best == -2) printf("Bad magician!\n");
		else if (best == -1) printf("Volunteer cheated!\n");
		else printf("%d\n", best + 1);
	}
}