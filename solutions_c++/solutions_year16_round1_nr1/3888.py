/*
 * LastWordSolution.cpp
 *
 *  Created on: 16 Apr 2016
 *      Author: dmartana
 */




#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class LastWordSolution
{
public:
	string lastWord(string input)
	{
		string lastw = "";
		for (auto c : input) {
			if (lastw == "") lastw.push_back(c);
			else {
				if (lastw.at(0) <= c) {
					lastw = c + lastw;
				} else {
					lastw.push_back(c);
				}
			}
		}
		return lastw;
	}
};

int main()
{
	LastWordSolution lws;
//	vector<string> testCases = { "-", "-+", "+-", "+++", "--+-" };
	vector<string> inputStrs;
	ifstream inFile("inFile.in");
	string line;
	bool isFirstLine = true;
	while (getline(inFile, line)) {
		if (isFirstLine) { //ignore the "no of test cases"
			isFirstLine = false;
			continue;
		}
		inputStrs.push_back(line);
	}
	ofstream outputFile("out.txt");
	string newline = "\n";
	int i = 1;
	for (auto stack : inputStrs) {
		string out = "Case #" + to_string(i) + ": " + lws.lastWord(stack);
		outputFile.write(out.c_str(), out.size());
		outputFile.write(newline.c_str(), newline.size());
		++i;
	}
}
