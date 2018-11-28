#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main () {
	int cases;
	ifstream mfr ("A-large.in");
	
	vector<string> outPut;
	if (mfr.is_open())
	{
		string line;
		getline (mfr,line);	
		cases = atoi(line.c_str());
		int matrix[4][4];
		char T = 'T';
		char X = 'X';
		char O = 'O';
		char Dot = '.';
		
		int Tval = T;
		int Xval = X;
		int Oval = O;
		int DotVal = Dot;
		
		int Xwin1 = Xval * 4;
		int Xwin2 = Xval * 3 + Tval;
		
		int Owin1 = Oval * 4;
		int Owin2 = Oval * 3 + Tval;
		
		int totalT = Tval + Xval*8 + Oval*7;
		int total = Xval*8 + Oval*8;
		
		int testCaseNo = 0;
		while (testCaseNo < cases)
		{
			for( int i=0; i<4; i++)
			{
				getline (mfr,line);
				for( int j=0; j<4; j++)
				{
					matrix[i][j] = line[j];
				}
			}
			int value1,value2,value3,value4,total2;
			value3 = 0;value4 = 0;total2 = 0;
			bool someOneWon = false;
			for( int i=0; i<4; i++)
			{
				value1 = matrix[i][0] + matrix[i][1] + matrix[i][2] + matrix[i][3];
				value2 = matrix[0][i] + matrix[1][i] + matrix[2][i] + matrix[3][i];
				value3 = value3 + matrix[i][i];
				value4 = value4 + matrix[3-i][i];
				
				if( ( value1 == Xwin1) || ( value1 == Xwin2) ||  value2 == Xwin1 ||  value2 == Xwin2 || value3 == Xwin1 ||  value3 == Xwin2 || value4 == Xwin1 ||  value4 == Xwin2)
				{
					outPut.push_back("X won");
					someOneWon = true;
					break;
				}
				if( value1 == Owin1 ||  value1 == Owin2 ||  value2 == Owin1 ||  value2 == Owin2 || value3 == Owin1 ||  value3 == Owin2 || value4 == Owin1 ||  value4 == Owin2)
				{
					outPut.push_back("O won");
					someOneWon = true;
					break;
				}
				total2 = total2 + value1;
			}
			if( !someOneWon)
			{
				if( ( value3 == Xwin1) || ( value3 == Xwin2) || ( value4 == Xwin1) || ( value4 == Xwin2))
				{
					outPut.push_back("X won");
					someOneWon = true;
				}
				else if( ( value3 == Owin1) || ( value3 == Owin1) || ( value4 == Owin1) || ( value4 == Owin1))
				{
					outPut.push_back("O won");
					someOneWon = true;
				}
				else
				{
					if( total == total2 || totalT == total2)
						outPut.push_back("Draw");
					else
						outPut.push_back("Game has not completed");
				}
			}
			getline (mfr,line);
			testCaseNo++;
		}
		mfr.close();
	}
	
	ofstream mfw ("A-large.out");
	if (mfw.is_open())
	{
		int lines = outPut.size() - 1;
		for( int i = 0; i < lines; i++)
		{
			mfw << "Case #"<< (i+1) << ": " << outPut[i] << "\n";
		}
		mfw << "Case #"<< outPut.size() << ": " << outPut[outPut.size() - 1];
		mfw.close();
	}

	return 0;
}
