#include <fstream>
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

// This problem is attempted by calculating the possible values accros all possible iterations, that are the incremental smallest value for F
// which is 1.0 and then compute the corresponding value and compute it against the current minimum value.

#define DEFAULT_COCKIES_RATE	2.0L
#define EPSILON					0.000001L

int main()
{
	int				T, nCase = 1, nIter;
	long double		dblC, dblF, dblX, dblCurrentMin, dblPrevCost;
	ifstream		InFile("B-large.in");
	ofstream		OutFile("B-large.out", ios_base::ate || ios_base::out);

	if (OutFile.is_open())
	{
		InFile >> T;
		
		while (T--)
		{
			InFile >> dblC >> dblF >> dblX;
			
			OutFile << "Case #" << nCase++ << ": ";
			
			dblCurrentMin = dblX / DEFAULT_COCKIES_RATE;
			dblPrevCost = 0.0L;

			for (nIter = 1; nIter <= (unsigned int(dblX + 3.0L)) ; ++nIter)
			{
				dblPrevCost += (dblC / ((dblF * (long double)(nIter - 1)) + DEFAULT_COCKIES_RATE));

				if ((dblPrevCost + (dblX / ((dblF * (long double)(nIter)) + DEFAULT_COCKIES_RATE))) < dblCurrentMin)
					dblCurrentMin = (dblPrevCost + (dblX / ((dblF * (long double)(nIter)) + DEFAULT_COCKIES_RATE)));
			}
			
			OutFile << fixed;
			OutFile << setprecision(7) << dblCurrentMin << endl;
		}
	}

	return 0;
}