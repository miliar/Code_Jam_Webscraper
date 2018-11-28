// 2014.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <sstream>
#include <iterator>
#include <string>
#include <vector>
#include <set>

using namespace std;

class MagicTrick {
public:
	MagicTrick () {
		data1 = vector<vector<int> >(4, vector<int>());
		data2 = vector<vector<int> > (4, vector<int>());
	}
	void parseData() {
		string line;
		
		cin >> ans1;
		--ans1;
		getline(cin, line);
		for (int i = 0; i < 4; ++i) {
			getline(cin, line);
			istringstream iss(line);
			copy(istream_iterator<int>(iss), istream_iterator<int>(), back_inserter(data1[i]));
		}
		cin >> ans2;
		--ans2;
		getline(cin, line);
		for (int i = 0; i < 4; ++i) {
			getline(cin, line);
			istringstream iss(line);
			copy(istream_iterator<int>(iss), istream_iterator<int>(), back_inserter(data2[i]));
		}
	}

	string solve() {
		int foundVals = 0;
		int foundNum;

		set<int> vals;
		for (int i = 0; i < 4; ++i) {
			vals.insert(data1[ans1][i]);
		}

		for (int i = 0; i < 4; ++i) {
			int curVal = data2[ans2][i];
			if (vals.find(curVal) != vals.end()) {
				++foundVals;
				foundNum = curVal;
			}
		}

		if (foundVals == 0 ) 
			return "Volunteer cheated!";
		else if (foundVals > 1)
			return "Bad magician!";
		else {
			ostringstream oss;
			oss << foundNum;
			return oss.str();
		}
	}

private:
	vector<vector<int> > data1;
	vector<vector<int> > data2;
	int ans1;
	int ans2;
};

int main(int argc, char* argv[])
{	
	string line;
	int count;

	cin >> count;
	getline(cin, line);

	for (int i = 1; i <= count; ++i) {
		MagicTrick mt;
		mt.parseData(); 
		cout << "Case #" << i << ": " << mt.solve() << endl;
	}
	
	return 0;
}

