#include "stdio.h"
#include "algorithm"
#include <string>
#include "iostream"
using namespace std;

bool myfunction(string s)
{
	int t = s.find('-');
	if (t==-1)
		return false;
	return true;
}
int main()
{
	ios_base::sync_with_stdio(false);

	string s;
	int n;
	freopen("B-large.in", "rt", stdin);
	freopen("B-large 3.ou", "wt", stdout);
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		cin >> s;
		int a=1, b;
		int c = 0;
		while (myfunction(s))
		{
			if (s[0] == '+')
			{
				for (int j = a; j < s.size(); j++)
				{
					if (s[j] == '-')
					{
						break;
					}
					a++;
				}
				for (int j = 0; j < a+1; j++)
				{
					s[j] = '-';
				}
				c++;
			}
			else
			{
				for (int j = a; j < s.size(); j++)
				{
					if (s[j] == '+')
					{
						break;
					}
					a++;
				}
				for (int j = 0; j < a+1; j++)
				{
					s[j] = '+';
				}
				c++;
			}
		}
		printf("Case #%d: %d\n", i + 1, c);
	}
	return 0;
}