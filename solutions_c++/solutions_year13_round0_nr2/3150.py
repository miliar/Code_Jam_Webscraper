// Code Jam 2013 qualifier
// Problem B
// Author: intrepid
//
#include <iostream>
#include <vector>
#include <algorithm>
#include <stdexcept>
using namespace std;

class Lawn
{
public:
	typedef vector<int> row_t;
	typedef vector<row_t> matrix_t;
	
	Lawn(size_t rows, size_t cols) :
		rows_(rows),
		cols_(cols),
		data_(rows, row_t(cols))
	{
	}
	
	row_t& operator [] (size_t row) { return data_.at(row); }
	
	row_t getRow (size_t row) const { return data_.at(row); }
	row_t getCol(size_t col) const
	{
		row_t returnValue;
		for_each(data_.begin(), data_.end(), [&returnValue, &col] (const row_t& row) {
			returnValue.push_back(row[col]);
		});
		return returnValue;
	}
	
	bool possible() const
	{
		matrix_t possibleMap(rows_, row_t(cols_, 0));
		
		// Check cols
		for (int col=0; col < cols_; ++col) {
			row_t curCol = getCol(col);
			row_t::iterator maxE = max_element(curCol.begin(), curCol.end());
			if ( maxE == curCol.end() ) throw std::logic_error("No elements in col!");
			for (int row=0; row < rows_; ++row) {
				if ( curCol.at(row) == *maxE ) possibleMap[row][col] = 1;
			}
		}
		// Check rows
		for (int row=0; row < rows_; ++row) {
			row_t curRow = getRow(row);
			row_t::iterator maxE = max_element(curRow.begin(), curRow.end());
			if ( maxE == curRow.end() ) throw std::logic_error("No elements in row!");
			for (int col=0; col < cols_; ++col) {
				if ( curRow.at(col) == *maxE ) possibleMap[row][col] = 1;
			}
			// Actual check
			if ( find(possibleMap[row].begin(), possibleMap[row].end(), 0) != possibleMap[row].end() ) {
				return false;
			}
		}
		return true;
	}

private:
	size_t rows_;
	size_t cols_;
	matrix_t data_;
};

int main()
{
	size_t numTests;
	cin >> numTests;
	if ( !cin.good() ) {
		cerr << "Error getting numTests.\n";
		return 1;
	}
	cerr << "Tests: " << numTests << '\n';
	
	for (int i=0; i < numTests; ++i) {
		size_t rows, cols;
		cin >> rows >> cols;
		if ( !cin.good() ) {
			cerr << "Error reading rows and cols.\n";
			return 1;
		}
		
		Lawn lawn(rows, cols);
		for (int row=0; row < rows; ++row) {
			for (int col=0; col < cols; ++col) {
				cin >> lawn[row][col];
			}
		}
		if ( !cin.good() ) {
			cerr << "Error reading data.\n";
			return 1;
		}
		
		
		cout << "Case #" << i + 1 << ": ";
		cout << ( lawn.possible() ? "YES" : "NO" );
		cout << '\n';
	}
	
	cerr << "Done.\n";
	
	return 0;
}
