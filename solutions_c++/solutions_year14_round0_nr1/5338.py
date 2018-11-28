#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int t = 0; t < tc; t++)
	{
		map <int, int> can;
		int r;
		cin >> r;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				int x;
				cin >> x;
				if (i + 1 == r)
					can[x] = 1;
			}

		cin >> r;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				int x;
				cin >> x;
				if (i + 1 == r)
					can[x]++;
			}
		vector <int> res;
		for (auto it = can.begin(); it != can.end(); it++)
			if (it->second == 2)
				res.push_back(it->first);
		if (res.empty())
		{
			printf("Case #%d: Volunteer cheated!\n", t + 1);
		}
		else if (res.size() == 1)
		{
			printf("Case #%d: %d\n", t + 1, *res.begin());
		}
		else
		{
			printf("Case #%d: Bad magician!\n", t + 1);
		}
	}
}