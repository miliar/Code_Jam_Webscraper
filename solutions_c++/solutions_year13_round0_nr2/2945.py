#include <iostream>
#include <fstream>
using namespace std;

// Bi-Dimensional Array that can be dynamically allocated
template<typename T>
class BiDiArray
{
public:
	BiDiArray(unsigned int r, unsigned int c)
	{
		// TODO: Exception if r or c = 0
		data = new T[r * c];
		RowCount = r;
		ColCount = c;
	}
	T& At(unsigned int r, unsigned int c)
	{
		// TODO: Exception for Out of Bounds
		return data[ColCount * r + c];
	}
	unsigned int Rows() { return RowCount; }
	unsigned int Cols() { return ColCount; }

protected:
	T *data;
	unsigned int RowCount;
	unsigned int ColCount;
};

template <class T>
bool ValidField(BiDiArray<T> &Field) {
	// General algorithm:
	// Look for the maximum height in a row (or column).  Anything shorter than that in a row must have been cut
	//      in its column (or row), so ensure that there is nothing taller in its column (or row)

	bool Valid = true;		// Assume anything is possible unless demonstrated otherwise

	// First, check each row
	for (unsigned int i = 0; Valid && (i < Field.Rows()); ++i) {
		// Find the maximum value
		T maxVal = Field.At(i, 0);
		for (unsigned int j = 1; j < Field.Cols(); ++j) {
			if (Field.At(i, j) > maxVal) {
				maxVal = Field.At(i, j);
			}
		}

		for (unsigned int j = 0; Valid && (j < Field.Cols()); ++j) {
			if (Field.At(i, j) < maxVal) {
				// this block must have been cut in its column so there must not be anything in its
				// column taller than it
				for (unsigned int k = 0; Valid && (k < Field.Rows()); ++k) {
					if (Field.At(k, j) > Field.At(i, j)) {
						Valid = false;
					}
				}
			}
		}
	}

	// Then, check each column
	for (unsigned int i = 0; Valid && (i < Field.Cols()); ++i) {
		// Find the maximum value
		T maxVal = Field.At(0, i);
		for (unsigned int j = 1; j < Field.Rows(); ++j) {
			if (Field.At(j, i) > maxVal) {
				maxVal = Field.At(j, i);
			}
		}

		for (unsigned int j = 0; Valid && (j < Field.Rows()); ++j) {
			if (Field.At(j, i) < maxVal) {
				// this block must have been cut in its column so there must not be anything in its
				// column taller than it
				for (unsigned int k = 0; Valid && (k < Field.Cols()); ++k) {
					if (Field.At(j, k) > Field.At(j, i)) {
						Valid = false;
					}
				}
			}
		}
	}

	return Valid;
}

void main() {
	ifstream in("D:\\lm2.txt");
	ofstream out("D:\\lm2out.txt");
	int numBoards;
	in >> numBoards;
	for (int board = 1; board <= numBoards; ++board) {
		unsigned int rows;
		unsigned int cols;
		in >> rows >> cols;
		BiDiArray<int> Board(rows, cols);
		for (unsigned int i = 0; i < rows; ++i) {
			for (unsigned int j = 0; j < cols; ++j) {
				in >> Board.At(i, j);
			}
		}
		out << "Case #" << board << ": " << (ValidField(Board) ? "YES" : "NO") << endl;
	}

	in.close();
	out.close();
}


