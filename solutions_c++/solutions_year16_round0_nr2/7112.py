#include <fstream>
#include <iostream>
#include <string>
using namespace std;

bool mustFlip(char c, bool side) {
	return ((c == '-' && side) || (c == '+' && !side));
}

bool side(char c) {
	return (c == '+');
}

int solve(string str) {
	bool happySideUp = side(str[0]);
	int flips = 0;
	for (int i = 1; i < str.length(); i++) {
		if (mustFlip(str[i], happySideUp))
		{
			flips++;
			happySideUp = !happySideUp;
		}
	}
	if (!happySideUp) flips++;
	return flips;
}

int main() {
	ifstream inputFile;
	inputFile.open("input.txt");
	ofstream outputFile;
	outputFile.open("output.txt");
	int T;
	string pancakes;
	inputFile >> T;
	getline(inputFile, pancakes); // ignore newline
	for (int i = 1; i <= T; i++)
	{
		getline(inputFile, pancakes);
		outputFile << "Case #" << i << ": " << solve(pancakes) << endl;
	}
}