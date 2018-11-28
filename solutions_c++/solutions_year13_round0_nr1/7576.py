#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>

int value1 = 0;
int value2 = 0;
using namespace std;
int checkResult(int checkValue, int player)
{
	int diagonalMask1 = 33825;
	int diagonalMask2 = 4680;

	if((checkValue & diagonalMask1) == diagonalMask1 || (checkValue & diagonalMask2) == diagonalMask2)
	{
		return 1;
	}

	int rowMask = 15;
	int lowMask = 4369;
	int mask = 15;
	for(int i=0; i!=4; i++)
	{
		if( (checkValue & rowMask) == rowMask || (checkValue & lowMask) == lowMask)
		{
			return 1;
		}
		else
		{
			rowMask = rowMask << 4;
			lowMask = lowMask << 1;

		}
	}

	return 0;

}


void readFile()
{
	value1 = 0;
	value2 = 0;
	
	bool isFullFlag = false;

	char getLine[50];
	char resultChar[50];
	string resultLine;
	int list = 0;
	int result = 0;
	std::ifstream fin;
	std::ofstream fout;

	fin.open(L"A-large.in");
	fout.open(L"out.txt");
	fin.getline(getLine, 50);

	list = atoi(getLine);

	for(int z = 0 ; z!= list; z++)
	{
		for(int j=0; j!=4; j++)
		{
			fin.getline(getLine, 50);

			for(int i=0; i!=4; i++)
			{
				if(getLine[i] == 'X')
				{
					value1 = value1 + (1 << i+ (j*4)) ;
				}
				else if(getLine[i] =='O')
				{
					value2 = value2 + (1 << i+(j*4)) ;
				}
				else if(getLine[i] == 'T')
				{
					value1 = value1 + (1 << i+(j*4)) ;
					value2 = value2 + (1 << i+(j*4)) ;
				}


			}
			
		}

		if((value1 | value2) ==  65535)
		{
			isFullFlag = true;
		}

		fin.getline(getLine, 50);
		result = checkResult(value1, 1);
		if(result == 1)
		{
			
			 fout << "Case #" << z+1 << ": X won" << endl;
		}
		else if(result == 0)
		{
			result = checkResult(value2, 2);

			if(result == 1)
			{
				fout << resultLine << "Case #" << z+1 << ": O won" << endl;
			}
			else 
			{
				if(isFullFlag == true)
				{
					fout << resultLine << "Case #" << z+1 << ": Draw" << endl;
				}
				else if(isFullFlag == false)
				{
					fout << resultLine << "Case #" << z+1 << ": Game has not completed" << endl;
				}
				
			}
		}

		isFullFlag = false;
		value1 = 0;
		value2 = 0;
		
	}
	fin.close();
	fout.close();
}


void main()
{
	readFile();
}