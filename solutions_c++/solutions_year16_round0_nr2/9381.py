// Pancakes.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	int count = 0,cases;
	char last,tmp;
	string str;


	ifstream myfile;
	myfile.open("B-large.in");
	ofstream outputFile;
	outputFile.open("outputLarge.txt");
	if (myfile.is_open())
	{
		myfile >> cases;
		
		for (int j = 0; j < cases; ++j) {
			myfile >> str;
			count = 0;
			for (int i = 0; i < str.length(); ++i) {
				if (i == 0) {
					last = str.at(str.length() - 1);
					if (last == '-') count++;
				}
				else {
					tmp = str.at(str.length() - 1 - i);
					if (tmp != last) count++;
					last = tmp;
				}
			}

			outputFile << "Case #" + to_string(j + 1) + ": " + to_string(count) + "\n";
			cout <<  "Case #" + to_string(j+1)+ ": " + to_string(count) + "\n";
		}

		outputFile.close();
		myfile.close();
	}
	else cout << "Error file\n";

	
	


	int pause;
	cin >> pause;
    return 0;
}

