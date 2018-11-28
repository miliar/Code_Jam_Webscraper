#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int cs = 1; cs <= t; ++cs)
	{
		unsigned x, a, b; cin >> x >> a >> b;
		string winner, gabriel = "GABRIEL", richard = "RICHARD";

		if (x == 1)
		{
			winner = gabriel;
		}
		if (x == 2)
		{
			winner = gabriel;
			if (a % 2 && b % 2) winner = richard;
		
		}
		if (x == 3)
		{
			winner = gabriel;
			if (a < 3 && b < 3) winner = richard;
			if (a < 2 || b < 2) winner = richard;
			if (a == 4 && b == 4) winner = richard;
			if ((a*b) % 3) winner = richard;
		}
		if (x == 4)
		{
			winner = gabriel;
			if (a < 4 && b < 4) winner = richard;
			if (a < 3 || b < 3) winner = richard;
			if ((a == 3 && b == 4) || (a == 4 && b == 3)) winner = gabriel;
		}
		if ((a*b) % x) winner = richard;

		cout << "Case #" << cs << ": " << winner << "\n";
	}

	return 0;
}