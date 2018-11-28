#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cstdio>
#include <string>

using namespace std;


signed main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		string s;
		cin >> s;
		bool ismin = s[0] == '-';
		int rs = 0;
		for (int j = 1; j < s.size(); j++)
		{
			if (s[j] != s[j - 1])
				rs++;
		}
		cout << "Case #" << i + 1 << ": " << rs + (ismin != (rs & 1)) << endl;
			
	}
}