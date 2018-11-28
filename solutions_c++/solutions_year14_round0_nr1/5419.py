#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;
const int n = 4;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int z = 1; z <= T; ++z)
	{
		int a;
		scanf("%d", &a);
		set <int> first;
		int x;
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < n; ++j)
			{
				scanf("%d", &x);
				if (i + 1 == a)
					first.insert(x);
			}
		}
		scanf("%d", &a);
		set <int> second;
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < n; ++j)
			{
				scanf("%d", &x);
				if (i + 1 == a)
					second.insert(x);
			}
		}
		set <int> res;
		set_intersection(first.begin(), first.end(), second.begin(), second.end(), inserter(res, res.begin()));
		if (res.size() > 1)
			printf("Case #%d: Bad magician!\n", z);
		else if (res.size() == 0)
			printf("Case #%d: Volunteer cheated!\n", z);
		else
			printf("Case #%d: %d\n", z, *(res.begin()));
	}
	return 0;
}
