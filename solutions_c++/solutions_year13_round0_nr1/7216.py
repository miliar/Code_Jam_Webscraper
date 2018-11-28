#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <stdio.h>

using namespace std;

string checkPattern(string row)
{
	if(row == "XXXX")
		return "X won";
	else if(row == "OOOO")
		return "O won";
	else
	{
		int loc = row.find('T');
		if (loc == std::string::npos)
			return "No";
		else
		{
			string subRow = row.erase(loc,1);
			if(subRow == "OOO")
				return "O won";
			else if(subRow == "XXX")
				return "X won";
			else
				return "No";
		}
	}
}
string checkHoriz(string board)
{
	string result = "";
	for(int i = 0; i < 4; i++)
	{
		if(result == "O won" || result == "X won")
			break;
		else
		{
			string row = board.substr((0+(4*i)),4);
			result = checkPattern(row);
		}
	}
	return result;
}
string checkVert(string board)
{
	string result = "";
	for(int i = 0; i < 4; i++)
	{
		if(result == "O won" || result == "X won")
			break;
		else
		{
			string row = "";
			for(int s = 0; s < 4; s++)
				row.push_back(board.at(i+(s*4)));
			result = checkPattern(row);
		}
	}
	return result;
}
string checkDiag(string board)
{
	string result = "";
	string row = "";
	for(int s = 0; s < 4; s++)
		row.push_back(board.at(s*5));
	//cout << row << endl;
	result = checkPattern(row);
	if(result == "O won" || result == "X won")
		return result;
	else
	{
		row = "";
		for(int s = 0; s < 4; s++)
			row.push_back(board.at(3 +(s*3)));
		//cout << row << endl;	
		result = checkPattern(row);
		return result;		
	}
}
string checkDraw(string board)
{
	if(board.find('.')==std::string::npos)
		return "Draw";
	else
		return "Game has not completed";
}
string checkBoard(string board)
{
	string result =	checkHoriz(board);
	if(result == "No")
	{
		result = checkVert(board);
		if(result == "No")
		{
			result = checkDiag(board);
			if(result == "No")
				return checkDraw(board);
			else
				return result;
		}
		else
			return result;
	}
	else
		return result;

}
int main()
{
	fstream f("A-large.in", fstream::in);
	int num;
	f >> num;
	for(int s = 1; s <= num; s++)
	{
		string board = "";
		//board[16] = '\0';
		for(int i = 0; i < 4; i++)
		{
			string row;
			f >> row;
			//cout << row << endl;
			board.append(row);
			//strncat(board,row.c_str(),4);
		}
		//cout << board << endl;
		cout << "Case #" << s << ": " << checkBoard(board) << endl;
		//board = 0;
	}
}
