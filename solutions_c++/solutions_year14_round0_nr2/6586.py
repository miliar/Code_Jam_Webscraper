#include <iostream>
#include <stdlib.h>

using namespace std;

double farmIn(double cFarm, double cps)
{
	return (double)cFarm/cps;
}

int main()
{
	double sElapsed = 0.0; 
	double cTarget = 2000.0, cpsF = 4.0, cF = 500.0, cps = 2.0; 
	int testCase = 1, numTest = 0;

	cin >> numTest;
	cout.precision(7);
	cout.setf(ios::fixed, ios::floatfield);

	while(numTest > 0)
	{
		if(testCase != 1)
			cout << endl;

		cin >> cF >> cpsF >> cTarget;		
		//cout << "Read in: " << cF << " " << cpsF << " " << cTarget << endl;
		sElapsed = 0.0;
		cps = 2.0;
		while(1)
		{
			if((cTarget/cps) > (farmIn(cF, cps) + (cTarget/(cps + cpsF))))
			{
				sElapsed += farmIn(cF, cps);	
				cps += cpsF;
				//cout << "Elapsed; " << sElapsed << endl;
			}	
			else
				break;
		}
		sElapsed += cTarget/cps;
		
		cout << "Case #" << testCase << ": " << sElapsed;
		testCase++;
		numTest--;
	}
	return 0;
}

