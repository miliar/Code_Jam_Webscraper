//#include "stdafx.h"

#ifndef TOOLS_H
#define TOOLS_H

#include <vector>
#include <string>

#include "General.h"

bool  compareMatrices(S32 row, S32 col, S32** array1, S32** array2);
void  tokenize(string line, vector<string> &results);
S32   getHexInput(ifstream &inputFile);
bool  isPalindrome(S32 value);
S32   findNearestSquareNum(S32 start, bool isHigher);
void  delete2DimArray(S32** &array, S32 row);
S32** create2DimArray(S32 row, S32 col);
void  fillArray(S32** array, S32 row, S32 col, string line);
void fillArray(S32** array, S32 row_no, S32 cols, vector<string> &tokens);
void showArray(S32** array, S32 row, S32 col);


#endif //TOOLS_H
