#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdlib>
#include <random>
#include <string>
#include <algorithm>
using namespace std;

std::string s;

void shorten()
{
	while (!s.empty() && s.back() == '1')
		s.pop_back();
}

void rotate()
{
	reverse(s.begin(), s.end());
	for (int i = 0; i < s.size(); ++i)
		s[i] = '0' + (1 - (s[i] - '0'));
}

void solve()
{
	int counter = 0;

	while (!s.empty())
	{
		if (s.back() == '1')
		{
			shorten();
			continue;
		}
		if (s[0] == '1')
		{
			for (int i = 0; i < s.size(); ++i)
			{
				if (s[i] == '1')
					s[i] = '0';
				else
					break;
			}
			++counter;
		}
		rotate();
		++counter;
	}

	std::cout << counter << std::endl;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	cin >> t;
	for (int test_case = 1; test_case <= t; ++test_case)
	{
		cout << "Case #" << test_case << ": ";
		cin >> s;
		for (int i = 0; i < s.size(); ++i)
		{
			if (s[i] == '-')
				s[i] = '0';
			else
				s[i] = '1';
		}
		solve();
	}
}