#include <iostream>
#include <string>
using namespace std;
int main()
{
	int T;
	int X, R, C;
	cin >> T;
	for (int k = 0; k < T; ++k)
	{
		cin >> X >> R >> C;
		cout << "Case #" << (k + 1) << ": ";
		if ((R * C) % X != 0)
		{
			cout << "RICHARD" << endl;
			continue;
		}
		if (X == 1)
		{
			cout << "GABRIEL" << endl;
		}
		else if (X == 2)
		{
			cout << "GABRIEL" << endl;
		}
		else if (X == 3)
		{
			if (R == 1 || C == 1)
			{
				cout << "RICHARD" << endl;
			}
			else
			{
				cout << "GABRIEL" << endl;
			}
		}
		else
		{
			if (R <= 2 || C <= 2)
			{
				cout << "RICHARD" << endl;
			}
			else
			{
				cout << "GABRIEL" << endl;
			}
		}
	}
	return 0;
}