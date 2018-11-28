/*
 * Solution.cpp
 *
 *  Created on: 8 May 2016
 *      Author: dmartana
 */


#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

map<int, string> partyNames {
	{0,"A"},
	{1,"B"},
	{2,"C"},
	{3,"D"},
	{4,"E"},
	{5,"F"},
	{6,"G"},
	{7,"H"},
	{8,"I"},
	{9,"J"},
	{10,"K"},
	{11,"L"},
	{12,"M"},
	{13,"N"},
	{14,"O"},
	{15,"P"},
	{16,"Q"},
	{17,"R"},
	{18,"S"},
	{19,"T"},
	{20,"U"},
	{21,"V"},
	{22,"W"},
	{23,"X"},
	{24,"Y"},
	{25,"Z"},
};

class Solution
{
public:
	vector<string> evacPlan(vector<int> senators_)
	{
		vector<int> senators = senators_;
		vector<string> plan;
		string evacd = "";
		int numOfSenators = 0;
		for (auto e : senators) {
			numOfSenators += e;
		}

		while (numOfSenators > 0) {
			//subtract from the part with the highest number
			vector<int>::iterator it = max_element(senators.begin(), senators.end());
			int index = distance(senators.begin(), it);
			senators[index] -= 1;
			evacd += partyNames[index];
			--numOfSenators;
			//subtract if any party has absolute majority
			for (unsigned i = 0; i < senators.size(); ++i) {
				if (senators.at(i) > numOfSenators / 2) {
					senators[i] -= 1;
					evacd += partyNames[i];
					--numOfSenators;
				}
				if (evacd.size() >= 2)
					break;
			}
			plan.push_back(evacd);
			evacd = "";
		}

		return plan;
	}
private:

};

namespace {
vector<string> parseInput(string line)
{
	cout << line << endl;
	vector<string> elems;
	istringstream iss(line);
	do {
		string e;
		iss >> e;
		elems.push_back(e);
	} while (iss);
	return elems;
}
}

int main()
{
	Solution solution;
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
	int lineNo = 0;
	int Case = 1;
	for (auto str : inputStrs) {
		if (lineNo%2 == 0) {
			++lineNo;
			continue;
		} else {
			vector<int> memberNums;
			vector<string> parsed = parseInput(str);
			for (auto c : parsed) {
				try {
					memberNums.push_back(stoi(c));
				} catch (...) {
				}
			}
			vector<string> plan = solution.evacPlan(memberNums);
			string planstr = "";
			for (auto e : plan) {
				planstr += e;
				planstr += " ";
			}
			string out = "Case #" + to_string(Case) + ": " + planstr;
			cout << out << endl;
			outputFile.write(out.c_str(), out.size());
			outputFile.write(newline.c_str(), newline.size());
		}
		++lineNo;
		++Case;
	}

}
