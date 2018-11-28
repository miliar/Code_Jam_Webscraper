#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <set>

using namespace std;

#include "CJUtils.cpp"

const string INPUT_FILE = "B-large.in";
const string OUTPUT_FILE = "B-large.out";


typedef vector<char> charGrid;
// Indexed with (0,0) at the top left. The first coord is the row, and the second is the col.
int index(int row, int col, int nCols) {
	return row * nCols + col;
}

void printGrid(charGrid& grid, int nRows, int nCols) {
	cout << "Printing grid: " << endl;
	for (int i = 0; i < nRows; ++i) {
		for (int j = 0; j < nCols; ++j) {
			cout << grid[index(i, j, nCols)] << " ";
		}
		cout << endl;
	}
}

bool gridGood(charGrid& currGrid, int nRows, int nCols) {
	// Make sure that these grids have full rows and columns.
	// Iterate through the rows, if it's a full row of 'X', change them to 'V'
	for (int row = 0; row < nRows; ++row) {
		bool allX = true;
		for (int col = 0; col < nCols; ++col) {
			if (currGrid[index(row, col, nCols)] != 'X')
				allX = false;
		}
		if (allX) {
			for (int col = 0; col < nCols; ++col) {
				currGrid[index(row, col, nCols)] = 'V';
			}
		}
	}

	// Then iterate through the columns, if it's a full col of 'X' or 'V', change them to 'V'
	for (int col = 0; col < nCols; ++col) {
		bool allGood = true;
		for (int row = 0; row < nRows; ++row) {
			if (currGrid[index(row, col, nCols)] != 'X' && currGrid[index(row, col, nCols)] != 'V') {
				allGood = false;
			}
		}
		if (allGood) {
			for (int row = 0; row < nRows; ++row) {
				currGrid[index(row, col, nCols)] = 'V';
			}
		}
	}

	// If you can make the pattern, there should now be no more 'X's in the grid.
	for (int i = 0; i < currGrid.size(); ++i) {
		if (currGrid[i] == 'X') return false;
	}
	return true;
}

string doTestCase(ifstream& infile) {
	// Read dimensions of the lawn N and M
	// N is number of rows, M is number of columns
	string line;
	getline(infile, line);
	stringstream sstr;
	sstr.str(line);
	size_t N, M;
	sstr >> N >> M;

	// Read N rows. As you read, keep track of numbers that you've seen.
	set<int> heightsSeen;
	vector<int> heightGrid;
	for (int row = 0; row < N; ++row) {
		getline(infile, line);
		stringstream sstr;
		sstr.str(line);
		for (int col = 0; col < M; ++col) {
			int square;
			sstr >> square;
			heightsSeen.insert(square);
			heightGrid.push_back(square);
		}
	}

	// Sort the numbers, or make sure you get them in sorted order. Actually, maybe unnecessary.
	// For each number you've seen, construct a Grid with an 'X' for every number that is
	// that number or below, and a '.' otherwise.
	vector<charGrid> heightLayouts;
	for (set<int>::iterator it = heightsSeen.begin(); it != heightsSeen.end(); ++it) {
		int height = *it;
		charGrid currGrid;
		for (int i = 0; i < heightGrid.size(); ++i) {
			if (heightGrid[i] <= height) {
				currGrid.push_back('X');
			} else {
				currGrid.push_back('.');
			}
		}
		heightLayouts.push_back(currGrid);
	}

	// Make sure that these grids have full rows and columns.
	// Iterate through the rows, if it's a full row of 'X', change them to 'V'
	// Then iterate through the columns, if it's a full col of 'X' or 'V', change them to 'V'
	for (int i = 0; i < heightLayouts.size(); ++i) {
		//printGrid(heightLayouts[i], N, M);
		// If you can make the pattern, there should now be no more 'X' in the grid.
		if (!gridGood(heightLayouts[i], N, M)) {
			// If there are 'X's in the grid, return NO.
			return "NO";
		}
	}
	// All of the grids worked, so we're good.
	return "YES";
}

int main() {

	ifstream infile(INPUT_FILE.c_str());
	if (!infile.good()) {
		cout << "Error opening input file." << endl;
		return -1;
	}
	ofstream outfile(OUTPUT_FILE.c_str());

	string line;
	// Read the number of test cases
	getline(infile, line);
	size_t T = StringToInteger(line);
	cout << "Test cases " << T << endl;
	for (size_t i = 0; i < T; ++i) {
		cout << "Doing test case " << i + 1 << endl;
		string answer = doTestCase(infile);
		outfile << "Case #" << i + 1 << ": " << answer << endl;
	}

	getline(cin, line);
	return 0;
}