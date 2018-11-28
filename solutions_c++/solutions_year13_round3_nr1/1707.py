#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <fstream>
using namespace std;

#include <stdlib.h>

#include "hasConst.h"

int main()
{
	ifstream inFile("A-small-attempt0.in");
	ofstream outFile;
	outFile.open("results.txt");
	
	//Get the number of test cases
	string str;
	getline(inFile,str);
	int numberCases = atoi(str.c_str());
	
	//Main loop
	for(int z = 0;z < numberCases;z++)
	{
		getline(inFile,str);
		//Break into two
		istringstream iss(str);
		string testString;
		iss >> testString;
		string nValString;
		iss >> nValString;
		int nVal = atoi(nValString.c_str());
		
		//For each of the possible substring sizes
		//From max size to smallest
		
		int numberSubSeq = 0;
		
		for(int i = testString.size();i >= nVal;i--)
		{
			//Calculate the number of strings to test
			int toTest = testString.size() - i + 1;
			
			//Temporary string
			char *toCheck;
			toCheck = new char[i+1];
			toCheck[i] = '\0';
			
			//Try all the combinations
			for(int j = 0;j < toTest;j++)
			{
				//Assign the string
				for(int z = 0;z < i;z++)
				{
					toCheck[z] = testString.at(z+j);
				}
				
				string checkString(toCheck);
				
				//Find if has enough consequtive consonants
				bool enoughConstonants = hasConst(&checkString,nVal);
				
				if(enoughConstonants == true)
				{
					numberSubSeq++;
				}
			}
			
			//Clean up
			delete toCheck;
		}
		
		outFile << "Case #" << (z+1) << ": " << numberSubSeq << endl;
		cout << "Case #" << (z+1) << ": " << numberSubSeq << endl;
		
		//
		//cout << nVal << endl << testString << endl;
	}
	
	//Clean up
	inFile.close();
	outFile.close();

	return 0;
}