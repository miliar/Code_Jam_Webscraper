#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main() {
	fstream fin;
	fin.open("input_pancakes.txt", ios::in | ios::out);

	int t;
	fin >> t;

	string pancakes;
	long flips = 0, idx;
	for (int i = 1; i <= t; i++) {
		fin >> pancakes;
		flips = 0;

		while ((idx = pancakes.find_last_of("-")) != -1) {
			flips ++;
			for (int j = idx; j >= 0; j--) {
				switch(pancakes[j]) {
					case '+':
						pancakes[j] = '-';
						break;
					case '-':
						pancakes[j] = '+';
						break;
					default:
						cout << "Invalid sign!";
						break;
				}
			}
		}

		cout << "Case #" << i << ": " << flips << endl;
	}

	fin.close();

	return 0;
}
