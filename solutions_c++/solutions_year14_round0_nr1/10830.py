//============================================================================
// Name        : GCJ_Magic_Trick.cpp
// Author      : bernoullymk <mkibiana@gmail.com>
// Version     : 1.0
// Copyright   : bernoullymk - Google Code Jam 2014
// Description : Magic Trick
//============================================================================

#include <cstdlib>
#include <iostream>
#include <fstream>
using namespace std;

typedef int t_card_grid[4][14];

int main(int argc, char *argv[]) {

	int num_cases = 0;

	// input
	int first_row, second_row;
	t_card_grid grid_1, grid_2;

	// output
	int card;

	// auxiliary variables
	int i, j, count;

	// file streams
	ifstream in_file;
	ofstream out_file;

	if(argc == 3) {
		in_file.open(argv[1]);
		if(!in_file.is_open()) {
			cerr << "Error: Could not open input file '" << argv[1] << "'" << endl;
			exit(6);
		}
		out_file.open(argv[2]);
		if(!out_file.is_open()) {
			cerr << "Error: Could not open out file '" << argv[2] << "'" << endl;
			exit(8);
		}
	} else {
		cerr << "Error: Invalid number of arguments. Expected: in_file out_file" << endl;
		exit(4);
	}
	in_file >> num_cases;
	for(int it = 0; it < num_cases; it++) {
		count = 0;
		// read first row choice
		in_file >> first_row;
		first_row--;	// index from 0 to 3 instead of from 1 to 4
		// read first grid configuration, i: row, j: column
		for(i = 0; i < 4; i++) {
			for(j = 0; j < 4; j++) {
				in_file >> grid_1[i][j];
			}
		}
		// read second row choice
		in_file >> second_row;
		second_row--;	// index from 0 to 3 instead of from 1 to 4
		// read second grid configuration, i: row, j: column
		for(i = 0; i < 4; i++) {
			for(j = 0; j < 4; j++) {
				in_file >> grid_2[i][j];
			}
		}

		// do the magic, i: column of grid_1, j: column of grid_2
		for(i = 0; i < 4; i++) {
			for(j = 0; j < 4; j++) {
				if(grid_1[first_row][i] == grid_2[second_row][j]) {
					count++;
					card = grid_1[first_row][i];
					if(count > 1) {
						break;
					}
				}
			}
		}
		switch(count) {
		case 0:
			out_file << "Case #" << (it + 1) << ": Volunteer cheated!" << endl;
		break;
		case 1:
			out_file << "Case #" << (it + 1) << ": " << card << endl;
			break;
		default:
			out_file << "Case #" << (it + 1) << ": Bad magician!" << endl;
			break;
		}
	}
	if(in_file.is_open())	in_file.close();
	if(out_file.is_open())	out_file.close();

	return 0;
}
