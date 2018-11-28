#include <iostream>
#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <iomanip>

using namespace std;

int main()
{
	cout << "Enter name of input file: ";
	string infilename;
	cin >> infilename;
	ifstream infile(infilename.c_str());

	cout << "Enter name of output file: ";
	string outfilename;
	cin >> outfilename;
	ofstream outfile(outfilename.c_str());
	
	
	int numCase;
	double cost, farmrate, X;
	int farms;
	double rate;
	double cookies;
	double totalTime;
	double bestTimeToX;
	double timeToFarms;
	double testTime;
	
	infile >> numCase;
	cout << setprecision( 13 );
	outfile << setprecision(13);
	for (int i = 1; i <= numCase; i++)
	{
		infile >> cost >> farmrate >> X;
		timeToFarms = 0;
		rate = 2;
		bestTimeToX = X/rate;
		//cout << bestTimeToX <<endl;
		
		while(true)
		{
			timeToFarms = timeToFarms + cost/rate;
			testTime = timeToFarms + X/(rate + farmrate);
			//cout << "testtime: " << testTime << endl;
			if (testTime < bestTimeToX )
			{
				bestTimeToX = testTime;
				rate = rate + farmrate;
			}
			
			else
				break;
			//cout << bestTimeToX <<endl;
		}
		
		
	
		
		
		outfile << "Case #" << i << ": " << bestTimeToX << endl;
	
	
	
	}
	
	
}
