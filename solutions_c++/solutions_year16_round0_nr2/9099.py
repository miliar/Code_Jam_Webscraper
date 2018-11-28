#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>

using namespace std;

bool pl(char s[],int size)
{
	for (int i = 0; i < size; i++)
	{
		if (s[i] == '-') return false;
	}

	return true;
}

int main()
{
	char x;

	int t = 0, cou = 1;

	cin >> t;

	cin.get(x);

	while (t--)
	{
		char st[105];

		int counter = 0;

		cin.getline(st, 100, '\n');

		int size = strlen(st);

		while (!pl(st , size))
		{
			if (st[0] == '-')
			{
				for (int i = 0; i < size && st[i] == '-'; i++)
				{
					st[i] = '+';
				}
			}

			else
			{
				for (int i = 0; i < size && st[i] == '+'; i++)
				{
					st[i] = '-';
				}
			}

			counter++;
		}

		cout << "Case #" << cou << ": " << counter << endl;

		cou++;
	}
}