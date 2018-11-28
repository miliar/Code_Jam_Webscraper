#include <iostream>
#include <string>

using namespace std;

void main()
{
	int t, l, c, i, h, j, x;
	string s;

	cin >> t;
	x = 1;
	while (t > 0)
	{
		cin >> s;
		l = s.length() - 1;
		c = 0;
		while (l >= 0)
		{
			while (l >= 0 && s[l] == '+')
				l--;
			if (l < 0) break;

			if (s[0] == '+')
			{
				i = 0;
				while (i < l && s[i] == '+') i++;

				i--;
				for (j = 0, h = 0; j <= i / 2; j++)
				{
					if (j * 2 == i)
					{
						s[j] = s[j] == '+' ? '-' : '+';
					}
					else
					{
						char sj = s[j];
						s[j] = s[i - j] == '+' ? '-' : '+';
						s[i - j] = sj == '+' ? '-' : '+';
					}
					h = 1;
				}

				c += h;
				for (j = 0, h = 0; j <= l / 2; j++)
				{
					if (j * 2 == l)
					{
						s[j] = s[j] == '+' ? '-' : '+';
					}
					else
					{
						char sj = s[j];
						s[j] = s[l - j] == '+' ? '-' : '+';
						s[l - j] = sj == '+' ? '-' : '+';
					}
					h = 1;
				}
				c += h;
			}
			else
			{
				for (j = 0, h = 0; j <= l / 2; j++)
				{
					if (j * 2 == l)
					{
						s[j] = s[j] == '+' ? '-' : '+';
					}
					else
					{
						char sj = s[j];
						s[j] = s[l - j] == '+' ? '-' : '+';
						s[l - j] = sj == '+' ? '-' : '+';
					}
					h = 1;
				}
				c += h;
			}
			l -= 1;
		}
		cout << "Case #" << x <<": " << c << endl;
		x++;
		t--;
	}
}