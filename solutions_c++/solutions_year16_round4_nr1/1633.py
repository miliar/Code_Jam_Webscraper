#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <sstream>
using namespace std;

#define pb push_back

int n,nt,r,p,s;
int iter;
int tmp;
int test;
bool possible;
string str1, str2;
char c1, c2;

string makeDouble(string in, int iter)
{
	string s = "";
	int m = in.length();
	for (int i = 0; i < m; i++)
	{
		if (iter == 1)
		{
			if (in[i] == 'P')
				s.append("PR");
			if (in[i] == 'S')
				s.append("PS");
			if (in[i] == 'R')
				s.append("RS");
		}
		else
		{
			if (in[i] == 'P')
				s.append("PR");
			if (in[i] == 'S')
				s.append("PS");
			if (in[i] == 'R')
				s.append("SR");
		}
	}
	return s;
}

int main()
{
	int test;
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d\n", &test);
	for (int t = 1; t <= test; t++)
	{
		scanf("%d%d%d%d", &nt, &r, &p, &s);
		n = 1;
		iter = nt - 1;
		while (nt)
		{
			nt--;
			n *= 2;
		}
		int n1 = n;
		int r1 = r;
		int p1 = p;
		int s1 = s;
		possible = true;
		while (n1 > 2)
		{
			int p2 = r1 - s1 + p1;
			if ((p2 % 2) || (p2 < 0))
			{
				possible = false;
				break;
			}
			int s2 = s1 - r1 + p1;
			if ((s2 % 2) || (s2 < 0))
			{
				possible = false;
				break;
			}
			int r2 = r1 - p1 + s1;
			if ((r2 % 2) || (r2 < 0))
			{
				possible = false;
				break;
			}
			p1 = p2 / 2;
			r1 = r2 / 2;
			s1 = s2 / 2;
			n1 /= 2;
		}
		if ((p1 > 1) || (r1 > 1) || (s1 > 1))
			possible = false;
		else
		{
			if (p1 & r1)
			{
				c1 = 'P';
				c2 = 'R';
			}
			if (p1 & s1)
			{
				c1 = 'P';
				c2 = 'S';
			}
			if (s1 & r1)
			{
				c1 = 'R';
				c2 = 'S';
			}
		}
		if (!possible)
			printf("Case #%d: IMPOSSIBLE\n", t);
		else
		{
			str1 = "";
			str2 = "";
			//option 1
			str1 += c1;
			str1 += c2;
			tmp = iter;
			while (str1.length() != n)
			{
				str1 = makeDouble(str1, tmp);
				tmp--;
			}
			//option 2
			str2 += c2;
			str2 += c1;
			tmp = iter;
			while (str2.length() != n)
			{
				str2 = makeDouble(str2, tmp);
				tmp--;
			}
			if (str1 < str2)
				cout << "Case #" << t << ": " << str1 << endl;
			else
				cout << "Case #" << t << ": " << str2 << endl;
		}
	}
	return 0;
}