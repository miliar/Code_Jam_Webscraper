
#include "StdAfx.h"
#include <string>
#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
using namespace std;
 
#define TAB_COLUMNS 4
#define TAB_ROWS 4
#define WIN_NBR 4

char aTab[TAB_COLUMNS][TAB_ROWS];

string CheckTab()
{
	int icount = 0;
	char cWinner = NULL;
	char cprev;

	// check rows
	for (int i=0; i<TAB_ROWS; i++)
	{
		icount = 0;
		cWinner = NULL;
		for (int j=1; j<TAB_COLUMNS; j++)
		{
			if ( ( (aTab[i][j] == aTab[i][j-1]) || (aTab[i][j] == 'T') || (aTab[i][j-1] == 'T') ) && (aTab[i][j] != '.') )
			{
				if (aTab[i][j-1] == 'T')
				{
					if ( (j>1) && (cWinner == aTab[i][j]) )
						icount++;
				}
				else
				{
					icount++;
				}
				if (aTab[i][j] != 'T')
					cWinner = aTab[i][j];

			}
			else
			{
				icount = 0;
				cWinner = NULL;
			}
			
			if (icount == WIN_NBR-1)
			{
				char szresult[100];
				sprintf(szresult, "%c won", cWinner);
				return szresult;
			}
		}
	}

	// check cols
	for (int j=0; j<TAB_COLUMNS; j++)
	{
		icount = 0;
		cWinner = NULL;
		for (int i=1; i<TAB_ROWS; i++)
		{
			if ( ( (aTab[i][j] == aTab[i-1][j]) || (aTab[i][j] == 'T') || (aTab[i-1][j] == 'T') ) && (aTab[i][j] != '.') )
			{
				if (aTab[i-1][j] == 'T')
				{
					if ( (i>1) && (cWinner == aTab[i][j]) )
						icount++;
				}
				else
				{
					icount++;
				}
				if (aTab[i][j] != 'T')
					cWinner = aTab[i][j];
			}
			else
			{
				icount = 0;
				cWinner = NULL;
			}
			
			if (icount == WIN_NBR-1)
			{
				char szresult[100];
				sprintf(szresult, "%c won", cWinner);
				return szresult;
			}
		}
	}

	// check diag 1
	int j = 0;
	for (int i=0; i<TAB_ROWS; i++)
    {
		if ( ( (aTab[i][j] == aTab[i+1][j+1]) || (aTab[i][j] == 'T') || (aTab[i+1][j+1] == 'T') ) && (aTab[i+1][j+1] != '.') )
		{
				if (aTab[i+1][j+1] == 'T')
				{
					if ( (i>1) && (cWinner == aTab[i][j]) )
						icount++;
				}
				else
				{
					icount++;
				}
				if (aTab[i][j] != 'T')
					cWinner = aTab[i][j];
		}
		else
		{
			icount = 0;
			cWinner = NULL;
		}
			
		if (icount == WIN_NBR-1)
		{
			char szresult[100];
			sprintf(szresult, "%c won", cWinner);
			return szresult;
		}
		j++;
	}

	// check diag 2
	int k = TAB_COLUMNS-1;
	for (int i=0; i<TAB_ROWS; i++)
    {
		if ( ( (aTab[i][k] == aTab[i+1][k-1]) || (aTab[i][k] == 'T') || (aTab[i+1][k-1] == 'T') ) && (aTab[i+1][k-1] != '.') )
		{
				if (aTab[i+1][k-1] == 'T')
				{
					if ( (i>1) && (cWinner == aTab[i][k]) )
						icount++;
				}
				else
				{
					icount++;
				}
				if (aTab[i][k] != 'T')
					cWinner = aTab[i][k];
		}
		else
		{
			icount = 0;
			cWinner = NULL;
		}
			
		if (icount == WIN_NBR-1)
		{
			char szresult[100];
			sprintf(szresult, "%c won", cWinner);
			return szresult;
		}
		k--;
	}

	// check full
	for (int i=0; i<TAB_ROWS; i++)
	{
		for (int j=1; j<TAB_COLUMNS; j++)
		{
			if (aTab[i][j] == '.')
				return "Game has not completed";
		}
	}

	return "Draw";
}

int main()
{
  ifstream in( "D:\\DEV\\INPUT\\A-small-attempt1.in" );
  ofstream outfile( "D:\\DEV\\OUTPUT\\TicTacToeSmall.out" );
  string line;
  getline( in, line );
  int numCases = atoi( line.c_str() );
 
  for (int ncases=0; ncases<numCases; ncases++)
  { 
	for (int nrow=0; nrow<TAB_ROWS+1; nrow++)
	{
		getline(in, line); 
		if (line != "")
		{
			for (int ncol=0; ncol<TAB_COLUMNS; ncol++)
			{
				aTab[nrow][ncol] = line[ncol];
			}
		}
	}
	string strresult = CheckTab();
	outfile<<"Case #"<<ncases+1<<": "<<strresult<<endl;  // and write out
  }
  return 0;
}
