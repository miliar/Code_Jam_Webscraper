#include "Prototypes.h"

void GoogleCodeJam::Y2015::Qualification::OminousOmino()
{
	unsigned int T;

	std::cin >> T;
	assert(T >= 1 && T <= 100);

	for (unsigned int a (1); a <= T; ++a)
	{
		unsigned int X, R, C;
		std::cin >> X >> R >> C;
		assert(X >= 1 && X <= 4);
		assert(R >= 1 && R <= 4);
		assert(C >= 1 && C <= 4);

		string winner;

		if (X == 1)
		{
			winner = "GABRIEL";
		}
		else if (X == 2)
		{
			if ((R * C) % 2 == 1)
				winner = "RICHARD";
			else
				winner = "GABRIEL";
		}
		else if (X == 3)
		{
			if (R * C <= 4 || R * C % 3)
				winner = "RICHARD";
			else
				winner = "GABRIEL";
		}
		else
		{
			if (R * C <= 9 || R * C % 4)
				winner = "RICHARD";
			else
				winner = "GABRIEL";
		}

		std::cout << "Case #" << a << ": " << winner << std::endl;
	}
}