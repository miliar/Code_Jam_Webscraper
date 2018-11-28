#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <stdio.h>

using namespace std;

const int m = 4;
const int k = 17;


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt", "w", stdout);

	int c1[m][m], c2[m][m];
	int f[k];
	char* format = "Case #%d: %s\n";
	char* format2 = "Case #%d: %d\n";

	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int a1, a2;
		cin >> a1;

		for (int j = 0; j < m; j++)
		{
			for (int l = 0; l < m; l++)
			{
				cin >> c1[j][l];
			}
		}

		cin >> a2;

		for (int j = 0; j < m; j++)
		{
			for (int l = 0; l < m; l++)
			{
				cin >> c2[j][l];
			}
		}

		for (int j = 0; j < k; j++)
			f[j] = 0;

		for (int j = 0; j < m; j++)
		{
			f[c1[a1-1][j]]++;
			f[c2[a2-1][j]]++;
		}

		int countAns = 0;
		int lastAns = 0;
		for (int j = 0; j < k; j++)
		{
			if (f[j] == 2)
			{
				countAns++;
				lastAns = j;
			}
		}


		if (countAns == 1)
		{
			printf(format2, i + 1, lastAns);
		}
		else if (countAns > 1)
		{
			printf(format, i + 1, "Bad magician!");
		}
		else
		{
			printf(format, i + 1, "Volunteer cheated!");
		}
	}
	return 0;
}