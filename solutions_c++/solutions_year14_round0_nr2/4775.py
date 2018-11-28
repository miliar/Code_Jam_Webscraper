//============================================================================
// Name        : codejam_cookie.cpp
// Author      : Al Young
// Version     :
// Copyright   : My stuff, handds off
// Description : Hello World in C++, Ansi-style
//============================================================================
//The first line of the input gives the number of test cases, T. T lines follow. 
//Each line contains three space-separated real-valued numbers: C, F and X, whose
//meanings are described earlier in the problem statement.
//
//C, F and X will each consist of at least 1 digit followed by 1 decimal point 
//followed by from 1 to 5 digits. There will be no leading zeroes.


#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>      /* printf, fgets */
#include <stdlib.h>     /* atoi */
#include <sstream>
#include <vector>
#include <iomanip>

using namespace std;


int main() {
	std::cout << std::setprecision(7) << std::fixed;


	// Load in input file
	ifstream inputfile;
	ofstream outputfile;

	//	inputfile.open("A-small-attempt0.in", ifstream::in);
//		inputfile.open("A-small-practice.in", ifstream::in);
	inputfile.open("B-small-attempt1.in", ifstream::in);

//	outputfile.open("A-small-practice.out", ofstream::out);
	outputfile.open("B-small-attempt1.out", ofstream::out);
	outputfile<<setprecision(7) << fixed; 

	if(!inputfile.is_open())
	{
		cout << "Unable to open ze file" << endl;
		return 0;
	}

	else
	{
		//		cout << "Input file successfully opened" << endl;
		string number_of_cases;
		getline(inputfile,number_of_cases);
		int cases = atoi(number_of_cases.c_str());
		//		cout << "Examining " << cases << " cases" << endl;

		for( int x = 0; x < cases; x++)
		{
			// For each case 
			double CFX[3]; // C, F, X;
			double cookietime = 0;
			double next_cookietime = 0;
			int num_farms = 0;
			// Base rate remains the same
			double base_CR = 2;

			// Setup stuff
			string line;
			getline(inputfile,line);
			//			cout << line << endl;

			stringstream long_string(line);
			double holder;

			for( int y = 0; y < 3; y++)
			{
				long_string >> holder;
				CFX[y] = holder;
				//				cout << CFX[y] << endl;
			}

			while(1)
			{
				cookietime = 0;
				next_cookietime = 0;

				double CR, nextCR;
				CR = base_CR;
				nextCR = base_CR;

				for( int y = 0; y < num_farms; y++)
				{
					cookietime += CFX[0] / CR;
					CR += CFX[1];
				}
				cookietime += CFX[2]/CR;

				for( int y = 0; y < (num_farms+1); y++)
				{
					next_cookietime += CFX[0] / nextCR;
					nextCR += CFX[1];
				}
				next_cookietime += CFX[2]/nextCR;
				num_farms++;

				if(cookietime < next_cookietime)break;

			}
			//			while(cookietime>next_cookietime);

			outputfile << "Case #" << x+1 << ": " << cookietime << endl;
		}
	}


	cout << "!!!Hello Beautiful!!!" << endl; // prints !!!Hello World!!!
	return 0;
}
