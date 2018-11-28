/*
 * CountingSheep.cpp
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

class CountingSheepSolution
{
public:
	string countSheep(int N)
	{
		//TODO: get all the digits in i*N, then
		//put them in a Set,
		//then repeat with i = i + 1
		//where 1 <= i < infinity
		//Return the last N where seenDigits.size() == 10
		int i = 1;
		while (true) {
			if (N == 0) {
				return "INSOMNIA";
			}
			updateSeenDigits(getUniqueDigits(i * N));
			if (hasSeenAllDigits()) {
				break;
			}
			++i;
		}
		return to_string(i * N);
	}

	void clearSeenDigits() {
		seenDigits.clear();
	}
private:
	set<int> getUniqueDigits(int N)
	{
		//TODO: get all the digits in N
		// and put them in a Set
		set<int> ret;
		int num = N;
		while (num/10 > 0) {
			ret.insert(num%10);
			num /= 10;
		}
		ret.insert(num);
		return ret;
	}

	void updateSeenDigits(set<int> digits)
	{
		//put all the digits found into seenDigits set
		seenDigits.insert(digits.begin(), digits.end());
	}

	bool hasSeenAllDigits()
	{
		//TODO: checks whether all digits have been seen
//		for (auto i : seenDigits) {
//			cout << i << " ";
//		}
//		cout << endl;
		return seenDigits.size() == 10;
	}
private:
	set<int> seenDigits;
};

int main()
{
	CountingSheepSolution css;
//	vector<int> inputs = { 5, 0, 1, 2, 11, 1692 };
	vector<string> inputStrs;
	ifstream inFile("A-small-attempt1.in");
	string line;
	bool isFirstLine = true;
	while (getline(inFile, line)) {
		if (isFirstLine) {
			isFirstLine = false;
			continue;
		}
		inputStrs.push_back(line);
	}
	ofstream outputFile("out.txt");
	string newline = "\n";
	int caseNo = 1;
	for (auto in : inputStrs) {
		string out = "Case #" + to_string(caseNo) + ": " + css.countSheep(stoi(in));
//		cout << "Last number is " << out << endl;
		outputFile.write(out.c_str(), out.size());
		outputFile.write(newline.c_str(), newline.size());
		css.clearSeenDigits();
		++caseNo;
	}
	return 0;
}
