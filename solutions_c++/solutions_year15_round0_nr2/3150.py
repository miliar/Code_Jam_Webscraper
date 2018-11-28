#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);

	for (int i = 0; i < t; i++)
	{
		int n;
		scanf("%d", &n);
		vector<int> v;
		for (int i = 0; i < n; i++)
		{
			int x;
			scanf("%d", &x);
			v.push_back(x);
		}

		sort(v.begin(), v.end());

		int ans = v.back();

		for (int i = 1; i <= 1000; i++)
		{
			int curRes = i;
			for (auto a : v)
			{
				curRes += (a + i - 1) / i - 1;	
			}	
			ans = min(ans, curRes);
		}

		printf("Case #%d: %d\n", i + 1, ans);
	}
}
