#include "test.h"
#include <vector>
#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int len;
string str;
int main()
{
	int t;
	cin >> t;
	for (int times = 1; times <= t; times++)
	{
		cin >> len >> str;
		int total = 0, sol = 0;
		for (size_t i = 0; i < str.length(); i++)
		{
			if (i && total < i) sol = max(sol, (int)i - total);
			total += str[i] - '0';
		}
		cout << "Case #" << times << ": " << sol << endl;
	}
	return 0;
}
