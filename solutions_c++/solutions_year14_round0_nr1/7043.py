#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	int number;
	cin >> number;
	for (int n = 0; n < number; n++)
	{
		int i, j, k;
		int first, r1[5][5];
		cin >> first;
		for (i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
				cin >> r1[i][j];
		}

		int second, r2[5][5];
		cin >> second;
		for (i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
				cin >> r2[i][j];
		}

		//compare
		int count = 0, ans;
		int s1[5], s2[5];
		for (int i = 0; i < 4; i++)
		{
			s1[i] = r1[first - 1][i];
			s2[i] = r2[second - 1][i];
		}
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (s1[i] == s2[j])
				{
					count++;
					ans = s1[i];
				}
					
			}
		}
			
		if (count == 0)
			cout << "Case #" << (n + 1) << ": Volunteer cheated!\n";
		else if (count == 1)
			cout << "Case #" << (n + 1) << ": " << ans << "\n";
		else
			cout << "Case #" << (n + 1) << ": Bad magician!\n";
	}

	return 0;
}