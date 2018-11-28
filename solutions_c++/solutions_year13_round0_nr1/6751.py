#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
	int t, testc = 1;
	scanf("%i", &t);
	while (t--)
	{
		string s[4];
		for (int i = 0; i < 4; i++)
			cin>> s[i];
		bool bb = false;
		int c[4][2] = {0}, r[4][2] = {0}, d[2][2] = {0};
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				if (s[i][j] == 'X' || s[i][j] == 'T')
				{
					c[i][0]++, r[j][0]++;
					if (i == j)
						d[0][0]++;
					if (i + j == 3)
						d[1][0]++;
				}
				if (s[i][j] == 'O' || s[i][j] == 'T')
				{
					c[i][1]++, r[j][1]++;
					if (i == j)
						d[0][1]++;
					if (i + j == 3)
						d[1][1]++;
				}
				if (s[i][j] == '.')
					bb = true;
			}
		printf("Case #%i: ", testc++);
		bool b = false;
		for (int i = 0; i < 4; i++)
			if (c[i][0] == 4 || r[i][0] == 4 || d[i%2][0] == 4)
				b = true;
		if (b)
		{
			printf("X won\n");
			continue;
		}
		for (int i = 0; i < 4; i++)
			if (c[i][1] == 4 || r[i][1] == 4 || d[i%2][1] == 4)
				b = true;
		if (b)
		{
			printf("O won\n");
			continue;
		}
		if (bb)
		{
			printf("Game has not completed\n");
			continue;
		}
		printf("Draw\n");
	}
}
