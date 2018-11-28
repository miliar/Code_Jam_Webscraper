/******************************************************************************
Author: Jonathan Lam
Project Name: ttt.cpp
Compiler: Dev C++
Due Date: 5/12/2012
******************************************************************************/
#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>

using namespace std;

char CheckStatus(char board[4][4]);

int main()
{    
    ifstream file;
    ofstream ofile;
    int trials = 0;
    char board[4][4];
    
    file.open("al.in");
    ofile.open("answer.in");    
    
    file >> trials;
    
    for (int i = 0; i < trials; i++)		
    {
    	ofile<<"Case #"<<i+1<<": ";
    	
		for (int y = 0; y < 4; y++)			//Fill board
    		for (int x = 0; x < 4; x++)
    			file >> board[y][x];  
    			
    							
	    	switch (CheckStatus(board))
	    	{
				case 'X':	ofile<<"X won\n";
	    					break;
	    		case 'O':	ofile<<"O won\n";
	    					break;
	    		case 'C':	ofile<<"Game has not completed\n";
	    					break;
	    		default:	ofile<<"Draw\n";
	    		
	    	}
    			
    }
	
	
	  
    file.close();
    ofile.close();
    return 0;
}

char CheckStatus(char board[4][4])
{
		for (int row = 0; row < 4; row++)							//Rows
		{
    		if ((board[row][0] == 'X' || board[row][0] == 'T') &&
    			(board[row][1] == 'X' || board[row][1] == 'T') &&
    			(board[row][2] == 'X' || board[row][2] == 'T') &&
    			(board[row][3] == 'X' || board[row][3] == 'T'))    			
    				return 'X';
    		if ((board[row][0] == 'O' || board[row][0] == 'T') &&
    			(board[row][1] == 'O' || board[row][1] == 'T') &&
    			(board[row][2] == 'O' || board[row][2] == 'T') &&
    			(board[row][3] == 'O' || board[row][3] == 'T'))    			
    				return 'O';
    	}
    			
    		
    	for (int col = 0; col < 4; col++)							//columns
    	{
    		if ((board[0][col] == 'X' || board[0][col] == 'T') &&
    			(board[1][col] == 'X' || board[1][col] == 'T') &&
    			(board[2][col] == 'X' || board[2][col] == 'T') &&
    			(board[3][col] == 'X' || board[3][col] == 'T'))
    				return 'X';
    		if ((board[0][col] == 'O' || board[0][col] == 'T') &&
    			(board[1][col] == 'O' || board[1][col] == 'T') &&
    			(board[2][col] == 'O' || board[2][col] == 'T') &&
    			(board[3][col] == 'O' || board[3][col] == 'T'))
    				return 'O';
    }
    				
    	if ((board[0][0] == 'X' || board[0][0] == 'T') &&	//Diagonal 1
    		(board[1][1] == 'X' || board[1][1] == 'T') &&
    		(board[2][2] == 'X' || board[2][2] == 'T') &&
    		(board[3][3] == 'X' || board[3][3] == 'T'))
    			return 'X';
    	if ((board[0][0] == 'O' || board[0][0] == 'T') &&
    		(board[1][1] == 'O' || board[1][1] == 'T') &&
    		(board[2][2] == 'O' || board[2][2] == 'T') &&
    		(board[3][3] == 'O' || board[3][3] == 'T'))
    			return 'O';
    				
    	if ((board[0][3] == 'X' || board[0][3] == 'T') &&	//Diagonal 2
    		(board[1][2] == 'X' || board[1][2] == 'T') &&
    		(board[2][1] == 'X' || board[2][1] == 'T') &&
    		(board[3][0] == 'X' || board[3][0] == 'T'))
    			return 'X';
    	if ((board[0][3] == 'O' || board[0][3] == 'T') &&
    		(board[1][2] == 'O' || board[1][2] == 'T') &&
    		(board[2][1] == 'O' || board[2][1] == 'T') &&
    		(board[3][0] == 'O' || board[3][0] == 'T'))
    			return 'O';
    			
    	for (int y = 0; y < 4; y++)			//game not complete
    		for (int x = 0; x < 4; x++)
    			if (board[y][x] == '.')
    				return 'C';
    			
    	return 0;
}



















