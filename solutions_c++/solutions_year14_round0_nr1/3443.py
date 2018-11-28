#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;



void solve()
{
	int a, b;
	cin >> a;
	int da[4][4];
	int db[4][4];
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			cin >> da[i][j];
		}
	}
	cin >> b;
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			cin >> db[i][j];
		}
	}
	vector<int> ans;
	--a, --b;
	for (int i = 0; i < 4; ++i)
	{
		for(int j = 0; j < 4; ++j)
		{
			if (da[a][i] == db[b][j])
				ans.push_back(da[a][i]);
		}
	}
	if (ans.empty())
		cout << "Volunteer cheated!";
	else if (ans.size() > 1)
		cout << "Bad magician!";
	else
		cout << ans[0];
}

void main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
}