#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;
void flip(string& str, int end) {
	for (int i = 0; i < end; ++i) {
		if (str[i] == '+') {
			str[i] = '-';
		} else {
			str[i] = '+';
		}
	}
}
int find_last(const string& str) {
	for (int i = str.length()-1; i >= 0; --i) {
		if (str[i] == '-') {
			return i;
		}
	}
	return -1;
}
int main() {
	fstream fin;
	fin.open("input.txt");
	int cases = 0;
	fin >> cases;
	for (int rnd = 0; rnd < cases; ++rnd) {
		// Do each case here
		string pancakes;
		fin >> pancakes;
		int flips = 0;
		while (true) {
			// cout << "Current pancakes: " << pancakes << endl; 
			int loc = find_last(pancakes);
			if (loc == -1) {
				break;
			}
			flips++;
			flip(pancakes, loc+1);
		}


		// Output case info
		cout << "Case #" << rnd+1 << ": " << flips << endl;
	}
	fin.close();
	return 0;
}