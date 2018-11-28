#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
using namespace std;
struct number
{
	bool sign;
	char c;
	number()
	{
		sign = true;
	}
	number(char _c)
	{
		sign = true;
		c = _c;
	}
};
number operator*(number x, number y)
{
	number ans;
	int neg = 0;
	if (x.sign == false) neg++;
	if (y.sign == false) neg++;
	char res;
	char a = x.c, b = y.c;
	bool anssign = false;
	if (a == '1')
	{
		anssign = true;
		res = b;
	}
	else if (a == 'i')
	{
		if (b == '1')
		{
			anssign = true;
			res = 'i';
		}
		else if (b == 'i')
		{
			anssign = false;
			res = '1';
		}
		else if (b == 'j')
		{
			anssign = true;
			res = 'k';
		}
		else if (b == 'k')
		{
			anssign = false;
			res = 'j';
		}
	}
	else if (a == 'j')
	{
		if (b == '1')
		{
			anssign = true;
			res = 'j';
		}
		else if (b == 'i')
		{
			anssign = false;
			res = 'k';
		}
		else if (b == 'j')
		{
			anssign = false;
			res = '1';
		}
		else if (b == 'k')
		{
			anssign = true;
			res = 'i';
		}
	}
	else
	{
		if (b == '1')
		{
			anssign = true;
			res = 'k';
		}
		else if (b == 'i')
		{
			anssign = true;
			res = 'j';
		}
		else if (b == 'j')
		{
			anssign = false;
			res = 'i';
		}
		else
		{
			anssign = false;
			res = '1';
		}
	}
	if (neg % 2 == 1)
	{
		anssign = !anssign;
	}
	ans.sign = anssign;
	ans.c = res;
	return ans;
}
number pref[10007], suff[10007];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		int l, x;
		cin >> l >> x;
		string s;
		cin >> s;
		string t;
		for (int i = 1; i <= x; i++)
		{
			t += s;
		}
		s = t;
		suff[s.length() - 1] = number(s[s.length() - 1]);
		for (int i = s.length() - 2; i >= 0; i--)
		{
			suff[i] = number(s[i])*suff[i + 1];
		}
		bool ok = false;
		number cur(s[0]);
		for (int i = 1; i < s.length(); i++)
		{
			if (cur.sign == true && cur.c == 'i')
			{
				number sec(s[i]);
				for (int j = i; j < s.length() - 1; j++)
				{
					if (sec.sign == true && sec.c == 'j' && suff[j + 1].sign == true && suff[j + 1].c == 'k') ok = true;
					sec = sec*number(s[j + 1]);
				}
			}
			cur = cur*number(s[i]);
		}
		if (ok)
		{
			cout << "Case #" << tt << ": YES" << endl;
		}
		else
		{
			cout << "Case #" << tt << ": NO"<< endl;
		}
	}
}