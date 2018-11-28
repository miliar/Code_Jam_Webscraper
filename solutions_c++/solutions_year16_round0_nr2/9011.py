// Test.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
using namespace std;


struct Item
{
	int carId;
	bool left;	
	int speed;
	int position;
};

int _tmain(int argc, _TCHAR* argv[])
{	
	/*std::vector<Item> input;
	std::vector<std::vector<Item>> cases;*/

	string input;
	std::vector<string> cases;

	char *inname = "C:/Test/Debug/A-small.in";
    ifstream infile(inname);

	if (!infile) {
        cout << "There was a problem opening file "
             << inname
             << " for reading."
             << endl;
        return 0;
    }

	cout << "Opened " << inname << " for reading." << endl;

	int numCases;

    infile >> numCases;
    cout << "Num of cases is " << numCases << endl;
	getline(infile, input);//dummy
	for (int i=0; i<numCases; i++)
	{
		getline (infile, input);
		cases.push_back(input);
	}

	FILE * pFile;
    pFile = fopen ("out.txt","w+");

	for (int i=0; i<numCases; i++)
	{	
		input = cases[i];
		int res = 0;
		for (int j = 0; j < input.length()-1; j++)
		{
			if (input[j] != input[j + 1])
				res++;
		}
		if (input[input.length()-1] == '-')
			res++;
		fprintf (pFile, "Case #%d: %d\n",i+1,res);
	}
	fclose (pFile);
	
	return 0;
}

