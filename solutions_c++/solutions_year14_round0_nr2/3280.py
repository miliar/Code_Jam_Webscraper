// Google Code Jam
// Qualification round question 2
// Cookie Clicker
// --
// Compile line used: g++ q2.cpp -o q2.exe -std=c++11 -Wall -fpermissive

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char** argv)
{
	ifstream file_in;
	ofstream file_out;
	int num_problems;
	double C, F, X;

	double cps = 2.0;

	cout << fixed << showpoint;
	cout.precision(7);

	if(argc < 2)
	{
		cout << "Argument required: input file" << endl;
		return 1;
	}

	file_in.open(argv[1], ios::in);
	if(!file_in.is_open())
	{
		cerr << "Error opening file '" << argv[1] << "' for reading." << endl;
		return 2;
	}

	// Open output file
	file_out.open("output.txt", ios::out);
	if(!file_out.is_open())
	{
		cerr << "Error opening output file!" << endl;
		return 3;
	}

	file_out << fixed << showpoint;
	file_out.precision(7);

	// Ready to read problem set
	file_in >> num_problems;

	cout << "Number of problems: " << num_problems << endl;

	for(int i = 0; i < num_problems; i++)
	{
		file_in >> C >> F >> X;
		cps = 2.0;

		cout << "Cost of cookie farm: " << C << endl;
		cout << "Extra cookies per second per farm: " << F << endl;
		cout << "Goal: " << X << endl << endl;
	
		bool done = false;
		double stx = X/cps; // Seconds to X
		double acc = 0.0F;
		while(!done) 
		{
			// After a bit of working things out on paper,
			// we're basically working with a parabola.
			// Just need to find the 'lowest' point in 
			// the curve.

			double nstx = acc + (X/cps);
			if(nstx <= stx)
			{
				stx = nstx;
				acc += C/cps;
				cps += F;
			}
			else
			{
				done = true;
			}
			
		}

		cout << "It'll take " << stx << " seconds. " << endl;

		// Write output
		file_out << "Case #" << i+1 << ": " << stx << endl;
	}

	file_out.close();
	file_in.close();
	return 0;
}
