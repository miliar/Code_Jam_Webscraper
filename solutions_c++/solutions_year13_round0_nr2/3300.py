//#include "stdafx.h"

#ifndef TOOLS_H
#define TOOLS_H

#include <vector>
#include <string>

#include "General.h"

typedef struct lawn
{
    U32  val;
    bool visited;
}LAWN;

bool compareMatrices(U32 row, U32 col, LAWN** array1, LAWN** array2);
void tokenize(string line, vector<string> &results);
void fillArray(LAWN** array, U32 row, U32 col, U32 val);
void fillArray(LAWN** array, U32 row, U32 col, string line);
void showArray(U32 row, U32 col, LAWN** array);
void delete2DimArray(LAWN** &array, U32 row);
LAWN** create2DimArray(U32 row, U32 col);
U32    getHexInput(ifstream &inputFile);
bool   isPalindrome(U32 value);

#endif //TOOLS_H
