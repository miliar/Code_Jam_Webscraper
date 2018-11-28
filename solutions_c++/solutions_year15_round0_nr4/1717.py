#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int nombre_tests;
	cin >> nombre_tests;
	for (int i = 0; i < nombre_tests; i++)
	{
		int X, R, C;
		cin >> X >> R >> C;

		int Mult = R * C;
		bool Res;	// Si Res vaut true, on affiche GABRIEL, sinon on affiche RICHARD
		if (X < Mult && (Mult % X) == 0)
			Res = (((R > (X / 2)) && (C > (X / 2))) || (X <= (max(R, C) - (X / 2))));
		else
			Res = (X == 1 && Mult == 1) || (X == 2 && Mult == 2);

		if (!Res)
			cout << "Case #" << i + 1 << ": RICHARD" << endl;
		else
			cout << "Case #" << i + 1 << ": GABRIEL" << endl;
	}

	return EXIT_SUCCESS;
}
