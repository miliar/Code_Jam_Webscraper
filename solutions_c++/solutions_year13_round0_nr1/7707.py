// ConsoleApplication1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
using namespace std;

void solveTicTac(char *str){
	int totalNum = 0;
	short board = 0;
	short maskX = 0;
	short maskDot = 0;
	short firstRowMask = -4096;
	short secondRowMask = 3840;
	short thirdRowMask = 240;
	short forthRowMask = 15;
	short firstColMask = -30584;
	short secondColMask = 17476;
	short thirdColMask = 8738;
	short forthColMask = 4369;
	short firstDiagonalMask = -31711;
	short secondDiagonalMask = 4680;

	char tmp;

	fstream fsOut;
	fsOut.open("output.out", ios::out);

	fstream fs;
	fs.open(str, ios::in);
	fs >> totalNum;
	
	for (int k = 1; k <= totalNum; k++){
		board = 0;
		maskX = 0;
		maskDot = 0;

		for (int i = 0; i < 16; i++){
			fs >> tmp;
			switch (tmp){
			case '.':
				maskDot |= (1 << (15-i));
				break;
			case 'X':
				board |= (1 << (15-i));
				break;
			case 'T':
				maskX |= (1 << (15-i));
				break;
			}
		}
		
		board |= maskDot;

		if (((board & firstRowMask) == 0) || ((board & secondRowMask) == 0) || ((board & thirdRowMask) == 0) || ((board & forthRowMask) == 0)
			|| ((board & firstColMask) == 0) || ((board & secondColMask) == 0) || ((board & thirdColMask) == 0) || ((board & forthColMask) == 0)
			|| ((board & firstDiagonalMask) == 0) || ((board & secondDiagonalMask) == 0)){
			fsOut << "Case #" << k << ": O won" << endl;
			continue;
		}

		board ^= maskDot;

		board |= maskX;

		if (((board | (~firstRowMask)) == -1) || ((board | (~secondRowMask)) == -1) || ((board | (~thirdRowMask)) == -1) || ((board | (~forthRowMask)) == -1)
			|| ((board | (~firstColMask)) == -1) || ((board | (~secondColMask)) == -1) || ((board | (~thirdColMask)) == -1) || ((board | (~forthColMask)) == -1)
			|| ((board | (~firstDiagonalMask)) == -1) || ((board | (~secondDiagonalMask)) == -1)){
			fsOut << "Case #" << k << ": X won" << endl; 
			continue;
		}

		if (maskDot == 0){
			fsOut << "Case #" << k << ": Draw" << endl;
			continue;
		}

		fsOut << "Case #" << k << ": Game has not completed" << endl;
	}

	fs.close();
	fs.close();
}

int _tmain(int argc, _TCHAR* argv[])
{
	solveTicTac("A-large.in");
	return 0;
}

