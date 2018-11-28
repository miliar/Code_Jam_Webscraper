#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int Pancake_rev(string pancake) {
	char one = pancake[0];
	int count = 0;
	for (int i = 1; i < pancake.size(); ++i) {
		if (pancake[i] != one) {
			count++;
			one = pancake[i];
		}
	}
	if (pancake[pancake.size() - 1] == '-') count++;
	return count;
}

int main() {
	ifstream input("B-large.in");
	ofstream output("large_case_answer.txt");
	string num;
	getline(input, num);
	int n = stoi(num);
	for (int i = 0; i < n; ++i) {
		output << "case #" << i + 1 << ": ";
		getline(input, num);
		int res = Pancake_rev(num);
		output << res << endl;
	}
	return 0;
}