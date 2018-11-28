#include <cstdio>
#include <queue>
#include <unordered_set>
using namespace std;

int flip(int x)
{
	int y = 0;
	while (x > 0)
	{
		y *= 10;
		y += x % 10;
		x /= 10;
	}
	return y;
}

int doit()
{
	int n;
	scanf("%d", &n);
	std::unordered_set<int> visited;
	std::vector<int> cur;
	std::vector<int> next;
	cur.push_back(1);
	visited.insert(1);
	for (int cost = 1; ; ++cost)
	{
		for (size_t i = 0; i < cur.size(); ++i)
		{
			int x = cur[i];
			if (x == n)
				return cost;
			if (visited.insert(x+1).second)
				next.push_back(x+1);
			int f = flip(x);
			if (visited.insert(f).second)
				next.push_back(f);
		}
		cur.clear();
		std::swap(cur, next);
	}
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
	{
		int ret = doit();
		printf("Case #%d: %d\n", i+1, ret);
	}
	return 0;
}
