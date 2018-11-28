#include <iostream>
#include <string>

using namespace std;

int main() {
	unsigned numTests;
	string input;
	unsigned maxShyness;
	cin >> numTests;
	for (unsigned i = 0; i < numTests; i++) {
		unsigned counter = 0;
		unsigned minShyness = 0;
		cin >> maxShyness;
		cin >> input;
		for (unsigned p = 0; p <= maxShyness; p++) {
			if (minShyness < p) { // minimum shyness is too low for this group to stand up
				counter++;
				minShyness += 1;
			}
			minShyness += (input[p] - '0');
		}
		cout << "Case #" << i+1 << ": " << counter << "\n";
	}
	return 0;
}