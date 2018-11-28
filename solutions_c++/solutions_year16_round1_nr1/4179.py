//
// Created by Nguyen Hoang Kha on 4/16/16.
//

//--------------------------------------------------------------------------------------------------------------------------------------
// Constants

//--------------------------------------------------------------------------------------------------------------------------------------
// Include

#include <iostream>
#include <string>
#include <fstream>
#include <stack>

using namespace std;

//--------------------------------------------------------------------------------------------------------------------------------------
// Variables
string p;
stack<int> lowS;
stack<int> highS;
stack<int> modeS;

//--------------------------------------------------------------------------------------------------------------------------------------
// Functions

void xuly(void);
int maxLetter(int i, int j);
int splitP();

//--------------------------------------------------------------------------------------------------------------------------------------
// Main programs

int main() {
	ifstream in("/Users/user/Desktop/in.txt");
	streambuf *cinbuf = std::cin.rdbuf();
	cin.rdbuf(in.rdbuf());

	ofstream out("/Users/user/Desktop/out.txt");
	streambuf *coutbuf = std::cout.rdbuf();
	cout.rdbuf(out.rdbuf());
	xuly();
	return 0;
}

//--------------------------------------------------------------------------------------------------------------------------------------
// Solution

void xuly() {
	int T;

    cin >> T;

	for (int i = 1; i <= T; i++) {
		cin >> p;
		int lenp = p.size();
		if (lenp > 0) {

			lowS.push(0);
			highS.push(lenp - 1);
			modeS.push(0);

			cout << "Case #" << i << ": ";

			while (lowS.size() > 0) {
				int maxK = splitP();

				if (maxK >= 0) {
					cout << p[maxK];
				}

				int low = lowS.top();
				int high = highS.top();

				lowS.pop();
				highS.pop();
				modeS.pop();

				if (maxK < high) {
					lowS.push(maxK + 1);
					highS.push(high);
					modeS.push(1);
				}

				if (maxK > low) {
					lowS.push(low);
					highS.push(maxK - 1);
					modeS.push(0);
				}
			}

			cout << endl;
		}
	}
}

int maxLetter(int i, int j) {
	int max = 'A' - 1;
	int maxK = -1;
	for (int k = i; k <= j; k++) {
		if (p[k] >= max) {
			max = p[k];
			maxK = k;
		}
	}
	return maxK;
}

int splitP() {
	if (lowS.size() == 0) {
		return -1; // Print result;
	}

	int low = lowS.top();
	int high = highS.top();
	int s = modeS.top();

	int m;

	if (s == 0) {
		m = maxLetter(low, high);
	} else {
		m = low;
	}

	return m;
}

