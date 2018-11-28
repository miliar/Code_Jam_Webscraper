#include <iostream>
#include <cstring>
#include <string>

using namespace std;

string s;
int a[111];
int n;

int calc_plus(int len);

int calc_minus(int len)
{
	a[0] = 0;
	int ind = -1;
	for (int i = len; i >= 0; i--)
	{
		if (a[i] == 0)
		{
			ind = i;
			break;
		}
	}
	if (ind == 0)
		return 1;
	a[0] = 1;
	ind = -1;
	for (int i = len; i >= 0; i--)
	{
		if (a[i] == 1)
		{
			ind = i;
			break;
		}
	}
	if (ind == 0)
		return 0;
	for (int i = len - 1; i >= 1; i--)
	{
		if (a[i] != a[i + 1])
		{
			if (a[i + 1] == 0)
				return calc_minus(i);
			else
				return (calc_plus(i) + 1);
		}
	}
}

int calc_plus(int len)
{
	a[0] = 0;
	int ind = -1;
	for (int i = len; i >= 0; i--)
	{
		if (a[i] == 0)
		{
			ind = i;
			break;
		}
	}
	if (ind == 0)
		return 0;
	a[0] = 1;
	ind = -1;
	for (int i = len; i >= 0; i--)
	{
		if (a[i] == 1)
		{
			ind = i;
			break;
		}
	}
	if (ind == 0)
		return 1;
	for (int i = len - 1; i >= 1; i--)
	{
		if (a[i] != a[i + 1])
		{
			if (a[i + 1] == 0)
				return (calc_minus(i) + 1);
			else
				return calc_plus(i);
		}
	}
}

bool check()
{
	for (int i = 1; i <= n; i++)
		if (a[i] == 0)
			return false;
	return true;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out-2.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cin >> s;
		n = s.length();
		for (int j = 0; j < n; j++)
		{
			if (s[j] == '-')
				a[j + 1] = 0;
			else
				a[j + 1] = 1;
		}
		cout << "Case #" << i << ": ";
		cout << calc_plus(n) << endl;
	}
	return 0;
}