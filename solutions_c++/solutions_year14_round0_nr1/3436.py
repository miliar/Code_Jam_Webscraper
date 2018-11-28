#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, first, second, ans, count, temp;
	int row[4];
	bool rd ;
	cin >> t;

	for (int k = 1; k <= t; k++)
	{
		ans = 0; count = 0; rd = false;
		cout << "Case #" << k << ": ";
		cin >> first;
		for (int i = 1; i <= 12; i++)
		{
			
			if (first * 4 - 3 == i)
			{
				for (int j = 0; j < 4; j++)
					cin >> row[j];
				rd = true;
			}
			cin >> temp;
		}
		if (!rd)
		for (int j = 0; j < 4; j++)
			cin >> row[j];
		rd = false;
		cin >> second;
		for (int i = 1; i <= 12; i++)
		{
			
			if (second * 4 - 3 == i)
			{
				for (int j = 0; j < 4; j++)
				{
					cin >> temp;
					if (row[0] == temp)
					{
						count++;
						ans = row[0];
					}
					else if (row[1] == temp)
					{
						count++;
						ans = row[1];
					}
					else if (row[2] == temp)
					{
						count++;
						ans = row[2];
					}
					else if (row[3] == temp)
					{
						count++;
						ans = row[3];
					}
				}
				rd = true;
			}
			cin >> temp;
		}

		if (!rd)
		for (int j = 0; j < 4; j++)
		{
			cin >> temp;
			if (row[0] == temp)
			{
				count++;
				ans = row[0];
			}
			else if (row[1] == temp)
			{
				count++;
				ans = row[1];
			}
			else if (row[2] == temp)
			{
				count++;
				ans = row[2];
			}
			else if (row[3] == temp)
			{
				count++;
				ans = row[3];
			}
		}

		if (count == 1)
			cout << ans << endl;
		else if (count > 1)
			cout << "Bad magician!\n";
		else
			cout << "Volunteer cheated!\n";

	}
	
	
	return 0;
}