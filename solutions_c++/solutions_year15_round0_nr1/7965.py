#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
using namespace std;

double max(double a, double b, double c)
{
	double maxab = (a > b) ? a : b;
	return (maxab > c) ? maxab : c;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("t2.txt","w",stdout);
	int testnumber; cin >> testnumber;
	for (int test = 1; test <= testnumber; test++)
	{
		int add = 0, all = 0;
		int maxs; cin >> maxs;
		string s; cin >> s;
		for (int i = 0; i <= maxs; i++)
		{
			if (s[i] != '0' && all < i)
			{
				add += i - all;
				all = i;
			}
			all += s[i] - '0';
		}
		cout << "Case #" << test << ": " << add << endl; 
	}
}