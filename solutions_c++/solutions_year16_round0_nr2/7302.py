#include <iostream>
using namespace std;
int main() {
	int nTC = 0;
	cin >> nTC;
	for (int t = 1; t <= nTC; t++) {
		string input;
		cin >> input;
		char prev = input[0];
		int ns = 0;
		for (int i = 1; i < input.size(); i++) {
			if (input[i] != prev) {
				ns++;
				prev = input[i];
			}
		}
		if (prev == '-') {
			ns++;
		}
		cout << "Case #" << t << ": " << ns << endl;
	}
	return 0;
}
