#include <iostream>
#include <fstream>
using namespace std;

int numberFlip(string);

int main() {
	ofstream myfile("B-large.txt");
	ifstream target("B-large.in");
	int T;
	target >> T;
	for (int i = 0; i < T; i++) {
		string input;
		target >> input;
		int numb = numberFlip(input);
		myfile << "Case #" << i + 1 << ": " << numb << endl;
	}
	return 0;
}

int numberFlip(string initial) {
	string result = "";
	int length = initial.length();
	char prev = ' ';
	for (int i = 0; i < length; i++) {
		if (prev != initial[i]) {
			prev = initial[i];
			result = result + prev;
		}
	}
	if (initial[length - 1] == '+')
		return result.length() - 1;
	return result.length();
}
