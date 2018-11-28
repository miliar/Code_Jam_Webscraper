//============================================================================
// Name        : Lawnmower.cpp
// Author      : 
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

class Rectangle {
public:

	Rectangle(size_t n, size_t m) : n(n), m(m), r(new size_t*[n]) {
		for(size_t x(0); x < n; ++x) {
			r[x] = new size_t[m];
		}
	}

	~Rectangle() {
		for (size_t x(0); x < n; ++x) {
			delete[] r[x];
		}
		delete[] r;
	}

	void print() {
		cout << "Rectangle (" << n << ", " << m << ")" << endl;
		for (size_t x(0); x < n; ++x) {
			for (size_t y(0); y < m; ++y) {
				cout << r[x][y] << " ";
			}
			cout << endl;
		}
		cout << endl;
	}

	bool checkCoord(size_t i, size_t j) {
		bool h = true;
		bool v = true;
		for (size_t x(0); x < n; ++x) {
			if (r[x][j] > r[i][j]) {
				h = false;
			}
		}

		for (size_t y(0); y < m; ++y) {
			if (r[i][y] > r[i][j]) {
				v = false;
			}
		}
		return h || v;

	}

	bool isValid() {
		for (size_t x(0); x < n; ++x) {
			for (size_t y(0); y < m; ++y) {
				if (checkCoord(x, y) == false) {
					return false;
				}
			}
		}
		return true;
	}

	size_t n;
	size_t m;
	size_t **r;
};

bool process_case(ifstream* piFile) {
	size_t N, M;
	*piFile >> N;
	*piFile >> M;
	cout << "N = " << N << ", M = " << M << endl;

	Rectangle r(N, M);
	for (size_t x(0); x < N; ++x) {
		for (size_t y(0); y < M; ++y) {
			*piFile >> r.r[x][y];
		}
	}

	//r.print();
	return r.isValid();
}

void process_file(ifstream* piFile, ofstream* poFile) {
	size_t T;
	*piFile >> T;
	cout << "The input file contains " << T << " test cases." << endl;

	for (size_t i(1); i < T+1; ++i) {
		cout << "Case " << i << endl;
		*poFile << "Case #" << i << ": ";
		if (process_case(piFile)) {
			*poFile << "YES"; cout << "YES";
		} else {
			*poFile << "NO"; cout << "NO";
		}
		*poFile << endl;
		cout << endl;
	}

}


int main(int argc, char ** argv) {
	if (argc != 2) {
		cout << "Usage: " << argv[0] << " input-file" << endl;
		return 0;
	}

	string iFilePath(argv[1]);
	ifstream iFile(iFilePath.c_str(), ios::in);
	if (!iFile.is_open()) {
		cout << "Error: Could not open input file [ " << iFilePath << "]." << endl;
		return 1;
	}
	stringstream oFilePath;
	oFilePath << iFilePath << "-output.txt";
	ofstream oFile(oFilePath.str().c_str(), ios::out);
	if (!oFile.is_open()) {
		cout << "Error: Could not open output file [ " << oFilePath << "]." << endl;
		iFile.close();
		return 1;
	}

	process_file(&iFile, &oFile);

	cout << "End." << endl;
	iFile.close();
	oFile.close();
	return 0;
}
