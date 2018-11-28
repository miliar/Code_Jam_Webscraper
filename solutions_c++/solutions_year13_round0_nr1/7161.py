// codejam2013.cpp : main project file.

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace System;
using namespace std;

const int BOARD_SIZE=4;

void analyze(string[BOARD_SIZE],int);
void writeresult(int flag,int);

int main(array<System::String ^> ^args)
{
 // char board[BOARD_SIZE][BOARD_SIZE];
  
  
  ifstream myfile ("A-large.in");
	int n = 0;
	if (myfile.is_open())
  {
	  string line1;
	 /* char c = myfile.get();
	  n = c-48;*/
	  getline(myfile,line1);
	  std::stringstream ss(line1);
	  ss>>n;
	  int i = 0;
	  int row = 0;
	  string board[4];
    while (myfile.good() && i < n)
    {
		string line;
      getline (myfile,line);
	  
	  if(line.empty()) {
		  //break;
		  i++;
		  row = 0;
		 // cout << '\n';
		  analyze(board,i);
		  
		  continue;
	  }
	  board[row] = line;
	 // cout << board[row] <<'\n';
	  row++;
      //cout << line << endl;
    }
	
    myfile.close();
  }
	else cout << "Unable to open file"; 
   system ("pause");
    return 0;
}

void analyze(string board[BOARD_SIZE], int caseno )
{
	
	int incompleteLine = 0;
	int backDiagScore = 0;
	int diagScore = 0;
	for(int i = 0; i < 4; i++)
	{
		if(board[i][BOARD_SIZE-i-1] == 'X')
		{	
			backDiagScore +=2;
	
		}
		if(board [i][BOARD_SIZE-i-1] == 'O')
		{
			backDiagScore += 10;
	
		}
		if(board[i][BOARD_SIZE-i-1] == 'T')
		{
			backDiagScore += 1;
		}

		
		if(board[i][i] == 'X')
		{
			diagScore +=2;
	
		}
		if(board [i][i] == 'O')
		{
			diagScore += 10;
	
		}
		if(board[i][i] == 'T')
		{
			diagScore += 1;
	
		}
	}

	if(diagScore == 7 || diagScore == 8 || backDiagScore == 7 || backDiagScore == 8)
	{
		writeresult(0,caseno);
		return;
	}
	else if(diagScore == 31 || diagScore == 40 || backDiagScore == 40 || backDiagScore == 31)
	{
		writeresult(1,caseno);
		return;
	}

	

	for(int i = 0; i < 4; i++)
	{
		
		int score = 0;
		int scoreV = 0;    	
		for(int j = 0; j < board[i].size(); j++)
		{
			if(board[i][j] == '.')
			{
				incompleteLine++;
			
			}

			if(board[i][j] == 'X')
			{
				score += 2;
				
			}

			if(board[i][j] == 'O')
			{
				score += 10;			
				
			}
			if(board[i][j] == 'T')
			{
				score +=1;
				
			}

			if(board[j][i] == 'X')
				scoreV += 2;
			if(board[j][i] == 'O')
				scoreV += 10;
			if(board[j][i] == 'T')
				scoreV +=1;
		}

		if(score == 7 || score == 8 || scoreV == 7 || scoreV == 8)
		{
			writeresult(0, caseno);
			return;
		}
		else if (score == 31 || score == 40 || scoreV == 31 || scoreV == 40)
		{
			writeresult(1,caseno);
			return;
		}
		
	}

	 if(incompleteLine == 0)
		{
			writeresult(2,caseno);
			return;
		}
	else 
		{
			writeresult(3,caseno);
		}
		return;
	/*for(int i = 0; i < BOARD_SIZE; i++)
	{
		if(checkHorizontal(board[i]))
		{
			return;
		}		
	}
	for(int i = 0; i < BOARD_SIZE; i++)
	{
		if(checkVertical(board[i])
		{
			return;
		}
	}*/
}

void writeresult(int flag, int caseno)
{
  fstream filestr;
  filestr.open ("smalloutput.txt", fstream::in | fstream::out | fstream::ate);
  if(flag == 0)
  {
	  filestr << "Case #"<<caseno << ": X won\n";
  }
  else if(flag == 1) {
	  filestr << "Case #"<<caseno << ": O won\n";
  }
  else if(flag == 2)
  {
	  filestr << "Case #"<<caseno << ": Draw\n";
  }
  else
	 filestr << "Case #"<<caseno << ": Game has not completed\n";
  filestr.close();
}