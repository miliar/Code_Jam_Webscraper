#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<fstream>
using namespace std;
int common(int line1[4], int line2[4])
{
	int last = -1;
	int numCommon = 0;
	for (int i = 0; i <4 ; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (line2[j] == line1[i])
			{
				numCommon++;
				last = line2[j];
			}
		}
	}

	if (numCommon == 1)
		return last;
	if (numCommon == 0)
		return 0;
	else
		return -1;
}
int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int numTests;
	cin >> numTests;
	for (int o = 0; o < numTests; o++)
	{
		printf("Case #%d: ", o + 1);
		int line1[4], line2[4], temp;
		int n;
		cin >> n;
		n--;
		for (int i = 0 ; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (i == n)
				{
					scanf("%d", &line1[j]);
				}
				else
				{
					scanf("%d", &temp);
				}
			}
		}
		int m;
		cin >> m;
		m--;
		for (int i = 0 ; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (i == m)
				{
					scanf("%d", &line2[j]);
				}
				else
				{
					scanf("%d", &temp);
				}
			}
		}
		int x = common(line1, line2);
		if (x == 0)
		{
			cout << "Volunteer cheated!" << endl;
		} else if (x == -1)
		{
			cout << "Bad magician!" << endl;
		} else
		{
			cout << x << endl;
		}
	}

}