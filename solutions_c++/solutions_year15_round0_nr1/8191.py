//============================================================================
// Name        : standing_ovation.cpp
// Author      : Jose Lorente
// Version     :
// Copyright   : Jose Lorente
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int getTestCases();

class FriendFinder {
	int n;
	string data;

public:
	FriendFinder();
	int getResult();
};

int main() {
	int tCases, i = 0;
	cin >> tCases;

	while (i++ < tCases) {
		FriendFinder fFinder;
		cout << "Case #" << i << ": " << fFinder.getResult() << endl;
	}
}

FriendFinder::FriendFinder() {
	cin >> n;
	cin >> data;
}

int FriendFinder::getResult() {
	int sTotal = 0;
	int friends = 0;
	for (int i = 0; i <= n; i++) {
		stringstream str;
		int s;
		str << data[i];
		str >> s;
		if (sTotal < i) {
			int add = i - sTotal;
			friends += add;
			sTotal += add;
		}
		sTotal += s;
	}
	return friends;
}
