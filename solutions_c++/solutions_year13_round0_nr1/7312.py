// Tic-Tac-Toe-Tomek.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int _tmain(int argc, _TCHAR* argv[])
{
	string n;
	int N;
	ofstream output;
	ifstream input;
	output.open("C:/Users/mkara_000/Downloads/karara2.in");
	input.open("C:/Users/mkara_000/Downloads/A-large.in");
	getline(input,n);
	N = stoi(n);
	char board[4][4];
	string line;
	bool xWins = false;
	bool oWins = false;
	bool notComplete = false;
	for(int t = 1 ; t<=N ; t++)
	{
		getline(input,line);
		board[0][0] = line[0];
		board[0][1] = line[1];
		board[0][2] = line[2];
		board[0][3] = line[3];
		getline(input,line);
		board[1][0] = line[0];
		board[1][1] = line[1];
		board[1][2] = line[2];
		board[1][3] = line[3];
		getline(input,line);
		board[2][0] = line[0];
		board[2][1] = line[1];
		board[2][2] = line[2];
		board[2][3] = line[3];
		getline(input,line);
		board[3][0] = line[0];
		board[3][1] = line[1];
		board[3][2] = line[2];
		board[3][3] = line[3];
	
		//row scan;
		int xRow = 0;
		int oRow = 0;
		for(int i = 0 ; i<4 ; i++)
		{
			for(int j = 0 ; j<4 ; j++)
			{
				if( board[i][j] == 'X' )
				{
					xRow++;
				
				}
				else if( board[i][j] == 'O' )
				{
					oRow  ++;
				
				}
			
				else if( board[i][j] == 'T' )
				{
					oRow  ++;
					xRow  ++;
				}
			
			}
			if( xRow == 4)
			{
				xWins = true;
				break;
			}
			else if ( oRow == 4)
			{
				oWins = true;
				break;
			}
			oRow = 0;
			xRow = 0;
		}
		// col scan
		int xCol = 0;
		int oCol = 0;
		int xDiag = 0;
		int oDiag = 0;

		for(int i = 0 ; i<4 ; i++)
		{
			for(int j = 0 ; j<4 ; j++)
			{
				
				
				if( board[j][i] == 'X' )
				{
					xCol++;
				
				}
				else if( board[j][i] == 'O' )
				{
					oCol  ++;
				
				}
			
				else if( board[j][i] == 'T' )
				{
					oCol  ++;
					xCol  ++;
				}
				
			}
			if( xCol == 4)
			{
				xWins = true;
				break;
			}
			else if ( oCol == 4)
			{
				oWins = true;
				break;
			}
			oCol = 0;
			xCol = 0;
			
		}
		// diagonal scan
		for(int i = 0 ; i<4 ; i++)
		{
			for(int j = 0 ; j<4 ; j++)
			{
			if( i == j){
						if( board[j][i] == 'X' )
					{
						xDiag++;
				
					}
					else if( board[j][i] == 'O' )
					{
						oDiag  ++;
				
					}
			
					else if( board[j][i] == 'T' )
					{
						oDiag  ++;
						xDiag  ++;
					}

					}
			
			if( xDiag == 4)
			{
				xWins = true;
				
			}
			else if ( oDiag == 4)
			{
				oWins = true;
				
			}
			}
		}
		xDiag = 0;
		oDiag =  0;

		for(int i = 0 ; i<4 ; i++)
		{
			for(int j = 0 ; j<4 ; j++)
			{
				if( (i + j) == 3 ){
						if( board[i][j] == 'X' )
							{
								xDiag++;
				
							}
							else if( board[i][j] == 'O' )
							{
								oDiag  ++;
				
							}
			
							else if( board[i][j] == 'T' )
							{
								oDiag  ++;
								xDiag  ++;
							}
					}
			}

			if( xDiag == 4)
			{
				xWins = true;
				
			}
			else if ( oDiag == 4)
			{
				oWins = true;
				
			}
		}
		for(int i = 0 ; i<4 ; i++)
		{
			for(int j = 0 ; j<4 ; j++)
			{
				if(board[i][j] == '.')
					notComplete = true;
			}
		}
		if(xWins){
			output<<"Case #"<<t<<": X won"<<endl;
		}
		else if(oWins){
			output<<"Case #"<<t<<": O won"<<endl;
		}
		else if(notComplete){
			output<<"Case #"<<t<<": Game has not completed"<<endl;
		}
		else
			output<<"Case #"<<t<<": Draw"<<endl;
		xWins = false;
		oWins = false;
		notComplete = false;
		getline(input,line);
	}
	output.close();
	input.close();

	
	return 0;
}

