/*
 * TicTacToeTomek.h
 *
 *  Created on: Apr 13, 2013
 *      Author: taylan
 */

#ifndef TICTACTOETOMEK_H_
#define TICTACTOETOMEK_H_
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include "stdlib.h"

using namespace std;

string checkRows(char **board);
string checkCols(char **board);
string checkDiagonals(char **board);
void runQualificationA();


#endif /* TICTACTOETOMEK_H_ */
