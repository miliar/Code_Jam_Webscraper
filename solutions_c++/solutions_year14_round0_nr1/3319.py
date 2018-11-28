#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <string>
#include <cstdio>

using namespace std;

string solve()
{
	int row;
	cin >> row;
	vector <int> v;
	for (int i = 1; i <= 4; ++i)
	{
		for (int j = 1; j <= 4; ++j)
		{
			int num;
			cin >> num;
			if (i == row)
				v.push_back(num);
		}
	}

	cin >> row;
	bool found = false;
	int ans;
	string ret;
	for (int i = 1; i <= 4; ++i)
	{
		for (int j = 1; j <= 4; ++j)
		{
			int num;
			cin >> num;
			if (i == row)
			{
				if (find(v.begin(), v.end(), num) != v.end())
				{
					if (found)
						ret = "Bad magician!";
					found = true;
					ans = num;
				}
			}
		}
	}
	if (!found)
		ret =  "Volunteer cheated!";
	else if (ret != "Bad magician!")
	{
		ostringstream oss;
		oss << ans;
		ret = oss.str();
	}
	return ret;
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		string ans = solve();
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
}