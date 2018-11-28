#include <iostream>
#include <string>
#include <vector>

using namespace std;
class Solution {
public:
	int findMinFlipCount(string panCakeStack) {
		if (panCakeStack.size() == 0) {
			return 0;
		}
		vector<std::pair<int, int>> plusPairs;
		vector<std::pair<int, int>> minusPairs;
		int curPlusStart = -1;
		int curMinusStart = -1;
		int flipCount = 0;
		for (int pos = 0; pos < panCakeStack.size(); ++pos) {
			if (panCakeStack.substr(pos, 1) == "+") {
				if (curMinusStart != -1) {
					minusPairs.push_back(std::pair<int, int>(curMinusStart, pos - 1));
					curMinusStart = -1;
				}
				if (curPlusStart == -1) {
					curPlusStart = pos;
				}
			}
			else {
				if (curPlusStart != -1) {
					plusPairs.push_back(std::pair<int, int>(curPlusStart, pos - 1));
					curPlusStart = -1;
				}
				if (curMinusStart == -1) {
					curMinusStart = pos;
				}
			}
		}
		if (curPlusStart != -1) {
			plusPairs.push_back(std::pair<int, int>(curPlusStart, panCakeStack.size()-1));
			curPlusStart = -1;
		}
		else if (curMinusStart != -1) {
			minusPairs.push_back(std::pair<int, int>(curMinusStart, panCakeStack.size()-1));
			curMinusStart = -1;
		}
		if (plusPairs.size() == 0) {
			flipCount++;
			return flipCount;
		}
		while (minusPairs.size() != 0) {
			while (plusPairs.size() > 0 && minusPairs[minusPairs.size() - 1].second < plusPairs[plusPairs.size() - 1].first) {
				plusPairs.erase(plusPairs.begin() + (plusPairs.size() - 1));
			}
			if (plusPairs.size() != 0 && plusPairs.begin()->first == 0) {
				flipCount++;
				minusPairs.insert(minusPairs.begin(), std::pair<int, int>(plusPairs.begin()->first, plusPairs.begin()->second));
				plusPairs.erase(plusPairs.begin());
			}
			if (plusPairs.size() == 0)
			{
				return ++flipCount;
			}
			flipCount++;
			flipPancakes(plusPairs, minusPairs);
		}
		return flipCount;
	}
	void flipPancakes(vector<std::pair<int, int>> &plusPairs, vector<std::pair<int, int>> &minusPairs) {
		int end = minusPairs[minusPairs.size() - 1].second;
		vector<std::pair<int, int>> newPlusPairs;
		vector<std::pair<int, int>> newMinusPairs;
		for (auto rit = plusPairs.crbegin(); rit != plusPairs.crend(); ++rit) {
			newMinusPairs.push_back(std::pair<int, int>(end - rit->second, end - rit->first));
		}
		for (auto rit = minusPairs.crbegin(); rit != minusPairs.crend(); ++rit) {
			newPlusPairs.push_back(std::pair<int, int>(end - rit->second, end - rit->first));
		}
		plusPairs.swap(newPlusPairs);
		minusPairs.swap(newMinusPairs);
		return;
	}
};
void readInput() {
	int t;
	string panCakeStack;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		Solution s;
		cin >> panCakeStack;  // read n
		cout << "Case #" << i << ": " << s.findMinFlipCount(panCakeStack) << endl;
	}
}
int main(int argc, char *argv[]) {
	readInput();
}