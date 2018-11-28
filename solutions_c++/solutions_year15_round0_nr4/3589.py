#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	ifstream myfile;
	myfile.open("input.txt");
	
	ofstream ofile;
	ofile.open("output.txt");

	int total_cases = 0;

	myfile >> total_cases;

	int cas = 1;
	while (cas <= total_cases)
	{
		int x = 0, r = 0, c = 0;

		myfile >> x;
		
		myfile >> r;

		myfile >> c;


		if (x >= 7)
			ofile << "Case #" << cas++ << ": " << "RICHARD" << endl;

		else if ((r*c) % x == 0)
		{
			if (x - 1 <= r && x - 1 <= c)
				ofile << "Case #" << cas++ << ": " << "GABRIEL" << endl;
			else
				ofile << "Case #" << cas++ << ": " << "RICHARD" << endl;
		}

		else
			ofile << "Case #" << cas++ << ": " << "RICHARD" << endl;
	}


	return 0;
}