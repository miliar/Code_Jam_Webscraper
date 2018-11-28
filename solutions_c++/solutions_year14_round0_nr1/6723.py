#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int c[5][4], m[17];
	int t, i, j, a1, k, a2, b, bc;
	cin >> t;
	for (i = 1; i <= t; i++)
	{
		bc = 0;
		for (j = 1; j <= 16; j++)
			m[j] = 0;
		cin >> a1;
		for (j = 1; j <= 4; j++)
		for (k = 0; k < 4; k++)
			cin >> c[j][k];
		for (j = 0; j < 4; j++)
			m[c[a1][j]]++;
		cin >> a2;
		for (j = 1; j <= 4; j++)
		for (k = 0; k < 4; k++)
			cin >> c[j][k];
		for (j = 0; j < 4; j++)
			m[c[a2][j]]++;
		for (j = 1; j <= 16; j++)
		if (m[j] == 2)
		{
			b = j;
			bc++;
		}
		if (bc == 0)
			cout << "Case #" << i << ": " << "Volunteer cheated!" << endl;
		else if (bc == 1)
			cout << "Case #" << i << ": " << b << endl;
		else
			cout << "Case #" << i << ": " << "Bad magician!" << endl;
	}
	return 0;
}