#include <iostream>
#include <vector>
#include <queue>
#include <map>

typedef std::vector<int> V;
typedef std::queue<int> Q;
typedef std::map<int, int> M;

int k, n;
int keys[40];
V chest[20];
int chk[20];
int prev[1 << 21];

int main()
{
	int T;
	std::cin >> T;
	for (int t = 1 ; t <= T ; ++t)
	{
		std::cin >> k >> n;
		for (int i = 0 ; i < k ; ++i)
			std::cin >> keys[i];
		for (int i = 0 ; i < n ; ++i)
		{
			int sz;
			std::cin >> chk[i] >> sz;
			chest[i].resize(sz);
			for (int j = 0 ; j < sz ; ++j)
				std::cin >> chest[i][j];
		}
		for (int i = 0 ; i < 1 << n ; ++i)
			prev[i] = -1;

		Q q;
		q.push(0);
		while (!q.empty())
		{
			int mask = q.front();
			q.pop();
			// count the keys
			M m;
			for (int i = 0 ; i < k ; ++i)
				++m[keys[i]];
			for (int i = 0 ; i < n ; ++i)
				if (mask & (1 << i))
				{
					--m[chk[i]];
					for (int j = 0 ; j < chest[i].size() ; ++j)
						++m[chest[i][j]];
				}
			// find the next
			for (int i = 0 ; i < n ; ++i)
			{
				if (!(mask & (1 << i)) && m[chk[i]])
				{
					int m1 = mask | (1 << i);
					if (prev[m1] < 0)
					{
						prev[m1] = i;
						q.push(m1);
					}
				}
			}
		}

		std::cout << "Case #" << t << ":";
		int mask = (1 << n) - 1;
		if (prev[mask] < 0)
		{
			std::cout << " IMPOSSIBLE";
		}
		else
		{
			V res;
			while (mask != 0)
			{
				res.push_back(prev[mask]);
				mask ^= 1 << prev[mask];
			}
			for (int i = res.size() - 1 ; i >= 0 ; --i)
				std::cout << " " << res[i] + 1;
		}

		std::cout << "\n";
	}
	return 0;
}

