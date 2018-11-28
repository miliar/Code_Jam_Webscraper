// gettingTheDigits.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define zero 'Z'
#define four 'U'
#define two 'W'
#define six 'X'
#define eight 'G'
#define seven 'S'
#define five 'V'
#define three 'H'
#define nine 'I'
#define one 'E'

int main()
{
	int numCases = 0;

	cin >> numCases;

	for (int i = 0; i < numCases; i++)
	{
		// get input
		string input;
		cin >> input;

		vector<int> output;

		// series of loops to find digits
		while (input.find(zero) != string::npos) {	
			input = input.erase(input.find('Z'), 1);
			input = input.erase(input.find('E'), 1);
			input = input.erase(input.find('R'), 1);
			input = input.erase(input.find('O'), 1);

			output.push_back(0);
		};

		while (input.find(four) != string::npos) {
			input = input.erase(input.find('F'), 1);
			input = input.erase(input.find('O'), 1);
			input = input.erase(input.find('U'), 1);
			input = input.erase(input.find('R'), 1);

			output.push_back(4);
		};
		
		while (input.find(two) != string::npos) {
			input = input.erase(input.find('T'), 1);
			input = input.erase(input.find('W'), 1);
			input = input.erase(input.find('O'), 1);

			output.push_back(2);
		};

		while (input.find(six) != string::npos) {
			input = input.erase(input.find('S'), 1);
			input = input.erase(input.find('I'), 1);
			input = input.erase(input.find('X'), 1);

			output.push_back(6);
		};
		
		while (input.find(eight) != string::npos) {
			input = input.erase(input.find('E'), 1);
			input = input.erase(input.find('I'), 1);
			input = input.erase(input.find('G'), 1);
			input = input.erase(input.find('H'), 1);
			input = input.erase(input.find('T'), 1);

			output.push_back(8);
		};
		
		while (input.find(seven) != string::npos) {
			input = input.erase(input.find('S'), 1);
			input = input.erase(input.find('E'), 1);
			input = input.erase(input.find('V'), 1);
			input = input.erase(input.find('E'), 1);
			input = input.erase(input.find('N'), 1);

			output.push_back(7);
		};
		
		while (input.find(five) != string::npos) {
			input = input.erase(input.find('F'), 1);
			input = input.erase(input.find('I'), 1);
			input = input.erase(input.find('V'), 1);
			input = input.erase(input.find('E'), 1);

			output.push_back(5);
		};
		
		while (input.find(three) != string::npos) {
			input = input.erase(input.find('T'), 1);
			input = input.erase(input.find('H'), 1);
			input = input.erase(input.find('R'), 1);
			input = input.erase(input.find('E'), 1);
			input = input.erase(input.find('E'), 1);

			output.push_back(3);
		};
		
		while (input.find(nine) != string::npos) {
			input = input.erase(input.find('N'), 1);
			input = input.erase(input.find('I'), 1);
			input = input.erase(input.find('N'), 1);
			input = input.erase(input.find('E'), 1);

			output.push_back(9);
		};
		
		while (input.find(one) != string::npos) {
			input = input.erase(input.find('O'), 1);
			input = input.erase(input.find('N'), 1);
			input = input.erase(input.find('E'), 1);
			
			output.push_back(1);
		};

		// order
		sort(output.begin(), output.end());

		// output
		cout << "Case #" << i+1 << ": ";
		
		for (unsigned int i = 0; i < output.size(); i++)
		{
			cout << output[i];
		}

		cout << endl;
	}

    return 0;
}



