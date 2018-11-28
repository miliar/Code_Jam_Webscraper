#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

int main()
{
	int num_cases = 0;
	int nomino = 0;
	int width = 0;
	int height = 0;
	bool possible = false;
	char grid[20][20];

	cin >> num_cases;

	for (int i = 0; i < num_cases; ++i)
	{
		cin >> nomino;
		cin >> width;
		cin >> height;

		// do algorithm
		if ((width * height) % nomino)
		{
			// early out if not divisible
			possible = false;
		}
		else if (width >= 3 && height >= 3 && nomino > 6)
		{
			// donut hole early out
			possible = false;
		}
		else if (nomino == 1)
		{
			// every thing is possible with 1
			possible = true;
		}
		else if (nomino == 2)
		{
			// everything that's divisible is possible with 2
			possible = true;
		}
		else if (nomino == 3)
		{
			if ((width == 3 && height == 1) || (width == 1 && height == 3))
			{
				possible = false;
			}
			else
			{
				possible = true;
			}
		}
		else if (nomino == 4)
		{
			if (((width == 3 && height == 4) || (width == 4 && height == 3)) || 
				(width == 4 && height == 4))
			{
				possible = true;
			}
		}

		cout << "Case #" << i + 1 << ": " << (possible ? "GABRIEL" : "RICHARD") << endl;

		nomino = 0;
		width = 0;
		height = 0;
		possible = false;
	}

 	return 0;
}
