#pragma once

#include <fstream>
#include <iostream>
#include <string>

using namespace std;

enum CaseOutput
{
	XWIN,
	OWIN,
	DRAW,
	UNFINISHED
};

CaseOutput checkResult(char *tableau)
{
	for(int colI = 0; colI < 4; colI++) //verification sur les colonnes
	{
		//check for X win
		bool Xwin = (tableau[colI] == 'X' || tableau[colI] == 'T');
		Xwin = Xwin && (tableau[colI + 4] == 'X' || tableau[colI + 4] == 'T');
		Xwin = Xwin && (tableau[colI + 8] == 'X' || tableau[colI + 8] == 'T');
		Xwin = Xwin && (tableau[colI + 12] == 'X' || tableau[colI + 12] == 'T');

		if(Xwin)
			return XWIN;

		bool Owin = (tableau[colI] == 'O' || tableau[colI] == 'T');
		Owin = Owin && (tableau[colI + 4] == 'O' || tableau[colI + 4] == 'T');
		Owin = Owin && (tableau[colI + 8] == 'O' || tableau[colI + 8] == 'T');
		Owin = Owin && (tableau[colI + 12] == 'O' || tableau[colI + 12] == 'T');

		if(Owin)
			return OWIN;
	}

	for(int rowI = 0; rowI < 4; rowI++) //verification sur les lignes
	{
		bool Xwin = (tableau[4*rowI] == 'X' || tableau[4*rowI] == 'T');
		Xwin = Xwin && (tableau[4*rowI + 1] == 'X' || tableau[4*rowI + 1] == 'T');
		Xwin = Xwin && (tableau[4*rowI + 2] == 'X' || tableau[4*rowI + 2] == 'T');
		Xwin = Xwin && (tableau[4*rowI + 3] == 'X' || tableau[4*rowI + 3] == 'T');

		if(Xwin)
			return XWIN;

		bool Owin = (tableau[4*rowI] == 'O' || tableau[4*rowI] == 'T');
		Owin = Owin && (tableau[4*rowI + 1] == 'O' || tableau[4*rowI + 1] == 'T');
		Owin = Owin && (tableau[4*rowI + 2] == 'O' || tableau[4*rowI + 2] == 'T');
		Owin = Owin && (tableau[4*rowI + 3] == 'O' || tableau[4*rowI + 3] == 'T');

		if(Owin)
			return OWIN;
	}

	//diagonales
	bool Xwin = (tableau[0] == 'X' || tableau[0] == 'T');
	Xwin = Xwin && (tableau[5] == 'X' || tableau[5] == 'T');
	Xwin = Xwin && (tableau[10] == 'X' || tableau[10] == 'T');
	Xwin = Xwin && (tableau[15] == 'X' || tableau[15] == 'T');

	if(Xwin)
		return XWIN;

	bool Owin = (tableau[0] == 'O' || tableau[0] == 'T');
	Owin = Owin && (tableau[5] == 'O' || tableau[5] == 'T');
	Owin = Owin && (tableau[10] == 'O' || tableau[10] == 'T');
	Owin = Owin && (tableau[15] == 'O' || tableau[15] == 'T');

	if(Owin)
		return OWIN;

	Xwin = (tableau[3] == 'X' || tableau[3] == 'T');
	Xwin = Xwin && (tableau[6] == 'X' || tableau[6] == 'T');
	Xwin = Xwin && (tableau[9] == 'X' || tableau[9] == 'T');
	Xwin = Xwin && (tableau[12] == 'X' || tableau[12] == 'T');

	if(Xwin)
		return XWIN;

	Owin = (tableau[3] == 'O' || tableau[3] == 'T');
	Owin = Owin && (tableau[6] == 'O' || tableau[6] == 'T');
	Owin = Owin && (tableau[9] == 'O' || tableau[9] == 'T');
	Owin = Owin && (tableau[12] == 'O' || tableau[12] == 'T');

	if(Owin)
		return OWIN;

	//compte du nombre de point pour voir si on a fini
	for(int i = 0; i < 16; i++)
	{
		if(tableau[i] == '.')
			return UNFINISHED;
	}

	return DRAW;

}

int main(int argc, char **argv)
{
	ifstream input(argv[1]);
	ofstream ouput("output.out");

	int nbCase;
	input >> nbCase;

	char garbageChar;

	//input >> garbageChar;
	for(int i = 0; i < nbCase; i++)
	{
		char tableau[16];
		char *tablePtr = tableau;

		//récupération du tableau courant
		for(int colI = 0; colI < 4; colI++)
		{
			for(int rowI = 0; rowI < 4; rowI++)
			{
				char currentChar;
				input >> currentChar;
				*tablePtr = currentChar;
				tablePtr++;
			}
			//input >> garbageChar;
		}
		//input >> garbageChar;

		CaseOutput caseOutput = checkResult(tableau);

		ouput << "Case #" << i+1 << ": ";
		switch(caseOutput)
		{
		case DRAW:
			ouput << "Draw" << endl;
			break;
		case UNFINISHED:
			ouput << "Game has not completed" << endl;
			break;
		case XWIN:
			ouput << "X won" << endl;
			break;
		case OWIN:
			ouput << "O won" << endl;
			break;
		}
	}
	return 0;
}