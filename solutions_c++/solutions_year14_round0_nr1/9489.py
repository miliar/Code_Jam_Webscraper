#include <iostream>
using namespace std;

void inputMatrix(int a[4][4])
{
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			cin >> a[i][j];
		}

	}
}

void printMatrix(int a[4][4])
{
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			cout << a[i][j] << ' ';
		}
		cout << endl;

	}
}



int main() 
{
	freopen("a.txt", "r", stdin);
	freopen("a.output", "w", stdout);
	int T, m, n;
	int a[4][4], b[4][4];

	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		cin >> m;
		inputMatrix(a);
		cin >> n;
		inputMatrix(b);

		/**
		 * do the algo
		 */
		int count = 0, number;
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				if (a[m-1][i] == b[n-1][j]) {
					count++;
					number = a[m-1][i];
				}
			}
		}
		switch (count) {
			case 0: cout << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl; break;
			case 1: cout << "Case #" << i+1 << ": " << number << endl; break;
			default: cout << "Case #" << i+1 << ": " << "Bad magician!" << endl;
		}

	}



	return 0;
}