// practice.cpp : Defines the entry point for the console application.
//


#include <iostream>
#include <sstream>
#include <iterator>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <stdio.h>
#include <algorithm>
#include <deque>
#include <string>

using namespace std;

class SO {
private:
	int smax;
	string audience;

public:
	void parseData() {
		string line;

		cin >> smax;
		cin >> audience;
		getline(cin, line);
	}


	int solve() {
		vector<int> audCount(smax + 1, 0);
		int ind = 0;
		for (char c : audience)
			audCount[ind++] = c - '0';

		vector<int> audNow(smax + 1, 0);
		int extra = 0;

		if (audCount[0] == 0) {
			++extra;
			audNow[0] = 1;
		}
		else {
			audNow[0] = audCount[0];
		}
		for (int i = 1; i <= smax; ++i) {
			if (audNow[i - 1] >= i) {
				audNow[i] = audNow[i - 1] + audCount[i];
			}
			else {
				audNow[i] = i + audCount[i];
				extra += i - audNow[i - 1];
			}
		}
		return extra;
	}

};

int main(int argc, char* argv[])
{
	string line;
	int count;

	cin >> count;
	getline(cin, line);

	for (int i = 1; i <= count; ++i) {
		SO so;
		so.parseData();
		cout << "Case #" << i << ": " << so.solve() << endl;
	}
	return 0;
}

