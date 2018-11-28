#include <cstdio>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

int n, x;

int przyp()
{
	scanf("%d%d", &n, &x);
	vector<int> v;
	for(int i = 0; i < n; i++)
	{
		int a;
		scanf("%d", &a);
		v.push_back(a);
	}
	sort(v.begin(), v.end());
	int wyn = 0;
	while(!v.empty())
	{
		int y = v[0];
		v.erase(v.begin());
		wyn++;
		for(int i = v.size() - 1; i >= 0; i--)
		{
			if(y + v[i] <= x)
			{
				v.erase(v.begin() + i);
				break;
			}
		}
	}
	return wyn;
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++)
		printf("Case #%d: %d\n", i, przyp());
	return 0;
}
