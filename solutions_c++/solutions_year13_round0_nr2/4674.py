#include <iostream>
#include <fstream>
#include <ostream>
#include <cmath>
#include <cstdlib>
#include <stdio.h>
#include <string>
using namespace std;

#include "problems.h"

bool isValid(int** heights, int rows, int cols){
	bool* rowsLeft = new bool[rows];
	for(int r = 0; r < rows; r++){
		rowsLeft[r] = true;
	}
	bool* colsLeft = new bool[cols];
	for(int c = 0; c < cols; c++){
		colsLeft[c] = true;
	}
	bool patchLeft = true;
	while(patchLeft){
		patchLeft = false;
		int min = 100000;
		int minRow = 0;
		int minCol = 0;
		for(int r = 0; r < rows; r++){
			if(rowsLeft[r] == false){
				continue;
			}
			for(int c = 0; c < cols; c++){
				if(colsLeft[c] == false){
					continue;
				}
				if(heights[r][c] < min){
					min = heights[r][c];
					minRow = r;
					minCol = c;
					patchLeft = true;
				}
			}
		}
		bool validRow = true;
		bool validCol = true;
		for(int r = 0; r < rows; r++){
			if(rowsLeft[r] == false){
				continue;
			}
			if(heights[r][minCol] != min){
				validCol = false;
				break;
			}
		}
		for(int c = 0; c < cols; c++){
			if(colsLeft[c] == false){
				continue;
			}
			if(heights[minRow][c] != min){
				validRow = false;
				break;
			}
		}
		if(validRow){
			rowsLeft[minRow] = false;
		}
		if(validCol){
			colsLeft[minCol] = false;
		}
		if(validRow == false && validCol == false){
			delete [] rowsLeft;
			delete [] colsLeft;
			return false;
		}
	}
	delete [] rowsLeft;
	delete [] colsLeft;
	return true;
}


void problem2(char* input, char* output){
	ifstream fin;
	fin.open(input);

	ofstream fout;
	fout.open(output);

	char buf[100];

	int nCases;
	fin >> nCases;
	for(int i = 0; i < nCases; i++){
		int rows, cols;
		fin >> rows >> cols;
		int** heights = new int*[rows];
		for(int r = 0; r < rows; r++){
			heights[r] = new int[cols];
			for(int c = 0; c < cols; c++){
				fin >> heights[r][c];
			}
		}

		if(isValid(heights, rows, cols)){
			sprintf(buf, "Case #%d: YES", (i+1));
		} else {
			sprintf(buf, "Case #%d: NO", (i+1));
		}
		fout << buf << endl;


		for(int r = 0; r < rows; r++){
			delete [] heights[r];
		}
		delete [] heights;
	}

	fin.close();
	fout.close();
}


int main(int argc, char** argv){
	char* input = "B-large.in";
	char* output = "B-large.out";

	problem2(input, output);

	return 0;
}
