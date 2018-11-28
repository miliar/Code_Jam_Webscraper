#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <stdlib.h>
#include <vector>


using namespace std;



string function(string input);


int main() {
	ofstream fout("output.txt");
	ifstream file;
	file.open("A-large.in", ios::in);    // open file

	int T;  // number of test cases
	file >> T;


	for (int i = 1; i <= T; i++)
	{
		string input, output;
		file >> input;

		output = function(input);
		fout << "Case #" << i << ": " << output << endl;
	}


	fout.close();
	file.close();
	return 0;
}



string function(string input)
{
	vector <char> b;
	char cmp = 0;
	

	for each (char a in input)
	{
		if (a >= cmp)
		{
			cmp = a;
			b.insert(b.begin(), a);
		}
		else
		{
			b.push_back(a);
		}
	}

	string output(b.begin(), b.end());
	return output;
}

