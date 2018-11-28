#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
#include <string>
#include <map>
#include <set>
using namespace std;


int  main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int q = 1; q <= t; q++)
	{
		int smax;
		cin >> smax;

		string 	s;
		cin >> s;

		int stay = 0;
		int ans = 0;
		for (int i = 0; i < s.length(); i++)
		{
			int temp = s[i] - '0';
			if (stay < i)
			{
				ans += (i - stay);
				stay = i + temp;
			}
			else
			{
				stay += temp;
			}
		}

		cout << "Case #" << q << ": " << ans << endl;
	}
	return 0;
}