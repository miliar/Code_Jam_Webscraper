#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<bitset>
using namespace std;

int main() {
	int testCases, origLength, complex, allowed;
	cin >> testCases;
	for (int i = 0; i < testCases; i++) {
		cin >> origLength >> complex >> allowed;
		vector<int> result;
		cout << "Case #" << i + 1 << ": ";
		if (allowed >= origLength) {
			for (int j = 0; j < allowed; j++)
				cout << j + 1 << " ";
		}
		else if (origLength > allowed)
			cout << "IMPOSSIBLE";
		cout << endl;

	}

}