/*
 * RevengeOfThePie.cpp
 *
 *  Created on: 9 Apr 2016
 *      Author: dmartana
 */

#include <algorithm>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;

class RevengeOfThePancakeSolution
{
public:
	int makeAllHappy(string stack)
	{
		//TODO: executes the maneuvers in the smallest possible times
		count = 0;
		pancakeStack = stack;
		unsigned pos = 1;
		string happyStack(pancakeStack.size(), '+');

		//keep flipping until all are happy
		while (pancakeStack != happyStack) {
			while (pos < pancakeStack.size() && isTopSameAs(pos)) {
				++pos;
			}
			flip(pos - 1);
			++count;
			if (pos == pancakeStack.size()) {
				pos = 1;
			}
		}
		return count;
	}
private:
	bool isTopSameAs(int pos)
	{
		//TODO: check whether the top pancake is
		//showing the same face as the one at pos.
		//CAUTION: ensure the caller checks that pos is at most pancakeStack.size() - 1
		return pancakeStack.at(0) == pancakeStack.at(pos);
	}
	void flip(int from)
	{
		//TODO: flip the pancakes starting from from up to the top
		// and return the new stack (string)
		string temp = "";
		for (int i = from; i >= 0; --i) {
			temp.push_back(getFlippedSign(i));
		}
		pancakeStack.replace(0, from + 1, temp);
	}
	char getFlippedSign(int pos)
	{
		//TODO: flip the sign/face of the pancake at pos
		char sign = pancakeStack.at(pos);
		if (sign == '+') {
			return '-';
		} else {
			return '+';
		}
	}
private:
	string pancakeStack;
	int count;
};

int main()
{
	RevengeOfThePancakeSolution rtps;
//	vector<string> testCases = { "-", "-+", "+-", "+++", "--+-" };
	vector<string> inputStrs;
	ifstream inFile("A-small-attempt1.in");
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
		string out = "Case #" + to_string(i) + ": " + to_string(rtps.makeAllHappy(stack));
		outputFile.write(out.c_str(), out.size());
		outputFile.write(newline.c_str(), newline.size());
		++i;
	}
}
