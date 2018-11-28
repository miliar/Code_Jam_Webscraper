#include <iostream>
#include <vector>
#include <list>
#include <set>
#include <string>
#include <cmath>
#include <climits>
#include <algorithm>

using namespace std;

inline void swap(char& a, char& b)
{
	char temp = a;
	a = b;
	b = temp;
}

void flip(string& s, int n)
{
	for (int i = 0; i < n / 2; ++i)
	{
		if (s[i] == '-')
			s[i] = '+';
		else
			s[i] = '-';
		if (s[n - i] == '-')
			s[n - i] = '+';
		else
			s[n - i] = '-';
		if (s[i] != s[n - i])
			swap(s[i], s[n - i]);
	}
}

void complement(string& s, int n)
{
	for(int i = 0; i < n; ++i)
	{
		if(s[i] == '+') s[i] = '-';

		else s[i] = '+';

	}
}

int main()
{
	int t;
	cin >> t;
	for (int xt = 1; xt <= t; ++xt)
	{
		string s;
		cin >> s;
		int count = 0;
		while (s.find('-') != s.npos)
		{
			++count;
			int i = 1;
			while (i < s.size())
			{
				if (s[i] == '-' && s[i - 1] == '+')
				{
					complement(s, i);
					break;
				}
				++i;
			}
			if (i == s.size())
				break;
		}
		cout << "Case #" << xt << ": ";
		cout << count << endl;
	}
}