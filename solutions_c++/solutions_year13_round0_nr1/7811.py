#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <algorithm>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <assert.h>
using namespace std;


long solve(char grid[][5] )
{
	long result = 0;
	long nbXd1, nbXd2,nbOd1, nbOd2,nbTd1,nbTd2, nbDot;
	nbXd1=nbXd2=nbOd1=nbOd2=nbTd1=nbTd2= 0;
	nbDot = 0;

	for (int i =0; i<4; i++)
	{
		//diag1
		if(grid[i][i]=='X')
			nbXd1++;
		else if(grid[i][i]=='O')
			nbOd1++;
		else if(grid[i][i]=='T')
			nbTd1++;
		//diag2
		if(grid[i][3-i]=='X')
			nbXd2++;
		else if(grid[i][3-i]=='O')
			nbOd2++;
		else if(grid[i][3-i]=='T')
			nbTd2++;


		long nbX, nbO,nbT;
		long nbXc, nbOc,nbTc;
		
		nbX=nbO=nbT=0;
		nbXc = nbOc = nbTc = 0;
        for(int j = 0; j<4; j++)
		{
			//line
            if(grid[i][j]=='X')
				nbX++;
			else if(grid[i][j]=='.')
				nbDot++;
			else if(grid[i][j]=='O')
				nbO++;
			else if(grid[i][j]=='T')
				nbT++;
			//column 
			if(grid[j][i]=='X')
				nbXc++;
			else if(grid[j][i]=='.')
				nbDot++;
			else if(grid[j][i]=='O')
				nbOc++;
			else if(grid[j][i]=='T')
				nbTc++;
			//diag1
			nbXd1++;

		}

		if((nbX==4) || (nbX+nbT ==4) || (nbXc==4) || (nbXc+nbTc ==4))
			return 1;
		if((nbO==4) || (nbO+nbT ==4) || (nbOc==4) || (nbOc+nbTc ==4))
			return 2;
	}

	if((nbXd1==4) || (nbXd1+nbTd1 ==4) || (nbXd2==4) || (nbXd2+nbTd2 ==4))
		return 1;
	if((nbOd1==4) || (nbOd1+nbTd1 ==4) || (nbOd2==4) || (nbOd2+nbTd2 ==4))
		return 2;


	if(nbDot != 0)
		result = 3;
	else
		result = 4;
	return result;
}


int _tmain(int argc, _TCHAR* argv[])
{
	int numCase = 0;
	
	cin >> numCase;

	for (int i = 0; i < numCase; i++)
	{
		char grid[5][5];
		for(int j=0;j<4;j++)
		{
			string line;
			cin >> grid[j];
		}

		cin.ignore();

		cout << "Case #" << (i+1) << ": ";
		
		switch(solve(grid))
		{
			case 1:
				cout << "X won";
				break;
			case 2:
				cout << "O won";
				break;
			case 3:
				cout << "Game has not completed";
				break;
			case 4:
				cout << "Draw";
				break;
		}
		cout << endl;
	}

	return 0;
}



