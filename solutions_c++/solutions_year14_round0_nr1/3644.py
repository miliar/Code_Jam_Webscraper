#include<iostream>
using namespace std;
void main()
{
	int T, j, k;
	cin >> T;
	int a[4][4], b[4][4], A, B;
	for (int i = 1; i <= T; i++)
	{
		int count = 0;
		int index = -1;
		cin >> A;
		for (j = 0; j < 4; j++)
		for (k = 0; k < 4; k++)
			cin >> a[j][k];
		cin >> B;
		for (j = 0; j < 4; j++)
		for (k = 0; k < 4; k++)
			cin >> b[j][k];
		for (j = 0; j < 4; j++)
		for (k = 0; k < 4; k++)
		if (a[A - 1][j] == b[B - 1][k])
		{
			count++;
			index = j;
		}
		cout << "Case #" << i << ": ";
		if (count == 1)
			cout << a[A - 1][index];
		else if (count == 0)
			cout << "Volunteer cheated!";
		else
			cout << "Bad magician!";
		cout << endl;
	}
}