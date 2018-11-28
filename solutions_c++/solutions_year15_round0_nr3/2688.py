#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;
char mul(char x, char y)
{
	if (x == '1')
		return y;
	else if (x == 'i')
	{
		if (y == '1')
			return 'i';
		if (y == 'i')
			return '1';
		if (y == 'j')
			return 'k';
		if (y == 'k')
			return 'j';
	}
	else if (x == 'j')
	{
		if (y == '1')
			return 'j';
		if (y == 'i')
			return 'k';
		if (y == 'j')
			return '1';
		if (y == 'k')
			return 'i';
	}
	else if (x == 'k')
	{
		if (y == '1')
			return 'k';
		if (y == 'i')
			return 'j';
		if (y == 'j')
			return 'i';
		if (y == 'k')
			return '1';
	}
}

int op(char x, char y)
{
	if (x == y || (x == 'i' && y == 'k') || (x == 'j' && y == 'i') || (x == 'k' && y == 'j'))
		return -1;
	return 1;
}

int main()
{
	ifstream inf("in.txt");
	int t, T;
	inf >> T;
	map<char, map<char, char> > m;
	ofstream outf("res.txt");
	for (t = 1;t <= T;t++)
	{
		int l, x;
		inf >> l >> x;
		string tmp, s;
		inf >> tmp;
		int i;
		for (i = 0;i < x;i++)
			s += tmp;
		bool fi = false, fj = false, fk = false;
		char cur = s[0];
		i = 1;
		int q = 1, len = s.size();
		while (i < len)
		{
			if (cur == 'i')
			{
				fi = true;
				break;
			}
			q *= op(cur, s[i]);
			cur = mul(cur, s[i++]);
		}
		if (i < len)
			cur = s[i];

		while (i < len)
		{
			if (cur == 'j')
			{
				fj = true;
				break;
			}
			i++;
			if (i >= len)
				break;
			q *= op(cur, s[i]);
			cur = mul(cur, s[i]);
		}
		i++;
		if (i < len)
			cur = s[i];
		while (i < len)
		{
			i++;
			if (i >= len)
				break;
			q *= op(cur, s[i]);
			cur = mul(cur, s[i]);
		}
		if (cur == 'k')
		{
				fk = true;
		}
		if (fi && fj && fk && q == 1)
			outf << "Case #" << t << ": " << "YES" << endl;
		else
			outf << "Case #" << t << ": " << "NO" << endl;
	}
    return 0;
}