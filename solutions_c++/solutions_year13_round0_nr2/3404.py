#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <fstream>
#include <map>
#include <algorithm>

using namespace std;

#define DIM_X		100
#define DIM_Y		100

static int grid[DIM_X][DIM_Y];
static int rowMax[DIM_Y];
static int colMax[DIM_X];
static int N;
static int M;

void computeRowMax() {
	for(int j = 0; j < N; j++) {
		rowMax[j] = -1;
		for(int i = 0; i < M; i++) {
			rowMax[j] = max(rowMax[j], grid[i][j]);
		}
	}
}

void computeColMax() {
	for(int i = 0; i < M; i++) {
		colMax[i] = -1;
		for(int j = 0; j < N; j++) {
			colMax[i] = max(colMax[i], grid[i][j]);
		}
	}
}

bool isPossible() {
	computeColMax();
	computeRowMax();

	for(int j = 0; j < N; j++) {
		for(int i = 0; i < M; i++) {
			if(grid[i][j] < rowMax[j] && grid[i][j] < colMax[i]) {
				return false;
			}
		}
	}
	return true;
}

int main(int argc, char* argv[]) {
	string inTestName, outTestName;

	cout << "Enter the in test file name : " << endl;
	cin >> inTestName;
	cout << endl;

	size_t found = inTestName.find_last_of(".");
	outTestName = inTestName.substr(0, found) + ".out";

	/* Open file */
	ifstream inFile(inTestName.c_str());
	if(!inFile.is_open()) {
		cout << "Can't open input file" << endl;
		system("PAUSE");
		return 1;
	}

	ofstream outFile(outTestName.c_str());
	if(!outFile.is_open()) {
		cout << "Can't open output file" << endl;
		system("PAUSE");
		return 1;
	}

	int T; /*number of tests */
	inFile >> T;

	cout << "Start : "<< endl;
	for(int t = 0; t < T; t++) {
		cout << "\rProcess test " << t << " out of " << T;
		inFile >> N >> M;

		/* Fill grid */
		for(int j = 0; j < N; j++) {
			for(int i = 0; i < M; i++) {
				inFile >> grid[i][j];
			}
		}

		/* Check if X won */
		if(isPossible()) {
			outFile << "Case #" << t + 1 << ": YES" << endl;
		}
		else {
			outFile << "Case #" << t + 1 << ": NO" << endl;
		}
	}
	outFile.close();
	inFile.close();

	cout << endl << "Stop" << endl;

	system("PAUSE");
	return 0;
}
