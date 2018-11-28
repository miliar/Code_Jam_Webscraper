#include <iostream>

using namespace std;

int main()
{
	int nbCases;
	cin >> nbCases;
	for (int i = 0; i < nbCases; i ++)
	{
		int X, C, R;
		cin >> X >> C >> R;
		cout << "Case #" << i + 1 << ": ";
		cout << ((X < 7 && (C * R) % X == 0 && (C >= X || R >= X) && ((C >= X / 2 + 1 && R >= X / 2 + 1) || X <= 2)) ? "GABRIEL" : "RICHARD") << endl;
	}
}
