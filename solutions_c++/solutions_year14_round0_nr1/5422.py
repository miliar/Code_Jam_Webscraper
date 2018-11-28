#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <set>
#include <vector>
using namespace std;
int main()
{
	int n;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		int ans1, ans2;
		cin >> ans1;
		int A[10][10], B[10][10];
		for (int ii = 1; ii <= 4; ii++)
		{
			for (int jj = 1; jj <= 4; jj++)
			{
				cin >> A[ii][jj];
			}
		}
		cin >> ans2;
		for (int ii = 1; ii <= 4; ii++)
		{
			for (int jj = 1; jj <= 4; jj++)
			{
				cin >> B[ii][jj];
			}
		}
		int cnt = 0;
		int k;
		for (int ii = 1; ii <= 4; ii++)
		{
			for (int jj = 1; jj <= 4; jj++)
			{
				if (A[ans1][ii] == B[ans2][jj])
				{
					k = A[ans1][ii];
					cnt++;
				}
			}
		}
		if (cnt == 1)
		{
			cout << "Case #" << i << ":" << " " << k << endl;
		}
		if (cnt == 0)
		{
			cout << "Case #" << i << ": Volunteer cheated!" << endl;
		}
		if (cnt > 1)
		{
			cout << "Case #" << i << ": Bad magician!" << endl;
		}
	}



	return 0;
}