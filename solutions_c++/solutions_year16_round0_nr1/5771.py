#include <iostream>
#include <algorithm>
#include <string>
#include <limits>
#include <unordered_set>
#include <cstring>
using namespace std;

void readInput();
class Solution {
private:
	unordered_set<int> seenNumbers;
public:
	long findLastNumber(int n) {
		if (n == 0)
			return -1;
		for (int i = 1; i <= 100; ++i) {
			string result = to_string(n * i);
			for (int pos = 0; pos < result.size(); ++pos) {
				seenNumbers.insert(stoi(result.substr(pos, 1)));
				if (seenNumbers.size() == 10)
					return stol(result);
			}
		}
		return -1;
	}
};
void readInput() {
	int t, n;
	cin >> t; 
	for (int i = 1; i <= t; ++i) {
		Solution s;
		cin >> n;  // read n
		long lastNumber = s.findLastNumber(n);
		if (lastNumber != -1)
			cout << "Case #" << i << ": " << lastNumber << endl;
		else
			cout << "Case #" << i << ": " << "INSOMNIA" << endl;
	}
}

int main(int argc, char *argv) {
	Solution s;
	readInput();
}