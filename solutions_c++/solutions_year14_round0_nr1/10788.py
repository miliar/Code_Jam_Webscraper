#include<iostream>
using namespace std;

int main ()
{
	//freopen ("in.txt", "r", stdin);
	//freopen ("out.txt", "w", stdout);
	int first[4][4], second[4][4];
	int cases, num1, num2, cntFound, res;
	cin >> cases;

	for (int t=1; t<= cases; t++)
	{
		cin >> num1; num1 --;
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++)
				cin >> first[i][j];

		cin >> num2; num2--;
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++)
				cin >> second [i][j];

		cntFound = 0;
		for (int i=0; i<4; i++)
		{
			for (int j=0; j<4; j++)
				if (first[num1][i] == second [num2][j])
				{
						cntFound++;
						res = first[num1][i];
				}
		}

		cout << "Case #" << t << ": ";
		if (cntFound == 1)
			cout << res << endl;
		else if (cntFound == 0)
			cout << "Volunteer cheated!\n";
		else
			cout << "Bad magician!\n";
	}
	return 0;
}