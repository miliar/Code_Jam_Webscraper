// cpp_console_test.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const int BOARD_SIZE = 4;
char Board[BOARD_SIZE*BOARD_SIZE+1];

enum BINGO_STATE{
	WIN_O,
	WIN_X,
	DRAW,
	NOT_END
};

BINGO_STATE GetBingo(const char* arr)
{
	int countO=0;
	int countX=0;
	int countEmpty=0;

	for(int i=0;i<BOARD_SIZE;i++)
	{
		if (arr[i] == 'O') countO++;
		if (arr[i] == 'X') countX++;
		if (arr[i] == '.') countEmpty++;
		if (arr[i] == 'T') { countO++; countX++;}
	}

	if (countO >= BOARD_SIZE) {
		return WIN_O;
	} else if (countX >= BOARD_SIZE) {
		return WIN_X;
	} else if (countEmpty > 0) {
		return NOT_END;
	} else {
		return DRAW;
	}
}

const char* GetGameMessage(BINGO_STATE state)
{
	switch(state)
	{
	case WIN_O:
		return "O won";
		break;
	case WIN_X:
		return "X won";
		break;
	case DRAW:
		return "Draw";
		break;
	case NOT_END:
	default:
		return "Game has not completed";
	}
}

const char* GetGameState()
{
	char buffer[BOARD_SIZE+1]={0,};
	BINGO_STATE state;
	bool existEmpty = false;

	//Cross WINNER
	buffer[0] = Board[0]; buffer[1] = Board[BOARD_SIZE+1]; buffer[2] = Board[BOARD_SIZE*2+2]; buffer[3] = Board[BOARD_SIZE*3+3];
	buffer[BOARD_SIZE] = 0;

	state = GetBingo(buffer);
	if (state == WIN_O || state == WIN_X){
		return GetGameMessage(state);
	} else if (state == NOT_END) {
		existEmpty = true;
	}
	buffer[0] = Board[BOARD_SIZE-1]; buffer[1] = Board[BOARD_SIZE+2]; buffer[2] = Board[BOARD_SIZE*2+1]; buffer[3] = Board[BOARD_SIZE*3];
	buffer[BOARD_SIZE] = 0;

	state = GetBingo(buffer);
	if (state == WIN_O || state == WIN_X){
		return GetGameMessage(state);
	} else if (state == NOT_END) {
		existEmpty = true;
	}
	//horizon WINNER
	for(int x=0;x<BOARD_SIZE*BOARD_SIZE;x+=BOARD_SIZE)
	{
		strncpy(buffer,&Board[BOARD_SIZE*x],4);
		state = GetBingo(buffer);
		if (state == WIN_O || state == WIN_X) {
			return GetGameMessage(state);
		} else if (state == NOT_END) {
			existEmpty = true;
		}

	}
	//Vertical WINNER
	for(int y=0;y<BOARD_SIZE;y++)
	{
		for(int i=0;i<BOARD_SIZE;i++)
		{
			buffer[i] = Board[BOARD_SIZE*i+y];
		}
		state = GetBingo(buffer);
		if (state == WIN_O || state == WIN_X) {
			return GetGameMessage(state);
		} else if (state == NOT_END) {
			existEmpty = true;
		}
	}

	//DRAW
	if (existEmpty == false) {
		return GetGameMessage(DRAW);
	} else {
	//Not END
		return GetGameMessage(NOT_END);
	}

}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream input;
	ofstream output;

	input.open("input.txt",ifstream::in);
	output.open("output.txt",ofstream::out);

	int read_count;
	char buffer[256];

	input.getline(buffer,256);

	read_count=atoi(buffer);

	for(int i=0;i<read_count;i++)
	{
		for(int board_line=0;board_line<BOARD_SIZE;board_line++)
		{
			input.getline(buffer,256);
			strncpy(&Board[BOARD_SIZE*board_line],buffer,4);
		}
		input.getline(buffer,256); //skip line

		output<<"Case #"<<i+1<<": "<<GetGameState()<<endl;
	}
	
	input.close();

	output.close();

	
	return 0;
}