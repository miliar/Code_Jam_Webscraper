#include <iostream>
#include <cctype>
#include <queue>

using namespace std;

// Coordinate:
// Used to hold a coordinate of the mine field.
struct Coordinate {
	Coordinate(int row_, int col_) : row(row_), col(col_) {};
	int row;
	int col;
};

class MineField {
	public:

		bool isSolved() { return solved; };		
		void solveAllMines(int, int);
		void print();
		void printSolution();

		MineField(int row_, int col_, int mines_);
		~MineField();

	private:

		//Prohibit copy and assignment

		char ** mineField;
		int row;
		int col;
		int mines;
		bool solved;
		queue<Coordinate> toMark;

		void clear();

		void generateNumbers();
		void generateMarkings();
		void eraseNumberMarkings();

		void solveMineField();
		bool verifyMineField();

		int numAdjacentMines(int, int);	
		void pushAdjacentCells(int, int);
};

int main() {
	
	int testCases = 0;
	int row = 0;
	int col = 0;
	int mines = 0;

	char ** mineField;

	cin>>testCases;

	for (int i = 0; i < testCases; i++) {
		cout<<"Case #"<<i+1<<":"<<endl;
		cin>>row;
		cin>>col;
		cin>>mines;

		MineField m(row, col, mines);
		m.solveAllMines(0, mines);

		if (!m.isSolved()) {
			cout<<"Impossible"<<endl;
		}

	}

	return 0;

}

// Constructor
MineField::MineField(int row_, int col_, int mines_) : row(row_), col(col_), mines(mines_), solved(false) {
	mineField = new char* [row];

	for (int i = 0; i < row; i++) {

		mineField[i] = new char[col];

		for (int j = 0; j < col; j++) {
			mineField[i][j] = '.';
		}

	}

}

// Destructor
MineField::~MineField() {

	// Delete the rows
	for (int i = 0; i < row; i++) {
		delete [] mineField[i];
	}

	// Delete the field
	delete [] mineField;

}

// Print Solution:
// Prints the solution by removing the 'x' markings.
void MineField::printSolution()
{
	for (int i = 0; i < row; i++ ) {
		for (int j = 0; j < col; j++) {
			if (mineField[i][j] == 'x' || isdigit(mineField[i][j])) {
				mineField[i][j] = '.';
			}
			cout<<mineField[i][j];
		}
		cout<<'\n';
	}
}


// Print:
// Prints the cell contents of the minefield by [row][col].
void MineField::print()
{
	for (int i = 0; i < row; i++ ) {
		for (int j = 0; j < col; j++) {
			cout<<mineField[i][j];
		}
		cout<<'\n';
	}
}

// Clear:
// Sets all cells of the mine field to '.'.
void MineField::clear() {
	for (int i = 0; i < row; i++ ) {
		for (int j = 0; j < col; j++) {
			mineField[i][j] = '.';
		}
		cout<<'\n';
	}
}

// Generate Numbers:
// Generate the numbers of adjacent mines for every cell on the field.
void MineField::generateNumbers()
{
	for (int i=0; i < row; i++) {
		for (int j=0; j < col; j++) {
			if (mineField[i][j] == '.') {
				mineField[i][j] = '0' + numAdjacentMines(i, j);
			}
		}
	}
}

// Generate Markings:
// Mark the cells that will be revealed in one turn by clicking location
// startRow and startCol.
void MineField::generateMarkings() {

	int startRow = 0;
	int startCol = 0;
	bool foundZero = false;

	// Find the initial zero
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {

			if (!foundZero && mineField[i][j] == '0') {
				foundZero = true;
				startRow = i;
				startCol = j;
			}

			if (!foundZero && isdigit(mineField[i][j])) {
				startRow = i;
				startCol = j;
			}

		}
	}

	toMark.push(Coordinate(startRow, startCol));

	// Use breadth first search and expand around the zero
	while (!toMark.empty()) {

		Coordinate c = toMark.front();
		toMark.pop();

		// If the cell is zero, mark the cell, and push all adjacent cells
		if (mineField[c.row][c.col] == '0') {
			mineField[c.row][c.col] = 'x';
			pushAdjacentCells(c.row, c.col);
		}

		// If the cell is non-zero, simply mark the cell
		else {
			mineField[c.row][c.col] = 'x';
		}

	}

	// Mark the starting point
	mineField[startRow][startCol] = 'c';

	return;
}

// Erase Markings:
// Erases any digit, 'c', or 'x' marks from the cells.
void MineField::eraseNumberMarkings()
{
	for (int i=0; i < row; i++) {
		for (int j=0; j < col; j++) {
			if (isdigit(mineField[i][j]) || mineField[i][j] == 'x' || mineField[i][j] == 'c') {
				mineField[i][j] = '.';
			}
		}
	}
}

// Push Adjacent Cells:
// Pushes all digit adjacent cells to be marked
void MineField::pushAdjacentCells(int currRow, int currCol) {

	for (int v = -1; v <=1; v++) {
		for (int h = -1; h <=1; h++) {
			bool r = ((currRow + v < row) && (currRow + v >= 0));
			bool c = ((currCol + h < col) && (currCol + h >= 0));
			
			if (r && c && isdigit(mineField[currRow + v][currCol + h])) {
				toMark.push(Coordinate(currRow + v, currCol + h));
			}
		}
	}

	return;
	
}

// Number of Adjacent Mines:
// Determines number of mines adjacent to current cell
int MineField::numAdjacentMines(int currRow, int currCol) {

	int numMines = 0;

	for (int v = -1; v <= 1; v++) {
		for (int h = -1; h <= 1; h++) {
			bool r = ((currRow + v < row) && (currRow + v >= 0));
			bool c = ((currCol + h < col) && (currCol + h >= 0));
			
			if (r && c && mineField[currRow + v][currCol + h] == '*') {
				numMines++;
			}
		}
	}

	return numMines;
}

// Verify Mine Field:
// Verifies if mine field is one-click valid by checking that all digits
// have been marked by 'x's.
bool MineField::verifyMineField() {

	for (int i=0; i < row; i++) {
		for (int j=0; j < col; j++) {
			if (isdigit(mineField[i][j])) {
				return false;
			}
		}
	}

	return true;
}

// Not an efficient solution
// Recursively determine the next place to put the mine
void MineField::solveAllMines(int start, int minesLeft) {

	// If the mine field configuration has been solved, no need to permute
	// further possibilities.
	if (solved) return;

	// Base case: if no more mines to place, solve this configuration.
	if (minesLeft == 0) {
		solveMineField();
		return;
	}

	// Shift the mine by one spot, then solve next place to put mine
	for (int i = start; i < row*col - minesLeft + 1; i++) {

		// Put the mine at the next location
		int thisRow = i / col;
		int thisCol = i % col;
		mineField[thisRow][thisCol] = '*';

		// Erase the mine at the previous location
		if (i > start) {
			int prevRow = (i - 1) / col;
			int prevCol = (i - 1) % col;
			mineField[prevRow][prevCol] = '.';
		}

		// Recursively locate the next place to put the mine
		solveAllMines(i + 1, minesLeft - 1);
		mineField[thisRow][thisCol] = '.';
	}

}

// Solve Mine Field:
// Solve the current mine field configuration by seeing if 
// all digits can be marked with one click.
void MineField::solveMineField() {

//		cout<<"--------------"<<endl;
		generateNumbers();
//		cout<<"Number field: "<<endl;
//		print();

		generateMarkings();
//		cout<<"Marked field: "<<endl;
//		print();
//		cout<<"--------------"<<endl;

		// If mine field has solution, marked as solved
		if (verifyMineField()) {
			solved = true;
			printSolution();
		} else {
			eraseNumberMarkings();			
		}

}
