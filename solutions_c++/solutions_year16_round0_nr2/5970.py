#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	int t;
	cin >> t;
	cin.ignore();
	for(int i = 1; i<=t; i++) {
		cout << "Case #" << i << ": ";
		string input;
		getline(cin, input);

		int flips = 0;
		for(int j = input.size()-1; j >= 0 ; j--) {
			//cout << input << endl;
			if (input[j] == '-') {
				flips++;
				for(int k = 0; k <= j; k++) {
					if (input[k] == '+')
						input[k] = '-';
					else
						input[k] = '+';
				}
			}
		}
		cout << flips << endl;
	}




	return 0;
}