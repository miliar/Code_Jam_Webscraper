#include<iostream>
#include<vector>

using namespace std;
int arr[6][6][6];

int main()
{
	int test, testcase;
	freopen("C://Users//Tanvir//Desktop//D-small-attempt2.in", "r", stdin);
	freopen("C://Users//Tanvir//Desktop//out6.txt", "w", stdout);
	cin >> testcase;
	arr[3][1][1] = 0;
	arr[3][1][2] = 0;
	arr[3][1][3] = 0;
	arr[3][1][4] = 0;
	arr[3][2][1] = 0;
	arr[3][2][2] = 0;
	arr[3][2][3] = 1;
	arr[3][2][4] = 0;
	arr[3][3][1] = 0;
	arr[3][3][2] = 1;
	arr[3][3][3] = 1;
	arr[3][3][4] = 1;
	arr[3][4][1] = 0;
	arr[3][4][2] = 0;
	arr[3][4][3] = 1;
	arr[3][4][4] = 0;
	arr[4][1][1] = 0;
	arr[4][1][2] = 0;
	arr[4][1][3] = 0;
	arr[4][1][4] = 0;
	arr[4][2][1] = 0;
	arr[4][2][2] = 0;
	arr[4][2][3] = 0;
	arr[4][2][4] = 0;
	arr[4][3][1] = 0;
	arr[4][3][2] = 0;
	arr[4][3][3] = 0;
	arr[4][3][4] = 1;
	arr[4][4][1] = 0;
	arr[4][4][2] = 0;
	arr[4][4][3] = 1;
	arr[4][4][4] = 1;
	for (test = 1; test <= testcase; test++)
	{
		cout << "Case #" << test << ": ";
		int i, j, k;

		int x, r, c;
		cin >> x >> r >> c;
		if (x == 1)
			cout << "GABRIEL";
		else if (x == 2)
		{
			if ((r*c) % 2 == 0)
				cout << "GABRIEL";
			else
				cout << "RICHARD";
		}
		else if (x == 3 || x == 4)
		{
			if (arr[x][r][c])
				cout << "GABRIEL";
			else
				cout << "RICHARD";
		}
		else
			cout << "RICHARD";

		cout << endl;
	}
	return 0;
}