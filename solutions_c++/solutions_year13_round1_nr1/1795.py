#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main()
{
	int numCase;
	cin >> numCase;
	long double r,t;

	ofstream myfile;
  	myfile.open ("output.txt");

	for (int num = 0; num < numCase; num++)
	{

		// Read dimensions
		cin >> r;
		cin >> t;
		
		 // The area for ring #i is given by pi((r+2i-1)²-(r+2i-2)²) and the analytical sum is given by
		// sum_{i=1}^{n} pi((r+2i-1)²-(r+2i-2)²) = pi (-n +2m² +2mr) < pi t
  		// which yields the solution

		long long int ans=floor(0.25*(1 - 2*r + sqrt(1 - 4*r + 4*r*r + 8*t) ));
		
		// Print outcome
		myfile << "Case #" << (num+1) << ": " << ans << endl;
	}

  	myfile.close();
	return 0;
}
