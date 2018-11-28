
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <unordered_map>
#include <unordered_set>
#include <memory>
using namespace std;


int s[10007];

int main()
{
	int test_cases;
	scanf("%d", &test_cases);

	for (int test_case = 1; test_case <= test_cases; test_case++)
	{
		int n, x;
		scanf("%d %d", &n, &x);
		for (int i = 0; i < n; i++)
		{
			scanf("%d", s+i);
		}
		sort(s,s+n);

		int l = 0, r = n-1;
		int ans = 0;
		while (l<=r)
		{
			if (l==r)
			{
				r--;
			}
			else
			{
				if (s[l]+s[r]<=x)
				{
					l++;
					r--;
				}
				else
				{
					r--;
				}
			}
			ans++;
		}

		printf("Case #%d: %d\n", test_case, ans);
	}

	return 0;
}