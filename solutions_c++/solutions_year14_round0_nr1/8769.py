
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

#define ROWS_COUNT 4
#define ELEMENT_COUNT 4

int getIntFromFile(ifstream &input);
string getRowFromArrangement (ifstream &input, int index);
std::vector<int> stringToVect (string str);
void printVect (std::vector <int> v);
void doTheMagic (std::vector<int> lhs, std::vector<int> rhs, ofstream &output);

int main () {
	ifstream input;
	input.open ("A-small-attempt1.in.txt");
	if (!input.is_open()) {
		return 1;
	}
	int testsCount = getIntFromFile(input);
	ofstream output;
	output.open("A_small_res1.txt");

	for (int i = 0; i < testsCount; ++i) {
		int firstAnswer = getIntFromFile(input);
		string firstRow = getRowFromArrangement(input, firstAnswer);
		
		int secondAnswer = getIntFromFile(input);
		string secondRow = getRowFromArrangement(input, secondAnswer);

		//printf("Case #%d: ", i+1);
		output << "Case #" << i+1 << ": ";
		doTheMagic(stringToVect(firstRow), stringToVect(secondRow), output);
		// printf("\n");
		output << "\n";
	}

	input.close();

	return 0;
}

int getIntFromFile(ifstream &input) {
	string answer;
	getline (input, answer);
	return stoi(answer);
	return 0;
}

string getRowFromArrangement (ifstream &input, int index) {
	string resultRow = "";
	for (int i = 1; i <= ROWS_COUNT; ++i) {
		if (!input.is_open()) {
			printf("File not open\n");
			return "";
		}
		string currentRow = "";
		if (i == index) {
			getline (input, resultRow);
		} else {
			getline(input, currentRow);
		}
		
	}
	return resultRow;
}

void doTheMagic (std::vector<int> lhs, std::vector<int> rhs, ofstream &output) {


	bool foundCommonEl = false;
	int chosenCard = -1;
	for (std::vector<int>::iterator i = lhs.begin(); i < lhs.end(); ++i) {
		if (find (rhs.begin(), rhs.end(), *i) != rhs.end()) {
			if (!foundCommonEl) {
				foundCommonEl = true;
				chosenCard = *i;	
			} else {
				//printf("Bad magician!");
				output << "Bad magician!";
				return;
			}
		}
	}
	if (!foundCommonEl) {
		//printf("Volunteer cheated!");
		output << "Volunteer cheated!";
	} else {
		//printf("%d", chosenCard);
		output << chosenCard;
	}
}

std::vector<int> stringToVect (string str) {
	std::istringstream iss (str.c_str());
	std::vector<int> resultVect;

	for (int i = 0; i < ELEMENT_COUNT; ++i) {
		int val;
		iss >> val;
		resultVect.push_back(val);
	}
	return resultVect;
}

void printVect (std::vector <int> v) {
	for (std::vector<int>::iterator i = v.begin(); i < v.end(); ++i) {
		printf("%d; ", *i);
	}
	printf("\n");
}
