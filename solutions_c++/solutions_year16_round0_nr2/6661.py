#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

string s;
int main(void)
{
	freopen("inputB.txt", "r", stdin);
	freopen("outputB.txt", "w", stdout);
	int i, j, k;
	int r = 1;
	int cnt;
	int t;

	cin >> t;

	while (t--)
	{
		cin >> s;
		i = 1;
		cnt = 0;
		j = s.size();
		while (1)
		{
			if (j < i) break;
			if (s[j - i] == '-')
			{
				for (k = 0; k < j; k++)
				{
					if (s[k] == '+') s[k] = '-';
					else if (s[k] == '-') s[k] = '+';
				}
				cnt++;
			}
			i++;
		}
		printf("Case #%d: %d\n", r++, cnt);
	}
}