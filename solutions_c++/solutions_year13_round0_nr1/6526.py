/*
 * proba.cpp
 *
 *  Created on: 13-Apr-2013
 *      Author: ravi
 */
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cstdlib>
using namespace std;

#include "proba.h"

proba::proba() {
	// TODO Auto-generated constructor stub

}

proba::~proba() {
	// TODO Auto-generated destructor stub
}

proba::OUtput proba::stateOfGame() {
	// figure out if x has won
	const int count = 4;
	// check horizontally
	int stlinecount = 0;
	for (int i = 0; i < count; i++) {
			stlinecount = 0;
		for (int j = 0; j < count; j++) {
			if (mline[i].at(j) == 'X' || mline[i].at(j) == 'T') {
				stlinecount++;
				if (count == stlinecount)
					return X_won;
			}
		}
	}
	//check vertically
	stlinecount = 0;
	for (int j = 0; j < count; j++) {
			stlinecount = 0;
		for (int i = 0; i < count; i++) {
			if (mline[i].at(j) == 'X' || mline[i].at(j) == 'T') {
				stlinecount++;
				if (count == stlinecount)
					return X_won;
			}
		}
	}
	//check diagonally
	if ((mline[0].at(0) == 'X' || mline[0].at(0) == 'T') &&
		(mline[1].at(1) == 'X' || mline[1].at(1) == 'T') &&
		(mline[2].at(2) == 'X' || mline[2].at(2) == 'T') &&
		(mline[3].at(3) == 'X' || mline[3].at(3) == 'T')) {
		return X_won;
	}
	if ((mline[3].at(0) == 'X' || mline[3].at(0) == 'T') &&
		(mline[2].at(1) == 'X' || mline[2].at(1) == 'T') &&
		(mline[1].at(2) == 'X' || mline[1].at(2) == 'T') &&
		(mline[0].at(3) == 'X' || mline[0].at(3) == 'T')) {
		return X_won;
	}

	// figure out if o has won
	// check horizontally
	stlinecount = 0;
	for (int i = 0; i < count; i++) {
			stlinecount = 0;
		for (int j = 0; j < count; j++) {
			if (mline[i].at(j) == 'O' || mline[i].at(j) == 'T') {
				stlinecount++;
				if (count == stlinecount)
					return O_won;
			}
		}
	}
	//check vertically
	stlinecount = 0;
	for (int j = 0; j < count; j++) {
			stlinecount = 0;
		for (int i = 0; i < count; i++) {
			if (mline[i].at(j) == 'O' || mline[i].at(j) == 'T') {
				stlinecount++;
				if (count == stlinecount)
					return O_won;
			}
		}
	}
	//check diagonally
	if ((mline[0].at(0) == 'O' || mline[0].at(0) == 'T') &&
		(mline[1].at(1) == 'O' || mline[1].at(1) == 'T') &&
		(mline[2].at(2) == 'O' || mline[2].at(2) == 'T') &&
		(mline[3].at(3) == 'O' || mline[3].at(3) == 'T')) {
		return O_won;
	}
	if ((mline[3].at(0) == 'O' || mline[3].at(0) == 'T') &&
		(mline[2].at(1) == 'O' || mline[2].at(1) == 'T') &&
		(mline[1].at(2) == 'O' || mline[1].at(2) == 'T') &&
		(mline[0].at(3) == 'O' || mline[0].at(3) == 'T')) {
		return O_won;
	}

	//figure out if the game is still in progress
	for (int i = 0; i < count; i++) {
		for (int j = 0; j < count; j++) {
			if (mline[i].at(j) == '.') {
				return not_complete;
			}
		}
	}

	return draw;
}

void proba::solve(char *inputFile) {
	ifstream input(inputFile);
	ofstream output("output.txt");

	// Number of test cases
	getline (input, mline[0]);

	int testcases = atoi(mline[0].c_str());
	int count = 1;
	while  (input.good()) {
		if (count > testcases)
			break;
		// Each test case will have 4 lines
		getline (input, mline[0]);
		getline (input, mline[1]);
		getline (input, mline[2]);
		getline (input, mline[3]);

		// Figure out the state
		OUtput r = stateOfGame();
		switch(r) {
		case X_won:
			output << "Case #" << count << ": ";
			output << "X won" << endl;
			break;
		case draw:
			output << "Case #" << count << ": ";
			output << "Draw" << endl;
			break;
		case not_complete:
			output << "Case #" << count << ": ";
			output << "Game has not completed" << endl;
			break;
		case O_won:
			output << "Case #" << count << ": ";
			output << "O won" << endl;
			break;
		}

		// Skip the blank line
		getline (input, mline[0]);
		count++;
	}

	input.close();
	output.close();
}
