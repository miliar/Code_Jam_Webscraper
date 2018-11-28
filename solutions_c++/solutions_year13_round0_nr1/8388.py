#include<stdio.h>
#include<iostream>
#include<string>
#include<fstream>

#include<vector>

using namespace std;

string result[4] = {"Game has not completed","X won","O won","Draw"};

void printBoard(char board[4][4]);
void initBoard(char board[4][4]);
void getResult(int loop, char board[4][4]);
void makeBoard(char board[4][4], string boardInput[4]);
int getState(int state, char input);

int main()
{
	char board[4][4] = { {'X','X','X','O'} , {'.','.','O','.'} , {'.','O','.','.'} , {'T','.','.','.'} };
	ifstream inputFile ("test.txt");
	string line;
	string boardInput[4];
	if(inputFile.is_open())
	{
		getline(inputFile, line);
		int loop = atoi(line.c_str());
		for(int i = 0 ; i < loop; i++)
		{
			for(int j = 0 ;j < 4; j ++)
			{
				getline(inputFile, line);
				boardInput[j] = line;
			}
			getline(inputFile, line);
			
			makeBoard(board, boardInput);
			getResult(i+1, board);
		}
	}


  return 0;
}


void printBoard(char board[4][4])
{
  for(int i =0; i < 4; i ++)
  {
    for(int j = 0 ; j < 4; j ++)
      cout<<board[i][j];
    cout<<endl;
  }
}

void initBoard(char board[4][4])
{
  
  for(int i =0; i < 4; i ++)
  {
    for(int j = 0 ; j < 4; j ++)
      board[i][j] = '.';
  }

}

void getResult(int loop, char board[4][4])
{
	int state = 0;
	bool NotDone = false;
	
	for(int i = 0 ; i < 4; i ++)
	{
		state = -1;
		for(int j = 0 ; j < 4; j ++)
		{
			if(board[i][j] == '.')
			{
				NotDone = true;
				state = -1;
				break;
			}
			state = getState(state , board[i][j]);
			if(state == -1)
				break;
		}
		if(state == 1 || state == 2)
		{
			cout<<"Case #"<<loop<<": "<<result[state]<<endl;
			return;
		}
	}
	
	
	for(int j = 0 ; j < 4; j ++)
	{
		state = -1;
		for(int i = 0 ; i < 4; i ++)
		{
			if(board[i][j] == '.')
			{
				NotDone = true;
				state = -1;
				break;
			}
			state = getState(state , board[i][j]);
			if(state == -1)
				break;
		}
		if(state == 1 || state == 2)
		{
			cout<<"Case #"<<loop<<": "<<result[state]<<endl;
			return;
		}
	}
	
	state = -1;
	for(int i = 0 ; i < 4; i ++)
	{
		if(board[i][i] == '.')
		{
			NotDone = true;
			state = -1;
			break;
		}
		state = getState(state , board[i][i]);
		if(state == -1)
			break;
	}
	if(state == 1 || state == 2)
	{
		cout<<"Case #"<<loop<<": "<<result[state]<<endl;
		return;
	}
	
	state = -1;
	for(int i = 0 ; i < 4; i ++)
	{
		if(board[i][3-i] == '.')
		{
			NotDone = true;
			state = -1;
			break;
		}
		state = getState(state , board[i][3-i]);
		if(state == -1)
			break;
	}
	if(state == 1 || state == 2)
	{
		cout<<"Case #"<<loop<<": "<<result[state]<<endl;
		return;
	}
	
	if(NotDone)
		cout<<"Case #"<<loop<<": "<<result[0]<<endl;
	else
		cout<<"Case #"<<loop<<": "<<result[3]<<endl;
}

// -1 is break
// 0 is T
// 1 is X
// 2 is O
int getState(int state, char input)
{
	if(state == 0)
	{
		state =(input == 'X')?1:2;
		return state;
	}
	
	if(state == 1)
		if(input == 'O')
			return -1;
		else
			return 1;
	
	if(state == 2)
		if(input == 'X')
			return -1;
		else
			return 2;
	
	if(input == 'O')
		return 2;
	else if(input == 'X')
		return 1;
		
	return 0;
	
}

void makeBoard(char board[4][4], string input[4])
{
	for(int i = 0 ; i < 4; i ++)
		for(int j = 0 ; j < 4; j ++)
			board[i][j] = input[i][j];
}
