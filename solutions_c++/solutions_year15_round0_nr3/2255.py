#include<bits/stdc++.h>
using namespace std;
map<pair<int, int>, int> mp;
int mul(int m1, int m2)
{
	int a[4][4] = { { 1, 2, 3, 4 }, { 2, -1, 4, -3 }, { 3, -4, -1, 2 }, { 4, 3, -2, -1 } };
	int tmp = a[abs(m1) - 1][abs(m2) - 1];
	if (m1 / abs(m1) == m2 / abs(m2))
		return tmp;
	else
		return -tmp;
}
int divv(int m1, int m2)
{
	if (m1 < 0)
	{
		int a[4][3] = { { 2, 3, 4 }, { -1, -4, 3 }, { 4, -1, -2 }, { -3, 2, -1, } };
		return a[-m1-1][m2-2];
	}
	else
	{
		int a[4][3] = { { -2, -3, -4 }, {1, 4, -3 }, {-4, 1, 2 }, {3, -2, 1 } };
		return a[m1-1][m2 - 2];
	}
}
int main()
{
	int i, j, k, t, n, m, x, l, y;
	cin >> t;
	for (x = 1; x <= t; ++x)
	{
		cin >> l >> y;
		string s, p;
		cin >> s;
		for (i = 0; i < s.size(); ++i)
			s[i] = s[i] - 'i' + 2 + '0';
		//cout << s << endl;
		for (i = 0; i < y; ++i)
			p += s;
		//cout << p << endl;
		int flag = 0;
		int c1, c2, c3;
		c1 = p[0] - '0';
		c2 = p[1] - '0';
		c3 = p[2] - '0';
		for (k = 3; k< p.size(); ++k)
			c3 = mul(c3, p[k] - '0');
		for (i = 1; i < p.size() - 1 && flag == 0; ++i)
		{
			if (i>1)
			{
				c1 = mul(c1, p[i - 1] - '0');
				c2 = p[i] - '0';
				c3 = divv(c3, p[i] - '0');
			}
			int ci3 = c3;
			for (j = i + 1; j < p.size() && flag == 0; ++j)
			{
				if (j>i + 1)
				{
					ci3 = divv(ci3, p[j - 1] - '0');
					c2 = mul(c2, p[j - 1] - '0');
				}
				if (c1 == 2 && c2 == 3 && ci3 == 4)
				{
					flag = 1;
				}
			}
			//if (i > 500)
			//	cout << "yo";
		}
		cout << "Case #" << x << ": ";
		if (flag == 0)
			cout << "NO\n";
		else
			cout << "YES\n";
	}
	return 0;
}