//============================================================================
// Name        : codejam_magician.cpp
// Author      : Al Young
// Version     :
// Copyright   : My stuff, handds off
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>      /* printf, fgets */
#include <stdlib.h>     /* atoi */
#include <sstream>
#include <vector>

using namespace std;


int main() {

	// Load in input file
	ifstream inputfile;
	ofstream outputfile;

	inputfile.open("A-small-attempt0.in", ifstream::in);
	outputfile.open("A-small-practice.out", ofstream::out);
	//	inputfile.open("C-large-practice.in", ifstream::in);

	if(!inputfile.is_open())
	{
		cout << "Unable to open ze file" << endl;
		return 0;
	}

	else
	{
		cout << "Input file successfully opened" << endl;
		string number_of_cases;
		getline(inputfile,number_of_cases);
		int cases = atoi(number_of_cases.c_str());
		cout << "Examining " << cases << " cases" << endl;

		for( int x = 0; x < cases; x++)
		{
			int  match = 0; 
			int num_matches = 0;

			for( int y = 0; y < 10; y++)
			{
				int first_line, second_line;
				int row[4];

				// Setup stuff
				string line;
				getline(inputfile,line);
				if(y==0)
				{
					first_line=atoi(line.c_str());
					cout << "first_line = " << first_line << endl;
				}
				if (y==5)
				{
					second_line=atoi(line.c_str());
					cout << "second_line = " << second_line << endl;
				}


				if(
						(y<5)
						&&
						(y==(first_line))
				)
				{
					stringstream long_string(line);
					int holder;
					int element = 0;

					while(1)
					{
						long_string >> holder;
						if(!long_string) break;
						row[element] = holder;
						element++;			
					}

				}

				else if (
						(y>5)
						&&
						(y==(5+second_line))
				)
				{

					stringstream long_string(line);
					int holder;
					int element = 0;

					while(1)
					{
						long_string >> holder;
						if(!long_string) break;
						for( int z = 0; z < 4; z++)
						{
							if(row[z]==holder)
							{
								num_matches++;
								match = holder;
							}
						}
					}
				}
			}
			if(num_matches==0)
			{
				outputfile << "Case #" << x+1 << ": Volunteer cheated!" << endl;
			}
			else if(num_matches==1)
			{
				outputfile << "Case #" << x+1 << ": " << match << endl;
			}
			else
			{
				outputfile << "Case #" << x+1 << ": Bad magician!" << endl;
			}
		}
	}









	cout << "!!!Hello World!!! It's a me" << endl; // prints !!!Hello World!!!
	return 0;
}
