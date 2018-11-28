// CJ13_TTT.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	fstream fsin("C:\\Users\\basu_lucifer\\Downloads\\A-large.in", ios::in), fsout("C:\\Users\\basu_lucifer\\Downloads\\output.out", ios::out | ios::trunc);
	int t;
	vector<string> mat(4);
	vector<string> str(4);
	str[0] = "Draw";
	str[1] = "X won";
	str[2] = "O won";
	str[3] = "Game has not completed";
	fsin >> t;
	for(int ts = 1; ts <=t; ++ts)
	{
		int k = 0; 
		int ct = 0;
		char c;
		bool unfilled = false;
		bool won = false;
		for(int i =0; i < 4; ++i)
			fsin >> mat[i];

		for(int i =0; i < 4; ++i)
		{
			ct = 0;
			c = mat[i][0];
			if( c == 'T' ) c = mat[i][1];
			for(int j =0; j < 4; ++j)
			{
				if((mat[i][j] == 'T') || (mat[i][j] == c)) ++ct;
				if(mat[i][j] == '.') unfilled = true;		
			}
			if((ct == 4) && (c=='X' || c=='O')) {won = true; break;}
		}
		if(!won)
		{
			for(int i = 0; i < 4; ++i)
			{
				ct = 0;
				c = mat[0][i];
				if( c == 'T' ) c = mat[1][i];
				for(int j =0; j < 4; ++j)
				{
					if((mat[j][i] == 'T') || (mat[j][i] == c)) ++ct;
					if(mat[j][i] == '.') unfilled = true;		
				}
				if((ct == 4) && (c=='X' || c=='O')) {won = true; break;}
			}
			if(!won)
			{
				ct = 0;
				c = mat[0][0];
				if(c == 'T') c = mat[1][1];
				for(int i = 0; i < 4; ++i)
				{
					if((mat[i][i] == 'T') || (mat[i][i] == c)) ++ct;
					if(mat[i][i] == '.') unfilled = true;

				}
				if((ct == 4) && (c=='X' || c=='O')) {won = true;}
			}
			if(!won)
			{
				ct = 0;
				c = mat[0][3];
				if(c == 'T') c = mat[1][2];
				for(int i = 0; i < 4; ++i)
				{
					if((mat[i][3-i] == 'T') || (mat[i][3-i] == c)) ++ct;
					if(mat[i][3-i] == '.') unfilled = true;

				}
				if((ct == 4) && (c=='X' || c=='O')) {won = true;}
			}
		}

		if(won)
		{
			if(c == 'X') k = 1;
			else k = 2;
		}
		else
		{
			if(unfilled) k = 3;
			else k = 0;
		}

		fsout <<"Case #" << ts << ": " << str[k] << endl;  
	}
	fsin.close();
	fsout.close();
	return 0;
}

