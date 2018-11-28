#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void flip(string &s, int index) {
	for (int i = 0; i <= index; ++i) {
		if (s[i] == '-') s[i] = '+';
		else s[i] = '-';
	}
}

int main() {

	ofstream output;
	output.open("output.txt");

	int n;
	cin >> n;

	for (int i = 0; i < n; ++i) {
		int counter = 0;
		string s;
		cin >> s;
		for (int j = s.length() - 1; j >= 0; --j) {
			if (s[j] == '-') {
				flip(s, j);
				++counter;
			}
		}
		output << "Case #" << i + 1 << ": ";
		output << counter << endl;
	}

}