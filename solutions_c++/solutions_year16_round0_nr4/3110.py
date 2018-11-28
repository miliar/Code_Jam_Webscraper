#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ifstream inputFile("B-small.in");
	ofstream out("B-small.out");
	int n = 0;
	inputFile >> n;
	for (int i = 1; i <= n; i++) {
		out << "Case #" << i << ": 1";
		int K = 0;
		inputFile >> K;
		for (int j = 2; j <= K; j++) {
			out << " " << j;
		}
		out << endl;
		inputFile >> K;
		inputFile >> K; 
	}
	return 0;
}
