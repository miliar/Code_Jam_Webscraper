
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int a[4][4], b[4][4], a1, b1, i, j, k, t, t1, n;
	cin >> t;
	for (t1 = 1; t >= t1; t1++)
	{
		n = 0;
		cin >> a1;
		for (i = 0; i<4; i++)
			cin >> a[i][0] >> a[i][ 1] >> a[i][ 2] >> a[i][ 3];
		cin >> b1;
		for (i = 0; i<4; i++){
			cin >> b[i][0] >> b[i][ 1] >> b[i][2] >> b[i][ 3];
		}
		for (i = 0; i<4; i++)
		{
			for (j = 0; j<4; j++)
			{
				if (a[a1 - 1][i] == b[b1 - 1][j])
				{
					n++; k = a[a1 - 1][i];
					break;
				}
			}
		}
		cout << "Case #" << t1 << " ";
		switch (n)
		{
		case 0: cout << "Volunteer cheated!"; break;
		case 1: cout << k; break;
		default: cout << "Bad magician!";
		}
		cout << endl;
	}
	return 0;
}