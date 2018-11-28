// Pancakes.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int check[10];

bool arrayCheck() {

	for (int i = 0; i < 10; i++)
	{
		if (check[i] == 0) return true;
	}

	return false;
}

int main()
{
	int number, lastnum, tmpnum, cases;
	
	string str;


	ifstream myfile;
	myfile.open("A-large.in");
	ofstream outputFile;
	outputFile.open("outputLarge.txt");
	if (myfile.is_open())
	{
		myfile >> cases;
		int mult = 1;
		for (int j = 0; j < cases; ++j){
			myfile >> number;
			tmpnum = number;
			//cout << to_string(number) + " ";
			for (int y = 0;y<10;y++) {
				check[y] = 0;
			}
			mult = 1;
			while (arrayCheck()){
				
				lastnum = tmpnum;
				tmpnum = number * mult;

				if (lastnum == tmpnum && mult > 1) {
					tmpnum = -1;
					break;
				}

				string strnum = to_string(tmpnum);
				for (int i = 0; i < strnum.length();++i) {
					check[strnum.at(i) - '0']++;
				}
				mult++;
			}

			if (tmpnum < 0) {
				outputFile << "Case #" + to_string(j + 1) + ": " + "INSOMNIA\n";
				cout << "Case #" + to_string(j + 1) + ": " + "INSOMNIA\n";
			}
			else {
				outputFile << "Case #" + to_string(j + 1) + ": " + to_string(tmpnum) + "\n";
				cout << "Case #" + to_string(j + 1) + ": " + to_string(tmpnum) + "\n";
			}
		}

		outputFile.close();
		myfile.close();
	}
	else cout << "Error file\n";

	
	int pause;
	cin >> pause;
	return 0;
}


