#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	string line;
	ifstream myfile ("test.txt");
	ofstream ofile;
	int numOfTestCases = 0;
	double cps = 2;
	double c,f,x;
	double best = 0;
	ofile.open("result.txt");
	ofile.precision(7);
	ofile.setf( std::ios::fixed, std:: ios::floatfield );
	if (myfile.is_open())
	{
		getline(myfile, line);
		numOfTestCases = atoi(line.c_str());
		for(int i = 0; i < numOfTestCases; i++)
		{	
			getline(myfile, line);
			std::istringstream is( line );
			double n;
			is >> c;
			is >> f;
			is >> x;
			//ofile << c << " " << f << " " << x << endl;
			while( ((c / cps) + (x/(cps+f))) < (x / cps) )
			{
				best += (c/cps);
				cps += f;
			}
			best += (x/cps);


			
			ofile << "Case #" << i + 1 << ": " << best;
			best = 0;
			cps = 2;
			ofile << endl;
		}
		myfile.close();
	}

	else cout << "Unable to open file"; 
	ofile.close();
	return 0;
}


