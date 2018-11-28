//============================================================================
// Name        : codejam_minesweeper.cpp
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
#include <iomanip>

using namespace std;


int main() {
	//	std::cout << std::setprecision(7) << std::fixed;


	// Load in input file
	ifstream inputfile;
	ofstream outputfile;

//	inputfile.open("D-small-attempt0.in", ifstream::in);
	inputfile.open("D-large.in", ifstream::in);
//	inputfile.open("A-small-practice.in", ifstream::in);

	//	outputfile.open("A-small-practice.out", ofstream::out);
//	outputfile.open("D-small-attempt0.out", ofstream::out);
	outputfile.open("D-large.out", ofstream::out);

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
			// Setup stuff
			string line;
			getline(inputfile,line);
			int NoB = atoi(line.c_str());
			//			cout << line << endl;

			float nomai[NoB][2];
			float ken[NoB][2];

			getline(inputfile,line);
			stringstream long_string(line);
			float holder;

			for(int y = 0; y < NoB; y++)
			{
				long_string >> holder;
				nomai[y][0] = holder;
				nomai[y][1] = 1;
				//				cout << nomai[y] << endl;
			}
			//Sort the values
			float temp;
			for (int passes = 0;  passes < NoB - 1;  passes++)
			{
				for (int j = 0;  j < NoB - passes - 1;  j++)
				{
					if (nomai[j][0] > nomai[j+1][0])
					{
						temp = nomai[j][0];
						nomai[j][0] = nomai[j+1][0];
						nomai[j + 1][0] =temp;
					}
				}
			}

			//						cout<<"nomai After Sorting :";
			//						for(int i=0; i < NoB;i++)
			//						{
			//							cout<<nomai[i][0]<<endl;
			//						}

			getline(inputfile,line);
			stringstream long_string2(line);
			for(int y = 0; y < NoB; y++)
			{
				long_string2 >> holder;
				ken[y][0] = holder;
				ken[y][1] = 1;
			}

			//Sort values
			for (int passes = 0;  passes < NoB - 1;  passes++)
			{
				for (int j = 0;  j < NoB - passes - 1;  j++)
				{
					if (ken[j][0] > ken[j+1][0])
					{
						temp = ken[j][0];
						ken[j][0] = ken[j+1][0];
						ken[j+1][0]=temp;

					}
				}
			}
			//			cout<<"Ken After Sorting :";
			//			for(int i=0; i < NoB;i++)
			//			{
			//				cout<< ken[i][0] << endl;
			//			}

			// Start calculating score here
			// War
			int WP = 0; 
			for(int round = 0; round < NoB; round++)
			{
				int selectorN;
				for(int scan = NoB-1; scan >= 0; scan--)
				{
					if(nomai[scan][1]==1)
					{
						selectorN = scan;
						break;
					}
				}

				nomai[selectorN][1] = 0;

				bool gta = true; 		// Greater than all
				for(int y = 0; y < NoB; y++)
				{
					if(
							(nomai[selectorN][0]<ken[y][0])
							&&
							(ken[y][1]==1)
					)
						//when ken has a log heavier than naomi's log
					{
						ken[y][1]=0;		// burn it
						gta=false;			
						break;
					}
				}
				if(gta)
				{
					WP++;
				}
			}
			// Decientful War
			int DWP = NoB;
			// Reset log availablity
			for(int y = 0; y < NoB; y++)
			{
				ken[y][1]=1;
				nomai[y][1]=1;
			}

			for(int round = 0; round < NoB; round++)
			{
				int select;
				//				// Pick the lightest available log
				for(int scan = 0; scan < NoB; scan++)
				{
					if(nomai[scan][1]==1)
					{
						select = scan;
						break;
					}
				}
				//				// No longer available
				nomai[select][1] = 0;
				//
				bool sta = true; 		// smaller than all
				//				// See if Ken has a smaller one
				for(int y = 0; y < NoB; y++)
				{
					if(
							(nomai[select][0]>ken[y][0])
							&&
							(ken[y][1]==1)
					)
						// when ken has a log lighter than naomi's log
					{
						ken[y][1]=0;		// burn it
						sta=false;			
						break;
					}
				}
				if(sta)
				{
					DWP--;
				}
			}


			outputfile << "case #" << x+1 << ": " << DWP << " " << WP << endl;
			cout << "case #" << x+1 << endl;
			//			break;
		}
	}

	cout << "!!!Hello Beautiful!!!" << endl; // prints !!!Hello World!!!
	return 0;
}
