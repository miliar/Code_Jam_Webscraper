#include <iostream>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <sstream>

using namespace std;

void solve(); 

int main() {
	int nCases;
	cin >> nCases;
	for (int i = 0; i < nCases; i++) {
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}

int ctoi(char c) {
	return c - '0';
}

void solve() {
	int sMax;
	char buf[1024];
	cin >> sMax;
	cin.get(); // eat initial space
	cin.getline(buf, 1024);
	
	vector<int> digits;
	for (char* p = buf; *p != '\0'; p++) {
		digits.push_back(ctoi(*p));
	}
	
	int sumSoFar = 0;
	int friends = 0;
	for (int i = 0; i < digits.size(); i++) {
		if (sumSoFar < i) {
			int newFriends = i - sumSoFar;
			sumSoFar += newFriends;
			friends += newFriends;
		}
		sumSoFar += digits[i];
	}
	
	cout << friends << endl;
}