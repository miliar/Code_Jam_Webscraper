#include <iostream>
#include <sstream>
#include <fstream>
#include "strutils.h"
#include <vector>

using namespace std;

bool HSearch(vector<vector<char>> mat, char pl)
{
	int r=0, c=0;
	while(r<4)
	{
		c=0;
		if(mat[r][c]==pl || mat[r][c]=='T')
		{
			c++;
			if(mat[r][c]==pl || mat[r][c]=='T')
			{
				c++;
				if(mat[r][c]==pl || mat[r][c]=='T')
				{
					c++;
					if(mat[r][c]==pl || mat[r][c]=='T')
					{
						return true;
					}
				}
			}
		}
		r++;
	}
	return false;
}

bool VSearch(vector<vector<char>> mat, char pl)
{
	int r=0, c=0;
	while (c<4)
	{
		r=0;
		if(mat[r][c]==pl || mat[r][c]=='T')
		{
			r++;
			if(mat[r][c]==pl || mat[r][c]=='T')
			{
				r++;
				if(mat[r][c]==pl || mat[r][c]=='T')
				{
					r++;
					if(mat[r][c]==pl || mat[r][c]=='T')
					{
						return true;
					}
				}
			}
		}
		c++;
	}
	return false;
}

bool DSearch(vector<vector<char>> mat, char pl)
{
	int r=0, c=0;
	if(mat[r][c]==pl || mat[r][c]=='T')
	{
		r++;
		c++;
		if(mat[r][c]==pl || mat[r][c]=='T')
		{
			r++;
			c++;
			if(mat[r][c]==pl || mat[r][c]=='T')
			{
				r++;
				c++;
				if(mat[r][c]==pl || mat[r][c]=='T')
				{
					return true;
				}
			}
		}
	}
	return false;
}

bool RDSearch(vector<vector<char>> mat, char pl)
{
	int r=0, c=3;
	if(mat[r][c]==pl || mat[r][c]=='T')
	{
		r++;
		c--;
		if(mat[r][c]==pl || mat[r][c]=='T')
		{
			r++;
			c--;
			if(mat[r][c]==pl || mat[r][c]=='T')
			{
				r++;
				c--;
				if(mat[r][c]==pl || mat[r][c]=='T')
				{
					return true;
				}
			}
		}
	}
	return false;
}

bool isFinished(vector<vector<char>> mat)
{
	bool Yup=true;
	for(int r=0; r<4 && Yup; r++)
	{
		for (int c=0; c<4 && Yup; c++)
		{
			char ch=mat[r][c];
			if (ch == '.')
			{
				Yup=false;
			}
		}
	}
	return Yup;
}

int main()
{
	ifstream input;
	ofstream output;
	input.open("A-large.in");
	output.open("aglaya_output.in");
	
	cin.clear();
	input.seekg(0);

	string casenum;
	getline(input,casenum);
	int caseno=atoi(casenum);
	
	for (int i=1; i<=caseno; i++)
	{
		vector<vector<char>> tictac(4, vector<char>(4));
		string line;
		for (int k=0; k<4; k++)
		{
			getline(input,line);
			if(line!="")
			{
				for(int j=0; j<4; j++)
				{
					tictac[k][j]=line[j];
				}
			}
			else
			{
				k--;
			}
		}
		if(HSearch(tictac,'X') == true || VSearch(tictac,'X') == true || DSearch(tictac,'X') == true || RDSearch(tictac,'X') == true)
		{
			output << "Case #" << i << ": X won\n";
		}
		else if(HSearch(tictac,'O') == true || VSearch(tictac,'O') == true || DSearch(tictac,'O') == true || RDSearch(tictac,'O') == true)
		{
			output << "Case #" << i << ": O won\n";
		}
		else if(isFinished(tictac)==true)
		{
			output << "Case #" << i << ": Draw\n";
		}
		else if(isFinished(tictac)==false)
		{
			output << "Case #" << i << ": Game has not completed\n";
		}
	}
	output.close();
	return 0;
}