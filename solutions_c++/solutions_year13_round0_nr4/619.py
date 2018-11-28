#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
using namespace std;

const int maxn = 20;
int key_type[maxn];
multiset<int> chests[maxn];

bool flag[1 << maxn];
multiset<int> keys[1 << maxn];

int choice[1 << maxn];

int main()
{
	int caseN;
	cin >> caseN;
	for (int caseI = 1; caseI <= caseN; caseI++)
	{
		int n, m;
		cin >> m >> n;
		keys[0].clear();
		while (m--)
		{
			int x;
			cin >> x;
			keys[0].insert(x);
		}
		flag[0] = true;
		for (int i = 0; i < n; i++)
		{
			cin >> key_type[i];
			chests[i].clear();
			cin >> m;
			while (m--)
			{
				int x;
				cin >> x;
				chests[i].insert(x);
			}
		}
		
		for (int s = 1; s < (1 << n); s++)
		{
			keys[s] = keys[0];
			for (int i = 0; i < n; i++)
				if (s & (1 << i))
					keys[s].insert(chests[i].begin(), chests[i].end());
			flag[s] = true;
			for (int i = 0; i < n; i++)
				if (s & (1 << i))
				{
					if (!keys[s].count(key_type[i]))
					{
						flag[s] = false;
						break;
					}
					keys[s].erase(keys[s].find(key_type[i]));
				}
		}
		
		if (!flag[(1 << n) - 1])
		{
			cout << "Case #" << caseI << ":";
			cout << " IMPOSSIBLE" << endl;
			continue;
		}
		
		choice[(1 << n) - 1] = n;
		for (int s = (1 << n) - 2; s >= 0; s--)
		{
			choice[s] = -1;
			if (!flag[s])
				continue;
			for (int i = 0; i < n; i++)
				if (!(s & (1 << i)) && keys[s].count(key_type[i]) && choice[s | (1 << i)] != -1)
				{
					choice[s] = i;
					break;
				}
		}
		
		cout << "Case #" << caseI << ":";
		if (choice[0] == -1)
			cout << " IMPOSSIBLE" << endl;
		else
		{
			for (int s = 0; s != (1 << n) - 1; s |= (1 << choice[s]))
			{
				cout << " " << choice[s] + 1;
			}
			cout << endl;
		}
	}
	
	return 0;
}

