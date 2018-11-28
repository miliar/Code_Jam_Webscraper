#include <iostream>
#include <string>
#include <cstdio>
#include <fstream>

using namespace std;

int main() {
	fstream file;
	file.open("A-large.in", ios::in);
	if (!file.is_open()) {
		return EXIT_FAILURE;
	}
	fstream file2;
	file2.open("A-large.txt", ios::out);
	if (!file2.is_open()) {
		return EXIT_FAILURE;
	}
	int n;
	file >> n;
	for (int i = 0; i < n; i++) {
		int b;
		file >> b;
		string a;
		file >> a;
		int counter = 0;
		int fre = 0;
		for (int j = 0; j <= b; j++) {
			if (counter < j) {
				fre += j-counter;
				counter = j;
			}
			counter += a[j]-'0';
		}
		file2 << "Case #" << i+1 << ": " << fre << endl;
	}
	file.close();
	file2.close();
	return 0;
}