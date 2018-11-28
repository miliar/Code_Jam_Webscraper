#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;

int n;
vector<int> arr;

int main()
{
	int i, j, x, ret;
	int mv, mp;
	int t, cas;
	scanf("%d", &t);
	for (cas = 1; cas <= t; cas++)
	{
		arr.clear();
		scanf("%d", &n);
		for (i = 0; i < n; i++)
		{
			scanf("%d", &x);
			arr.push_back(x);
		}
		ret = 0;
		while (!arr.empty())
		{
			int len = arr.size();
			for (i = 0, mv = 2111222333, mp = -1; i < len; i++)
				if (arr[i] < mv) 
					{ mv = arr[i]; mp = i; }
			ret += min(mp, len - mp - 1);
			arr.erase(arr.begin() + mp);
		}
		printf("Case #%d: %d\n", cas, ret);
	}
	return 0;
}
