#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

const string abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

int main() {


	int testCases;
	cin >> testCases;
	for (int curTC = 1; curTC <= testCases; curTC++) {
		
		vector<pair<char, int>> senate;
		int partiesCount;
		int senateSize = 0;
		vector<string> instructions;
		cin >> partiesCount;
		for (int cP = 0; cP < partiesCount; cP++) {
			int pp;
			cin >> pp;
			senateSize += pp;
			senate.push_back(pair<char, int>(abc.at(cP), pp));
		}
		while (senateSize) {
			sort(senate.begin(), senate.end(), [](pair<char, int> p1, pair<char, int> p2){
				return p2.second < p1.second;
			});
			if (senate[0].second > 1 && (senateSize - 2) > (senate[1].second * 2)) {
				// cout << "i" << endl;
				senate[0].second -= 2;
				senateSize -= 2;
				instructions.push_back(string(2, senate[0].first));
			} else if (senate[1].second > 1 || (senate[1].second == 1 && senate[0].second == 1 && (senate.size() == 2 || !senate[2].second))) {
				// cout << "ii" << endl;
				senate[0].second--;
				senate[1].second--;
				senateSize -= 2;
				instructions.push_back(string({senate[0].first, senate[1].first}));
			} else {
				// cout << "iii" << endl;
				senate[0].second--;
				senateSize--;
				instructions.push_back(string({senate[0].first}));
			}
		}
		cout << "Case #" << curTC << ":";
		for (auto inst : instructions) {
			cout << " " << inst;
		}
		cout << endl;
	}
	return 0;

}
