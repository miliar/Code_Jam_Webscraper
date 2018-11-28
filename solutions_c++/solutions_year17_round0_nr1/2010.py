#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stack>
#include <functional>
#include <set>
#include <queue>
#include <string>
#include <map>
#include <iomanip>
#include <sstream>

using namespace std;


int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		cout << "Case #" << t + 1 << ": ";
		string s;
		int k, cnt = 0;
		cin >> s >> k;
		for (int i = 0; i <= s.length() - k; i++)
			if (s[i] == '-')
			{
				cnt++;
				for (int j = i; j < i + k; j++)
				{
					if (s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
			}
		bool fl = false;
		for (int i = 0; i < s.length(); i++)
		{
			if (s[i] == '-')
			{
				cout << "IMPOSSIBLE" << endl;
				fl = true;
				break;
			}
		}
		if (!fl)
			cout << cnt << endl;
	}
}