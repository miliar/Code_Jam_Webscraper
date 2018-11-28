#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

int main()
{
	//freopen("C:\\Users\\wayne\\Downloads\\input.txt", "r", stdin);
	//freopen("C:\\Users\\wayne\\Downloads\\output.txt", "w", stdout);
	freopen("C:\\Users\\wayne\\Downloads\\A-small-attempt0.in", "r", stdin);
	freopen("C:\\Users\\wayne\\Downloads\\Small-output.out", "w", stdout);
	//freopen("C:\\Users\\wayne\\Downloads\\A-large-practice.in", "r", stdin);
	//freopen("C:\\Users\\wayne\\Downloads\\Large-output.out", "w", stdout);
	int t;
	bool d, s, nc, temp;
	char b[4][4], c, w;

	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		d = false;
		s = false;
		nc = false;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				cin >> b[j][k];
		for (int j = 0; j < 4 && !nc; j++)
			for (int k = 0; k < 4 && !nc; k++)
				if (b[j][k] == '.')
					nc = true;
		for (int j = 0; j < 4 && !s; j++)
		{
			c = b[j][0] == 'T' ? b[j][1] : b[j][0];
			temp = c != '.' ? true : false;
			for (int k = 1; k < 4 && c != '.'; k++)
				if (b[j][k] != c && b[j][k] != 'T')
					temp = false;
			if (temp)
			{
				w = c;
				s = true;
			}

			c = b[0][j] == 'T' ? b[1][j] : b[0][j];
			temp = c != '.' ? true : false;
			for (int k = 1; k < 4 && c != '.'; k++)
				if (b[k][j] != c && b[k][j] != 'T')
					temp = false;
			if (temp)
			{
				w = c;
				s = true;
			}
		}
		c = b[0][0] == 'T' ? b[1][1] : b[0][0];
		temp = c != '.' ? true : false;
		for (int j = 1, k = 1; j < 4 && k < 4 && temp; j++, k++)
		{
			if (b[j][k] == '.')
				temp = false;
			else if (b[j][k] == 'T')
				continue;
			else if (b[j][k] != c)
				temp = false;
		}
		if (temp)
		{
			w = b[0][0];
			d = true;
		}
		c = b[0][3] == 'T' ? b[1][2] : b[0][3];
		temp = c != '.' ? true : false;
		for (int j = 1, k = 2; j < 4 && k >= 0 && temp; j++, k--)
		{
			if (b[j][k] == '.')
				temp = false;
			else if (b[j][k] == 'T')
				continue;
			else if (b[j][k] != c)
				temp = false;
		}
		if (temp)
		{
			w = b[0][3];
			d = true;
		}
		cout << "Case #" << i << ": ";
		if (s || d)
			cout << w << " won\n";
		else if (nc)
			cout << "Game has not completed\n";
		else
			cout << "Draw\n";
	}
	return 0;
}