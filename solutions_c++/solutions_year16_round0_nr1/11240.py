// Author: Ramya Bhaskar
// 	for Google Code Jam 2016
// g++ -o sheep sheep.cpp
#include <fstream>
#include <iostream>
// #include <cstdlib>
// #include <cstring>
#include <stdlib.h>
#include <math.h>
// #include <typeinfo>
#include <string>
#include <stdio.h>
// #include <iomanip>
#include <sstream>

using namespace std;

int main(){

	string line;
	int T;
	int N;

	ifstream inputfile; 
	inputfile.open("A-large.in");
	
	ofstream outputfile;
	outputfile.open("result2.txt");

	getline(inputfile,line);
	// T = atoi(line.c_str());
	int filelines = 1;
	while (getline(inputfile, line)){
		 
		// cout << line << endl;
		if (line[0] == '0')
			{
				// cout << "Case #" << filelines <<  ": INSOMNIA" << endl;
				outputfile << "Case #" << filelines <<  ": INSOMNIA" << endl;
			}

		else {
			// cout << line << " ";
			string lineHold = line;

			int nc0 = 0;
			int nc1 = 0;
			int nc2 = 0;
			int nc3 = 0;
			int nc4 = 0;
			int nc5 = 0;
			int nc6 = 0;
			int nc7 = 0;
			int nc8 = 0;
			int nc9 = 0;
			int not10 = true;
			int mult = 2;

			while (not10){

				int i = 0;
				while (line[i]){

					if (line[i] == '0' && nc0 < 1)
					{
						// cout << line[i] << " " ;
						nc0 += 1; 
						// cout << "|"<< nc0 << "| ";
					}
					else if (line[i] == '1' && nc1 < 1)
					{
						// cout << line[i] << " " ;
						nc1+= 1; 
						// cout << "|"<< nc1 << "| ";
					}
					else if (line[i] == '2' && nc2 < 1)
					{
						// cout << line[i] << " " ;
						nc2+= 1; 
						// cout << "|"<< nc2 << "| ";
					}
					else if (line[i] == '3' && nc3 < 1)
					{
						// cout << line[i] << " " ;
						nc3+= 1; 
						// cout << "|"<< nc3 << "| ";
					}
					else if (line[i] == '4' && nc4 < 1)
					{
						// cout << line[i] << " " ;
						nc4+= 1; 
						// cout << "|"<< nc4 << "| ";
					}
					else if (line[i] == '5' && nc5 < 1)
					{
						// cout << line[i] << " " ;
						nc5+= 1;
						// cout << "|"<< nc5 << "| "; 
					}
					else if (line[i] == '6' && nc6 < 1)
					{
						// cout << line[i] << " " ;
						nc6+= 1;
						// cout << "|"<< nc6 << "| ";
					}
					else if (line[i] == '7' && nc7 < 1)
					{
						// cout << line[i] << " " ;
						nc7+= 1; 
						// cout << "|"<< nc7 << "| ";
					}					
					else if (line[i] == '8' && nc8 < 1)
					{
						// cout << line[i] << " " ;
						nc8+= 1; 
						// cout << "|"<< nc8 << "| ";
					}
					else if (line[i] == '9' && nc9 < 1)
					{
						// cout << line[i] << " " ;
						nc9+= 1; 
						// cout << "|"<< nc9 << "| ";
					}
					i++; 
				} // end while; ran through number by digit

				if ((nc0 + nc1 + nc2 + nc3 + nc4 + nc5 + nc6 + nc7 + nc8 + nc9) == 10)
				// if (nc2 == 1)
				{
					not10 = false;
					// cout << " *10* ";
				}
				else
				{
					int num  = atoi(lineHold.c_str());
					// cout << "|"<< num << "| -" << mult << "- ";
					num  *= mult;
					mult += 1; 

					// cout << num << " ";
					// go back from int to string
					ostringstream convert;
					convert << num;
					line  = convert.str();
				}

			} // end while

			// cout << "Case #" << filelines << ": "<<  line << endl;
			outputfile << "Case #" << filelines << ": "<<  line << endl;
		} // end else statement

		filelines += 1;

	} // end outer while




	inputfile.close();
	return 0;
} // main