#include <iostream>
#include <fstream>

using namespace std;

int goodNumbers[] = {1, 4, 9, 121, 484};
int nGoodNumbers = 5;

int main(int argc, char* argv[]) {
	if (argc != 2) {
		cerr << "Usage: solver <input-file>" << endl;
		cerr << "Wrong number of arguments!" << endl;
		return 1;
	}
	ifstream inputFile;
	inputFile.open(argv[1], ifstream::in);
	if (!inputFile.is_open()) {
		cerr << "Could not open '" << argv[1] << "'." << endl;
		return 1;
	}
	int T;
	inputFile >> T;
	//cout << "Processing " << T << " cases:" << endl;
	for (int t = 1; t <= T; t++) {
		int A, B;
		inputFile >> A;
		inputFile >> B;
		cout << "Case #" << t << ": ";
		int i = 0;
		int n = 0;
		while (goodNumbers[i] < A && i < nGoodNumbers) {
			i++;
		}
		if (i == nGoodNumbers) {
			cout << 0 << endl;
			continue;
		}
		while (goodNumbers[i] <= B && i < nGoodNumbers) {
			i++;
			n++;
		}
		cout << n << endl;
	}
}