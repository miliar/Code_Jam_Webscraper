#include <iostream>
#include "gmpxx.h"

typedef mpz_class big;

using namespace std;

big FindMaxRings(big r, big t);

int main()
{
    int numCases;
    cin >> numCases;
    for (int caseNum = 1; caseNum <= numCases; caseNum++)
    {
	big r;
	cin >> r;
	big t;
	cin >> t;
	cout << "Case #" << caseNum << ": " << FindMaxRings(r, t) << endl;
    }
}

big FindMaxRings(big r, big t)
{
    big numRings = 0;
	
    for (big i = r+1; ; i += 2)
    {
	t -= i*i - (i-1)*(i-1);
	if (t >= 0)
	{
	    numRings++;
	}
	else
	{
	    break;
	}
    }
    //cout << "Remainder: " << t << endl;
    return numRings;
}
