#include <iostream>
#include <fstream>
#include <string>
#include <unordered_set>

using namespace std;
int countSheep(int start);

int main() {
	ifstream inputFile("A-small.in");
	ofstream out("A-small.out");
	int n = 0;
	inputFile >> n;
	for (int i = 1; i <= n; i++) {
		out << "Case #" << i << ": ";
		int start = 0;
		inputFile >> start;
		if (start == 0) {
			out << "INSOMNIA";
		} else {
			out << countSheep(start);
		}
		out << endl; 
	}
	return 0;
}

int countSheep(int start) {
	unordered_set<char> seen;
	int N = 1;
	int numSheep = 0;
	while (seen.size() != 10) {
		numSheep = N * start;
		string 	digits = to_string(numSheep);
		for (char digit : digits) {
			seen.insert(digit);
		}
		N++;
	}
	return numSheep;
}
