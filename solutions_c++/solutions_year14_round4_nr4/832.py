#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;

vector<vector<int>> groups;

int n, m;
vector<string> strs;

int worstCase;
int worstCount;

void go(int i)
{
	if(i == m)
	{
		int total = 0;

		for(int i = 0; i < n; i++)
		{
			set<string> prefixes;

			if(groups[i].size() == 0) return;

			for(int s : groups[i])
			{
				for(int l = 0; l <= strs[s].length(); l++)
				{
					prefixes.insert(strs[s].substr(0, l));
				}
			}

			total += prefixes.size();
		}

		if(total > worstCase)
		{
			worstCase = total;
			worstCount = 1;
		}
		else if(total == worstCase)
		{
			worstCount++;
		}

		return;
	}

	for(int j = 0; j < n; j++)
	{
		groups[j].push_back(i);
		go(i + 1);
		groups[j].pop_back();
	}
}

void solve()
{
	worstCase = 0;
	worstCount = 0;

	cin >> m >> n;

	groups.clear();
	groups.resize(n);

	strs.resize(m);
	for(auto& str : strs)
	{
		cin >> str;
	}

	go(0);

	cout << worstCase << " " << worstCount;
}

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}

	return 0;
}