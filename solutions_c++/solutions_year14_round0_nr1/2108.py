#include <iostream>

using namespace std;

#define FOUND 1
#define BADM 2
#define CHEAT 3

int T;
int m1[4][4], m2[4][4];
int r1, r2;

int main()
{
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		cin >> r1;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				cin >> m1[j][k];
		cin >> r2;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				cin >> m2[j][k];
		
		int count = 0;
		int val = 0;
		r1--;
		r2--;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				if (m1[r1][j] == m2[r2][k])
				{
					count++;
					val = m2[r2][k];
				}

		cout << "Case #" << i << ": ";
		if (count == 1)
			cout << val << endl;
		else if (count == 0)
			cout << "Volunteer cheated!" << endl;
		else
			cout << "Bad magician!" << endl;
	}
	return 0;
}
		