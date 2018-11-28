#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ifstream inputFile("B-small.in");
	ofstream out("B-small.out");
	int numCases = 0;
	inputFile >> numCases;
	for (int i = 1; i <= numCases; i++) {
		out << "Case #" << i << ": ";
		string pancakes = "";
		inputFile >> pancakes;
		
		int swaps = 0;
		char lastChar = pancakes[0];
		for (char pancake : pancakes) {
			if (lastChar != pancake) {
				swaps++;
			}
			lastChar = pancake;
		}
		if ((swaps%2 == 0 && pancakes[0] == '+') || (swaps%2 == 1 && pancakes[0] == '-')) {
			out << swaps;
		} else {
			out << swaps + 1;
		}
		out << endl;
	}
	return 0;
}
