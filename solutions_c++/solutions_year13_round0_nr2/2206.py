#include "LawnSquare.h"
#include <iostream>

LawnSquare::LawnSquare( void ) {
	length = 0;
	width = 0;
	numberOfSquares = 0;
	heightArray = 0;
	//checkedArray = 0;
}

LawnSquare::LawnSquare( int l, int w, int heightInfo[] ) {
	length = l;
	width = w;
	numberOfSquares = l*w;
	heightArray = new int[numberOfSquares];
	//checkedArray = new bool[numberOfSquares];

	for( int i = 0; i < numberOfSquares; i++ ) {
		heightArray[i] = heightInfo[i];
		//checkedArray[i] = false;
	}
}

LawnSquare::~LawnSquare( void ) {
	if( heightArray ) { delete[] heightArray; }
	//if( checkedArray ) { delete[] checkedArray; }
}

bool LawnSquare::CheckIfPossible( void ) {
	for( int i = 0; i < numberOfSquares; i++ ) {
		int row = i / width;
		int column = i % width;

		int squareHeight = heightArray[i];
		bool possibleColumn = true;
		bool possibleRow = true;

		// Check columns
		for( int j = 0; j < length; j++ ) {
			if( squareHeight < heightArray[ (j*width)+column ] ) {
				possibleColumn = false;
			}
		}

		// Check rows
		for( int j = 0; j < width; j++ ) {
			if( squareHeight < heightArray[ (row*width)+j ] ) {
				possibleRow = false;
			}
		}

		if( !possibleColumn && !possibleRow ) {
			return false;
		}
	}

	//If no wrong combinations are found its true
	return true;
}

void LawnSquare::PrintSquare( void ) {

	std::cout << "-----------------------" << std::endl;

	for( int i = 0; i < numberOfSquares; i++ ) {
		if( i % width == 0 ) { std::cout << std::endl; };
		std::cout << heightArray[i];
	}

	std::cout << std::endl << "-----------------------" << std::endl;
}