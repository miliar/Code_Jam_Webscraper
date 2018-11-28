#include <iostream>
using namespace std;

int getMat(int arr[4][4])
{
	for (int i=0;i<4;i++)
	{
		for (int j=0;j<4;j++)
		{
			cin >> arr[j][i];
		}
	}
}

int solve(int arr1[4][4], int r1, int arr2[4][4], int r2)
{
	int nums[17] = {0};
	for (int i=0;i<4;i++)
	{
		nums[arr1[i][r1-1]]++;
		nums[arr2[i][r2-1]]++;
	}
	int sol = -2;
	for (int i=1;i<=16;i++)
	{
		if (nums[i] == 2)
		{
			if (sol == -2)
				sol = i;
			else
				return -1;
		}
	}
	return sol;
}

int main() {
	int a[4][4], b[4][4];
	int tests;
	cin >> tests;
	for (int test=0;test<tests;test++)
	{
		int r1,r2;
		cin >> r1;
		getMat(a);
		cin >> r2;
		getMat(b);
		cout << "Case #" << test+1 << ": ";
		switch (solve(a,r1,b,r2))
		{
			case -1:
				cout << "Bad magician!\n";
				break;
			case -2:
				cout << "Volunteer cheated!\n";
				break;
			default:
				cout << solve(a,r1,b,r2) << endl;
		}
	}
	return 0;
}