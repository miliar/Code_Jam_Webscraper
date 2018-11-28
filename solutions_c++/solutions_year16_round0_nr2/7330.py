#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int n;
int main()
{
	cin >> n;
	string s;
	for (int i = 0; i < n; ++i)
	{
		cin >> s;
		int fn = 0;

		for (int j = s.length() - 1; j >= 0; --j)
		{
			if (s[j] == '+' && fn % 2 == 1 || s[j] == '-' && fn % 2 == 0)
			{
				fn++;
			}
		}

		printf("Case #%d: %d\n", i + 1, fn);
	}
}