#include <iostream>
#include <stdio.h>
#include <sstream>
#include <string.h>
#include <math.h>
#include <fstream>

char m[4][4];
int getState()
{
	const char size = 4;
	char res = 0;
	//check first line
	for (int i = 0; i<size; ++i)
	{
		//check diagonal
		if (m[0][i] == '.') continue;
		if ((i == 0) && (res = m[0][0] & m[1][1] & m[2][2] & m[3][3]))
		{
			return res;
		} 
		else if ((i == (size-1)) && (res = m[0][i] & m[1][2] & m[2][1] & m[3][0]))
		{
			return res;
		}

		//check vertical
		if (res = m[0][i] & m[1][i] & m[2][i] & m[3][i])
		{
			return res;
		}
	}

	//check first column
	for (int i = 0; i<size; ++i)
	{
		if (m[i][0] == '.') continue;
		//check horizontal
		if (res = m[i][0] & m[i][1] & m[i][2] & m[i][3])
		{
			return res;
		}
	}
	return 0;
}

int main(int argc, char *argv[]) {
  ifstream inputfile ("infile.txt");
  ofstream outfile ("outfile.txt");
  if (inputfile.is_open())
  {
	  int testNum;
	  inputfile >> testNum;
	  ofstream outfile ("outfile.txt");
	  for (int i = 0; i < testNum; ++i)
	  {
		  bool dots = false;
		  outfile << "Case #" << i+1 << ": ";
		  for (int i=0; i<4; ++i) {
			  for (int j=0; j<4; ++j) 
			  {
				  inputfile >> m[i][j];
				  if (m[i][j] == '.') {
					  m[i][j] = 0;
					  dots = true;
				  }
				  if (m[i][j] == 'X') m[i][j] = 1;
				  if (m[i][j] == 'O') m[i][j] = 2;
				  if (m[i][j] == 'T') m[i][j] = 3;
				  //cout << " " << m[i][j];
			  }
		  }
		  switch (getState()) {
			case 1:
				outfile << "X won" << endl;
				break;
			case 2:
				outfile << "O won" << endl;
				break;
			case 0:
				if (!dots)
					outfile << "Draw" << endl;
				else
					outfile << "Game has not completed" << endl;
				break;
			default:
					cout << "Error" << endl;
				break;
		  }
	  }
  }
}