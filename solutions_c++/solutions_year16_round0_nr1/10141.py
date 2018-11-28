#include <iostream>
#include <string>
using namespace std;

int casenum;

void solve() {
	int number;

	bool seen[10];
	for (int i = 0; i < 10; i++) {
		seen[i] = false;
	}

	cin >> number;
	if (number == 0) {
		cout << "Case #" << casenum << ": INSOMNIA" << endl;
		return;
	}

	int ctr = 1;
	int numsolved = 0;
	string temp;
	while (true) {
		temp = to_string(ctr * number);
		for (int i = 0; i < temp.length(); i++) {
			if (seen[temp[i] - '0'] == false) {
				seen[temp[i] - '0'] = true;
				numsolved++;
				if (numsolved == 10) {
					cout << "Case #" << casenum << ": " << temp << endl;
					return;
				}
			}
		}
		ctr++;
	}
}

int main() {
	// your code goes here
	int numcases;
	cin >> numcases;

	for (casenum = 1; casenum <= numcases; casenum++) {
		solve();
	}

	return 0;
}
