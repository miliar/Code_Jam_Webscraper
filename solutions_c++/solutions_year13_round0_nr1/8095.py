
#include<iostream>
#include<fstream>
#include <string>
//#include <cmath>

using namespace std;

int main() {

 string inputFileName = "input.txt";
 ifstream inputFile(inputFileName.c_str());

 string filename = "output.txt";
 ofstream outputFile;
 outputFile.open( filename.c_str(), ios_base::out );

 int numOfCases = 0;
 char board[4][4];
 int xOfT = -1;
 int yOfT = -1;
 int result = 0;
 int countX = 0;
 int countX_T = 0;
 int countO = 0;
int countO_T = 0;
int c = 0;
int h = 3;
int f = 0;
				int t = 3;
 //open the file
	if(inputFile.is_open())
	{
		inputFile >> numOfCases;
		cout << numOfCases << endl;
		
		for(int i = 1; i <= numOfCases; i++)
		{
			//initalize tempro. board.
			for(int k = 0; k < 4; k++)
				for(int j = 0; j < 4; j++)
					inputFile >> board[k][j];

			//locate T
			for(int k = 0; k < 4; k++)
				for(int j = 0; j < 4; j++)
				{
					if (board[k][j] == 'T')
					{
						xOfT = k;
						yOfT = j;
						break;
					}
				}
		//	cout << xOfT << " " << yOfT << endl;
			//check horizontal
			countX = 0;
			countX_T = 0;
			for(int k = 0; k < 4; k++)
			{
				for(int j = 0; j < 4; j++)
				{
					if(k != xOfT)
					{
						if(board[k][j] == 'X')
							countX++;
					}
					else
					{
						if(board[k][j] == 'X')
							countX_T++;
					}
				}
				if(countX == 4 || countX_T == 3)
				{
					result = 1;
					goto output;
				}
				countX = 0; countX_T = 0;
			}
		//	cout << "check hor X" << endl;
		    countO = 0;
			countO_T = 0;
			for(int k = 0; k < 4; k++)
			{
				for(int j = 0; j < 4; j++)
				{
					if(k != xOfT)
					{
						if(board[k][j] == 'O')
							countO++;
					}
					else
					{
						if(board[k][j] == 'O')
							countO_T++;
					}
				}
				if(countO == 4 || countO_T == 3)
				{
					result = 2;
					goto output;
				}
				countO = 0; countO_T = 0;
			}
			countX = 0; countO = 0; countX_T = 0; countO_T = 0; //
		//	cout << "check hor O" << endl;
			//check columns
			for(int k = 0; k < 4; k++)
			{
				for(int j = 0; j < 4; j++)
				{
					if(k != yOfT)
					{
						if(board[j][k] == 'X')
							countX++;
					}
					else
					{
						if(board[j][k] == 'X')
							countX_T++;
					}
				}
			
				if(countX == 4 || countX_T == 3)
				{
					result = 1;
					goto output;
				}
				countX = 0; countX_T = 0;
			}
		//	cout << "check ver X" << endl;
			for(int k = 0; k < 4; k++)
			{
				
				for(int j = 0; j < 4; j++)
				{
					if(k != yOfT)
					{
						
						if(board[j][k] == 'O')
							countO++;
					}
					else
					{
						if(board[j][k] == 'O')
							countO_T++;
					}
				}
				if(countO == 4 || countO_T == 3)
				{
					result = 2;
					goto output;
				}
				countO = 0; countO_T = 0;
			}
		//	cout << "check ver O" << endl;
			countX = 0; countO = 0; countX_T = 0; countO_T = 0; //
			//check vertical
			//check if T is on the diagonal
			bool isTdiag = false;
			bool isTdiag_1 = false;
			if((xOfT == yOfT) && xOfT != -1)
				isTdiag = true;
			//cout << xOfT << yOfT << endl;
			//cout << "11 " << isTdiag << endl;
			if( ((xOfT == 0)&(yOfT == 3)) | ((xOfT == 1)&(yOfT == 2)) | ((xOfT == 2)&(yOfT == 1)) | ((xOfT == 3)&(yOfT == 0)) )
			{
				isTdiag_1 = true;
			}
			char currentChar = 'X';
			if(!isTdiag)
				for(int k = 0; k < 4; k++)
				{
					if(board[k][k] == 'X')
						countX++;
				}
			else
				for(int k = 0; k < 4; k++)
				{
					if(board[k][k] == 'X')
						countX_T++;
				}
			if(countX == 4 || countX_T == 3)
				{
					result = 1;
					goto output;
				}
			
			countX = 0; countX_T = 0;
			if(!isTdiag_1)
				if(currentChar == board[0][3] && currentChar == board[1][2] && currentChar == board[2][1] && currentChar == board[3][0])
				{
					result = 1;
					goto output;
				}
			if(isTdiag_1)
			{
				c = 0;
				 h = 3;
				while(c <4 && h > -1)
				{
					if(board[c][h] = 'X')
					countX_T++;
					h--;
					c++;
				}
				if(countX == 4 || countX_T == 3)
				{
					result = 1;
					goto output;
				}
			}
			
			countO = 0; countO_T = 0;
			currentChar = 'O';
			if(!isTdiag)
				for(int k = 0; k < 4; k++)
				{
					if(board[k][k] == currentChar)
						countO++;
				}
			else
				for(int k = 0; k < 4; k++)
				{
					if(board[k][k] == currentChar)
						countO_T++;
				}
			if(countO == 4 || countO_T == 3)
				{
					result = 2;
					goto output;
				}
			countO = 0; countO_T = 0;
			if(!isTdiag_1)
				if(currentChar == board[0][3] && currentChar == board[1][2] && currentChar == board[2][1] && currentChar == board[3][0])
				{
					result = 2;
					goto output;
				}
			if(isTdiag_1)
			{
				 f = 0;
				 t = 3;
				while(f <4 && t > -1)
				{
					if(board[f][t] = currentChar)
					countO_T++;
					f++;
					t--;
				}
				cout << countO_T << endl;
				if(countO == 4 || countO_T-1 == 3)
				{
					result = 2;
					goto output;
				}
			}
			//cout << "survive!" << endl;
			//if survives here either draw or has not complete
			//check complete
			for(int k = 0; k < 4; k++)
				for(int j = 0; j < 4; j++)
					if(board[k][j] == '.')
					{
						result = 3;
						goto output;
					}
			result = 4;
			countO = 0; countO_T = 0; countX = 0; countX_T = 0;
output:
		if(result == 1)
			outputFile << "Case " << "#" << i << ": " << "X won" << endl;
		if(result == 2)
			outputFile << "Case " << "#" << i << ": " << "O won" << endl;
		if(result == 3)
			outputFile << "Case " << "#" << i << ": " << "Game has not completed" << endl;
		if(result == 4)
			outputFile << "Case " << "#" << i << ": " << "Draw" << endl;
		result = 0;
		xOfT = -1;
		yOfT = -1;
		countO = 0; countO_T = 0; countX = 0; countX_T = 0;
		isTdiag = false;
		 isTdiag_1 = false;
		 c = 0;
				 h = 3;
		 f = 0;
			 t = 3;
		}//end of for loop
		
		//close the file
		inputFile.close();
		outputFile.close();
	}
	else
		cout << "cannot open the image file" << endl;

	
/*	//write into a file
	//Declare variables
	string filename = "output.txt";

	//Open a stream for the output file
	ofstream outputFile;
	outputFile.open( filename.c_str(), ios_base::out );

	//Close the output file stream
	outputFile.close();*/

}


		/*	for(int k = 0; k < 4; k++)
			{
				for(int j = 0; j < 4; j++)
					cout << board[k][j];
				cout << endl;
			}
			*/