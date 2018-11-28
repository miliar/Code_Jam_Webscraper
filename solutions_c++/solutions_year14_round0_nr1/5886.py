#include <iostream>
#include <limits>
using namespace std;

bool isContained (int r[4], int a)
{
	for (int i = 0; i < 4; i++)
	{
		if (r[i] == a)
			return true;
	}
	return false;
}

int main (void)
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		cout << "Case #" << (t+1) <<": ";
		
		int row;
		int r1[4], r2[4];
		cin >> row;

		for (int i = 1; i <= 4; i++)
		{
			int k;
			for (int j = 0; j < 4; j++)
			{
				cin >> k;
				if (i == row)
					r1[j] = k;
			}
		}
		
		cin >> row;
		int possibilities = 0;
		for (int i = 1; i <= 4; i++)
		{
			int k;
			for (int j = 0; j < 4; j++)
			{
				cin >> k;
				if (i == row)
				{
					r2[j] = k;
					possibilities += isContained(r1, k) ? 1 : 0;
				}
			}
		}
		
		if (possibilities == 0)
		{
			cout << "Volunteer cheated!" << endl;
			continue;
		}
		if (possibilities > 1)
		{
			cout << "Bad magician!" << endl;
			continue;
		}
		
		for (int i = 0; i < 4; i++)
		{
			if (isContained(r2, r1[i]))
			{
				cout << r1[i] << endl;
				break;
			}
		}
	}
}
