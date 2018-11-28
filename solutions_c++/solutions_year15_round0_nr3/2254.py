#include <iostream>
#include <string>
#include <vector>
#include <stack>

using namespace std;

// 1 == 1
// i == 2
// j == 3
// k == 4

char i2c(int x)
{
	if (x == 2)
	{
		return 'i';
	}
	else if (x == 3)
	{
		return 'j';
	}
	else if (x == 4)
	{
		return 'k';
	}
	else
	{
		return '1';
	}
}

int c2i(char c)
{
	if (c == 'i')
	{
		return 2;
	}
	else if (c == 'j')
	{
		return 3;
	}
	else if (c == 'k')
	{
		return 4;
	}
	else
	{
		return 1;
	}
}

int multi(int a, int b)
{
	static vector<vector<int> > m = {
		{1, 2, 3, 4},
		{2, -1, 4, -3},
		{3, -4, -1, 2},
		{4, 3, -2, -1}
	};
	int oa = (a < 0 ? -a : a);
	int ob = (b < 0 ? -b : b);
	int val = m[oa-1][ob-1];
	if (a < 0)
		val = -val;
	if (b < 0)
		val = -val;
	// cout << a << " " << b << " " << val << endl;
	return val;
}

int divi(int a, int b)
{
	// c = a / b
	// b * c = a
	static vector<vector<int> > m = {
		{1, 2, 3, 4},
		{2, -1, 4, -3},
		{3, -4, -1, 2},
		{4, 3, -2, -1}
	};
	int ob = b < 0 ? -b : b;
	for (int i = 0; i < 4; ++i)
	{
		if (m[ob-1][i] == a)
		{
			int c = i + 1;
			if (b < 0)
			{
				c = -c;
			}
			return c;
		}
		if (m[ob-1][i] == -a)
		{
			int c = -(i + 1);
			if (b < 0)
			{
				c = -c;
			}
			return c;
		}
	}
	return 0;
}

bool splitijk(int len, int t, string& s)
{
	int val = 1;
	vector<int> st(len, 0);
	for (int i = 0; i < len; ++i)
	{
		val = multi(val, c2i(s[i]));
		st[i] = val;
	}
	vector<int> tt(t+1, 0);
	tt[0] = 1;
	for (int i = 1; i <= t; ++i)
	{
		tt[i] = multi(tt[i-1], st[len-1]);
	}

	// cout << tt[t] << endl;

	if (tt[t] != -1)
		return false;

	val = 1;
	for (int i = 0; i < t; ++i)
	{
		for (int j = 0; j < len; ++j)
		{
			val = multi(val, c2i(s[j]));
			if (val == 2)
			{
				int r = divi(st[len-1], st[j]);
				r = multi(r, tt[t-1-i]);
				if (r == 2)
				{
					int ii = i;
					int jj = j + 1;
					if (jj == len)
					{
						jj = 0;
						++ii;
					}
					int jk = 1;
					while(ii < t)
					{
						while(jj < len)
						{
							jk = multi(jk, c2i(s[jj]));
							if (jk == 3)
							{
								int r = divi(st[len-1], st[jj]);
								r = multi(r, tt[t-1-ii]);
								if (r == 4)
								{
									return true;
								}
							}
							++jj;
						}
						++ii;
						jj = 0;
					}
				}
			}
		}
	}

	return false;
}

int main()
{
	int t;
	cin >> t;
	for (int c = 1; c <= t; ++c)
	{
		int seglen, times;
		string seg;
		cin >> seglen >> times >> seg;
		if (splitijk(seglen, times, seg))
		{
			cout << "Case #" << c << ": YES" << endl;
		}
		else
		{
			cout << "Case #" << c << ": NO" << endl;
		}
	}
	return 0;
}