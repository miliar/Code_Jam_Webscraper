#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <climits>
#include <algorithm>


using namespace std;

vector<string> input;
vector<string> output;

void readInFile() {
	string line;
	bool isFirstLine = true;
	ifstream myfile("B-large.in");
	if (myfile.is_open())
	{
		while (getline(myfile, line))
		{
			if (isFirstLine) {
				isFirstLine = false;
			}
			else {
				input.push_back(line);
			}
		}
		myfile.close();
	}
}

string flip(string bit) {
	string flipped = "";
	string final_result = "";
	for (int i = bit.length() - 1; i >= 0; i--) {
		flipped += bit[i];
	}
	for (int j = 0; j < flipped.length(); j++) {
		if (flipped[j] ==  '-') {
			final_result += "+";
		}
		else {
			final_result += "-";
		}
	}
	return final_result;
}

bool isSolved(string problem) {
	bool isSolved = true;
	for (int i = 0; i < problem.length(); i++) {
		isSolved = isSolved && (problem[i] == '+');
	}
	return isSolved;
}

void outputAnswer() {
	ofstream myfile("angry.out");
	if (myfile.is_open())
	{
		for (int i = 0; i < output.size(); i++) {
			myfile << "Case #" + to_string(i + 1) + ": " + (output[i]) + "\n";
		}
		myfile.close();
	}
}

int main() {
	readInFile();

	for (int i = 0; i < input.size(); i++) {
		string problem = input[i];
		int moves = 0;
		while (!isSolved(problem)) {
			int pancakes_to_flip = -1;
			char top_pancake = problem[0];
			for (int j = 0; j < problem.size(); j++) {
				if (problem[j] != top_pancake) {
					pancakes_to_flip = j;
					break;
				}
			}
			if (pancakes_to_flip == -1) {
				pancakes_to_flip = problem.length();
			}
			problem = flip(problem.substr(0, pancakes_to_flip)) + problem.substr(pancakes_to_flip);
			moves++;
		}
		output.push_back(to_string(moves));
	}
	
	outputAnswer();
}