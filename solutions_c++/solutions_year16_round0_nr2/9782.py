#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;


int main()
{
	int T;
	cin >> T;
	for (int test = 1; test <= T; test++)
	{
		string s;
		cin >> s;
		int p = s.size()-1;
		for (int m = 0; ;m++)
		{
			while (p >= 0 && s[p] == '+') p--;
			if (p < 0)
			{
				printf("%s%d%s %d\n","Case #",test,":",m);
				break;
			}
			int t = 0;
			for (int i = 0; i <= p; i++)
			{
				if (s[i] == '+') s[i] = '-';
				else
				{
					t = i;
					break;
				}
			}
			if (t != 0) m++;
			string nw = s.substr(0,p+1);
			int tt = nw.size()-1;
			for (int i = 0; i < nw.size(); i++)
			{
				s[tt] = nw[i] == '+' ? '-' : '+';
				tt--;
			}
		}
	}
}
