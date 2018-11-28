#include <iostream>
#include <cstring>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
#include <set>
#include <string>
using namespace std;
/*the first answer*/
/*
int main()
{
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("result.txt", "w", stdout);
	int test_case;
	cin >> test_case;
	int index = 0;
	while (test_case--)
	{
		cout << "Case #" << ++index << ": ";
		int value;
		cin >> value;
		if (value == 0)
		{
			cout << "INSOMNIA" << endl;
			continue;
		}
		string digit = to_string(value);
		set<char> s;

		for (int i = 0; i < digit.size(); ++i)
		{
			s.insert(digit[i]);
		}
		if (s.size() == 10) cout << value << endl;
		for (int i = 2;; ++i)
		{
			int next = value*i;
			digit = to_string(next);
			for (int j = 0; j < digit.size(); ++j)
			{
				s.insert(digit[j]);
			}
			if (s.size() == 10)
			{
				cout << next << endl;
				break;
			}
		}

	}

}*/
/*
int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("result.txt", "w", stdout);
	int test_case;
	cin >> test_case;
	int index = 0;
	while (test_case--)
	{
		cout << "Case #" << ++index << ": ";
		string s;
		cin >> s;
		s.push_back('+');
		int len = s.size();
		int i = 0;
		int j = i + 1;
		int result = 0;
		while (j < len)
		{
			if (s[i] != s[j])
			{
				result++;
			}
			i++;
			j++;
		}
		cout << result << endl;

	}

}*/
int main()
{
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("result.txt", "w", stdout);
	int test_case;
	cin >> test_case;
	int index = 0;
	while (test_case--)
	{
		cout << "Case #" << ++index << ": ";
		
		int k, c, s;
		cin >> k >> c >> s;
		long long len = pow(k,c-1) ;
		if (len == 0)
		{
			cout << 1;
		}
		for (int i = 0; i < s&&len!=0; ++i)
		{
			cout << i*len +1<<" ";
		}
		
		cout << endl;

	}

}