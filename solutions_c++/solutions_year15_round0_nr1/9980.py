#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;
int t;
int smax;
char shyness;
int stoodPeople;
int addedPeople;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> smax;
		stoodPeople = 0;
		addedPeople = 0;
		// load 0 second
		cin >> shyness;
		stoodPeople = shyness - '0';
		for (int j = 1; j <= smax; ++j) {
			cin >> shyness;
			if (j <= stoodPeople) {
				// just add those people
				stoodPeople = stoodPeople + shyness - '0';
			}
			else {
				// add more people up to j
				addedPeople = addedPeople + j - stoodPeople;
				stoodPeople = j + shyness - '0';
			}
		}

		cout << "Case #" << i << ": " << addedPeople << endl;
	}
	return 0;
}