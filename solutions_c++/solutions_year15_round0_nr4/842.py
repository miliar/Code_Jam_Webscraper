#include <iostream>

int max(int a, int b)
{
	return a > b ? a : b;
}
int min(int a, int b)
{
	return a < b ? a : b;
}

using namespace std;

int main()
{
	int T; cin >> T;
	for (int t = 0; t < T; t++)
	{
		int X, R, C;
		cin >> X >> R >> C;

		bool richardWins = false;

		if (X >= 7)
		{
			richardWins = true;
			goto eval;
		}
		
		if ((X > R) && (X > C))
		{
			richardWins = true;
			goto eval;
		}

		if (((R * C) % X) != 0)
		{
			richardWins = true;
			goto eval;
		}

		if (min(R, C) < ((X + 1) / 2))
		{
			richardWins = true;
			goto eval;
		}

		if (X == 4 && (min(R, C) <= 2))
		{
			richardWins = true;
			goto eval;
		}

		if (X == 5 && (min(R, C) == 3 && max(R, C) == 5))
		{
			richardWins = true;
			goto eval;
		}

		if (X == 6 && (min(R, C) <= 3))
		{
			richardWins = true;
			goto eval;
		}

	eval:
		if (richardWins == true)
		{
			cout << "Case #" << t + 1 << ": RICHARD" << '\n';
		}
		else
		{
			cout << "Case #" << t + 1 << ": GABRIEL" << '\n';
		}
	}
}