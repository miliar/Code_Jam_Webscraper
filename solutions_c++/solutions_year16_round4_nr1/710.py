#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <stdio.h>
#include <string>
#include <map>
#include <algorithm>
#include <set>

using namespace std;

int main()
{
	cin.sync_with_stdio(0);
	freopen( "..\\input.txt", "r", stdin );
	freopen( "..\\output.txt", "w", stdout );

	int t;
	cin >> t;
	for( int tt = 1; tt <= t; tt++ )
	{
		int n, r, p, s;
		cin >> n >> r >> p >> s;

		bool hasAns = false;
		string bestAns;
		vector<char> ans;
		vector<char> letters = { 'R', 'P', 'S' };
		for (int st = 0; st < 3; st++)
		{
			string ans = "";
			ans += letters[st];
			for (int i = 0; i < n; i++)
			{
				string newAns = "";
				for (int j = 0; j < ans.length(); j++)
				{
					if (ans[j] == 'R')
					{
						newAns = newAns + "R" + "S";
					}
					if (ans[j] == 'P')
					{
						newAns = newAns + "P" + "R";
					}
					if (ans[j] == 'S')
					{
						newAns = newAns + "S" + "P";
					}
				}
				ans = newAns;
			}

			vector<int> count = { 0, 0, 0 };
			for (int i = 0; i < ans.length(); i++)
			{
				if (ans[i] == 'R')
				{
					count[0]++;
				}
				if (ans[i] == 'P')
				{
					count[1]++;
				}
				if (ans[i] == 'S')
				{
					count[2]++;
				}
			}
			if (count[0] != r || count[1] != p || count[2] != s)
			{
				continue;
			}

			if (!hasAns)
			{
				bestAns = ans;
				hasAns = true;
			}


			int step = 1;
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j <= ans.length() - 2 * step; j += 2 * step)
				{
					string first = "";
					string second = "";

					for (int k = j; k < j + step; k++)
					{
						first += ans[k];
						second += ans[k + step];
					}
					if (first > second)
					{
						swap(first, second);
					}
					for (int k = j; k < j + step; k++)
					{
						ans[k] = first[k - j];
						ans[k + step] = second[k - j];
					}
				}
				step *= 2;
			}
			if (bestAns > ans)
			{
				bestAns = ans;
			}
		}

		if (!hasAns)
		{
			cout << "Case #" << tt << ": IMPOSSIBLE" << endl;
			continue;
		}


		//printf( "Case #%d: ", tt );
		cout << "Case #" << tt << ": " << bestAns << endl;
	}
	return 0;
}