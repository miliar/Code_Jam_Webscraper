#include "stdafx.h"
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::ifstream;
using std::ofstream;
using std::string;
using std::ostringstream;

using std::vector;

#define NUM_PARAMS 4

#define WIDTH  4
#define HEIGHT  4

#define NUM_PLAYERS 2

int winVal1 = 3;

int winVal2 = 4;

//Items
class tictac
{

public:
	tictac()
	{
		m_type = "";
	}

	~tictac()
	{

	}

	void setType(string t_type)
	{
		m_type = t_type;
	}

	string getType()
	{
		return m_type;
	}

private:
	string m_type;
};


class player
{
public: 
	player()
	{
		win = false;
		piece.setType(".");
		piecesInARow = 0;	
	}

	~player(){}

	void addInaRow()
	{
		piecesInARow++;

		if (piecesInARow == 4)
		{
			win = true;
		}
	}

	void resetCounter()
	{
		piecesInARow = 0;
	}
	
	
	int getInaRow()
	{
		return piecesInARow;
	}

	void setPiece(string _piece)
	{
		piece.setType(_piece);
	}

	bool getWin()
	{
		return win;
	}

	void setWin(bool w)
	{
		win = w;
	}
	

private:
	bool win;
	tictac piece;
	short piecesInARow;
	
};



tictac gameBoard[WIDTH][HEIGHT];

player players[2];


//Store Credit

template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }

vector<int> StrToIntArr(string& _str)
{
	vector<int> myVec;

	char *dup = _strdup(_str.c_str());
	
	char * pch;
	printf ("Splitting string \"%s\" into tokens:\n",dup);
	pch = strtok (dup," ");
	

	while (pch != NULL)
	{
		printf ("%s\n",pch);
		myVec.push_back(atoi(pch));
		pch = strtok (NULL, " ");
	}
	free(dup);
	return myVec;
}

vector<string> StrToStroArr(string& _str)
{
	vector<string> myVec;

	char* dup = _strdup(_str.c_str());

	char* pch;

	pch = strtok(dup, " ");
	return myVec;
}

vector<string> GetLines(int Player)
{
	vector<string> validLines;
	string tPiece;

	switch(Player)
	{
	case 0:
		tPiece = "X";
		break;
	case 1:
		tPiece = "O";
		break;

	default:
		tPiece = ".";
	}

	for (int i = 0; i<WIDTH; i++)//Rows
	{
		validLines.push_back("");
		for (int j = 0; j<HEIGHT; j++)
		{
			string piece = gameBoard[i][j].getType();
			if (strcmp(piece.c_str() , "T")==0)
			{
				piece = tPiece;
			}
			validLines.back().append(tostr(piece));
		}
	}

	for(int j = 0; j<WIDTH; j++) //Columns
	{
		validLines.push_back("");
		for (int i = 0; i<HEIGHT; i++)
		{
			string piece = gameBoard[i][j].getType();
			if (strcmp(piece.c_str(), "T") == 0)
			{
				piece = tPiece;
			}
			validLines.back().append(tostr(piece));
		}
	}
	validLines.push_back("");

	for(int i = 0; i<4; i++)//Diagonal 1.
	{
		

		string piece = gameBoard[i][i].getType();
		if(strcmp(piece.c_str(), "T") == 0)
		{
			piece = tPiece;
		}
		validLines.back().append(tostr(piece));
	}
	validLines.push_back("");
	for(int i = 3; i>-1; i--)//Diagonal 2.
	{
		string piece = gameBoard[(i - 3)*-1][i].getType();
		if(strcmp(piece.c_str(), "T") == 0)
		{
			piece = tPiece;
		}
		validLines.back().append(tostr(piece));
	}

	return validLines;
}


string parseCase(int curCase, string* params)
{
	std::string res;
	res.append("Case #");
	res.append(tostr(curCase));
	res.append(": ");
	vector<int> rsvec;
	
	players[0].setPiece("X");
	players[1].setPiece("O");

	players[0].setWin(false);
	players[1].setWin(false);

	string completition = "D";

	for (int i = 0; i<NUM_PARAMS; i++)
	{
		for(int j = 0; j<NUM_PARAMS; j++)
		{
			gameBoard[i][j].setType(tostr(params[i][j]));
			if (strcmp(gameBoard[i][j].getType().c_str(), ".") == 0)
			{
				completition = ".";
			}
		}				
	}

	for (int curPlayer = 0; curPlayer<2; curPlayer++)
	{
		vector<string> validLines = GetLines(curPlayer);
		string curPlayerPiece = ".";
		if (curPlayer  == 0)
		{
			curPlayerPiece = "X";
		}
		else
			curPlayerPiece = "O";

		for (int i = 0; i<validLines.size(); i++)
		{
			for (int j = 0; j<4; j++)
			{
				string piece = tostr(validLines[i][j]);
				if (strcmp(piece.c_str(), curPlayerPiece.c_str()) == 0)
				{
					players[curPlayer].addInaRow();					
				}
			}
			players[curPlayer].resetCounter();
		}

	}

	if (players[0].getWin())
	{
		res.append("X won");
	}
	else if (players[1].getWin())
	{
		res.append("O won");
	}
	else if(strcmp(completition.c_str(), "D")== 0)
	{
		res.append("Draw");
	}
	else
		res.append("Game has not completed");

	
	res.append("\n");
	cout<<res;
	return res;

}

int main(int argc, char* argv[]) 
{ 
	ifstream fin;
	ofstream fout;
		
		fin.clear();
		fout.clear();
			
		fin.open("a.in");
		fout.open("a.out", std::ios::trunc);
	
		//Number of cases
		string numCases;
		getline(fin, numCases);
		cout<<numCases<<endl;

		int curCase = 1;

		string curLine[NUM_PARAMS];

		bool emptyLine = false;

		while(!fin.eof())
		{	
		
			for(int i = 0; i < NUM_PARAMS; i ++)
			{
				getline(fin,curLine[i]);
				if (curLine[i].empty())
				{
					emptyLine = true;
					break;
				}
				
			}
			
			if (emptyLine)
			{
				emptyLine = false;
				continue;
			}
			
			fout<<parseCase(curCase, curLine);
			++curCase;
				
		}

		fin.close();		
		fout.close();

		cin.get();

    return 0; // return 0 for no errors
}