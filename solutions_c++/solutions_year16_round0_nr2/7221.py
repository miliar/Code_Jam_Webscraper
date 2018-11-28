#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;


void flip(string &str, int i)
{
	if (str[i] == '+')
		str[i] = '-';
	else
		str[i] = '+';
}

void reverse(string &str, int e)
{
	for (int i = 0; i <= e/2; i++)
	{
		flip(str, i);
		if (e - i != i)
			flip(str, e - i);
		swap(str[i], str[e - i]);
	}
}

void trim(string &str)
{
	for (int i = str.length()-1; i >= 0; i--)
	{
		if (str[i] == '+')
			str.erase(str.begin() + i);
		else
			break;
	}
}

int main()
{
	ifstream cin("a.in");
	ofstream cout("a.out");
	int t;
	cin >> t;
	for (int k = 1; k <= t; k++)
	{
		string str;
		cin >> str;

		int ans = 0;
		while (1)
		{
			trim(str);
			if (str == "")
				break;
			int flipPos;

			flipPos = str.find_last_of(str[0]);

			reverse(str, flipPos);
			ans++;
		}
		cout << "Case #" << k << ": " << ans << endl;

	}
	return 0;
}