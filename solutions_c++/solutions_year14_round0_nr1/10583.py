// MagicTrick.cpp : définit le point d'entrée pour l'application console.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <boost/algorithm/string.hpp>
#include <vector>

using namespace std;
using namespace boost;

int main() {
	int lineOne[4], lineTwo[4];
	int numberSamples = 0;
	int lineNumber = 0;
	//int candidates[4]; 
	int counter = 0;
	vector<string> numbers(4) ;
	vector<int> commonNumbers(0);

	string line;
	ifstream myfile("small.txt");


	ofstream out("output.txt");

	if (myfile.is_open())
	{
		getline(myfile, line);
		numberSamples = stoi(line, nullptr);

		for (int j = 0; j < numberSamples; j++){
			getline(myfile, line);
			lineNumber = stoi(line, nullptr);
			for (int k = 0; k < 4; k++){
				getline(myfile, line);
				if ((k + 1) == lineNumber){
					split(numbers, line, is_any_of(" "));
					for (int i = 0; i < 4; i++){
						lineOne[i] = stoi(numbers[i], nullptr, 10);
					}
				}
			}

			getline(myfile, line);
			lineNumber = stoi(line, nullptr);
			for (int k = 0; k < 4; k++){
				getline(myfile, line);
				if ((k + 1) == lineNumber){
					split(numbers, line, is_any_of(" "));
					for (int i = 0; i < 4; i++){
						lineTwo[i] = stoi(numbers[i], nullptr, 10);
					}
				}
			}
			for (int i = 0; i < 4; i++){
				bool isInBoth = false;
				for (int j = 0; j < 4; j++){
					if (lineTwo[j] == lineOne[i]){
						isInBoth = true;
					}
				}
				if (isInBoth){
					commonNumbers.push_back(lineOne[i]);
				}
			}
			out << "Case #" << (j + 1) << ": ";
			if (commonNumbers.size() == 1){
				out << commonNumbers[0];
			}
			else if (commonNumbers.size() == 0){
				out << "Volunteer cheated!";
			}
			else{
				out << "Bad magician!";
			}
			out << "\n";
			commonNumbers.clear();
		}
		myfile.close();
		out.close();
	}
	return 0;
}

