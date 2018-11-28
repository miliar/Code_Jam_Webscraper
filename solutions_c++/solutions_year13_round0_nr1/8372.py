#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

void checkwin(string board[], int count);
int main()
{
 
	ifstream myfile;
	myfile.open("input.in");
	string board[4];
    string s;
	if (myfile.is_open()) 
	{	
		getline(myfile, s);
	}
	int numbercase;
	stringstream(s) >> numbercase;
	for(int j=1; j<=numbercase; ++j)
	{
        getline(myfile, board[0]);
		getline(myfile, board[1]);
		getline(myfile, board[2]);
		getline(myfile, board[3]);
		checkwin(board,j);
		getline(myfile, s);
	}
	return 0;
}

void checkwin(string board[], int count)
{
	int x = -1;
	int y = -1;
	for(int i=0; i<4; ++i)
	{
		for (int j=0; j<4; ++j)
		{
			if(board[i][j] == 'T'){
				x = i;
				y = j;
				break;
			}
		}
	}
	if(x != -1){
		board[x][y] = 'X';
	}
	if(board[0][0]== 'X' && board[1][1]== 'X' && board[2][2]== 'X' && board[3][3] == 'X'){
		cout << "Case #" << count << ": X won" << endl;
		return;
	}
	if(board[0][0]=='O' && board[1][1]=='O' && board[2][2]=='O' && board[3][3] == 'O'){
		cout << "Case #" << count << ": O won" << endl;
		return;
	}
	if(board[0][3]=='X' && board[1][2]=='X' && board[2][1]=='X' && board[3][0] == 'X'){
		cout << "Case #" << count << ": X won" << endl;
		return;
	}
	if(board[0][3]=='O' && board[1][2]=='O' && board[2][1]=='O' && board[3][0] == 'O'){
		cout << "Case #" << count << ": O won" << endl;
		return;
	}
	for(int j=0; j<4; ++j){
		if(board[j][0]=='X' && board[j][1]=='X' && board[j][2]=='X' && board[j][3] == 'X'){
			cout << "Case #" << count << ": X won" << endl;
			return;
		}
		if(board[j][0]=='O' && board[j][1]=='O' && board[j][2]=='O' && board[j][3] == 'O'){
			cout << "Case #" << count << ": O won" << endl;
			return;
		}
	}
	for(int j=0; j<4; ++j){
		if(board[0][j]=='X' && board[1][j]=='X' && board[2][j]=='X' && board[3][j] == 'X'){
			cout << "Case #" << count << ": X won" << endl;
			return;
		}
		if(board[0][j]=='O' && board[1][j]== 'O' && board[2][j]=='O' && board[3][j] == 'O'){
			cout << "Case #" << count << ": O won" << endl;
			return;
		}
	}
    if(x != -1){
		board[x][y] = 'O';}
	if(board[0][0]== 'X' && board[1][1]== 'X' && board[2][2]== 'X' && board[3][3] == 'X'){
		cout << "Case #" << count << ": X won" << endl;
		return;
	}
	if(board[0][0]=='O' && board[1][1]=='O' && board[2][2]=='O' && board[3][3] == 'O'){
		cout << "Case #" << count << ": O won" << endl;
		return;
	}
	if(board[0][3]=='X' && board[1][2]=='X' && board[2][1]=='X' && board[3][0] == 'X'){
		cout << "Case #" << count << ": X won" << endl;
		return;
	}
	if(board[0][3]=='O' && board[1][2]=='O' && board[2][1]=='O' && board[3][0] == 'O'){
		cout << "Case #" << count << ": O won" << endl;
		return;
	}
	for(int j=0; j<4; ++j){
		if(board[j][0]=='X' && board[j][1]=='X' && board[j][2]=='X' && board[j][3] == 'X'){
			cout << "Case #" << count << ": X won" << endl;
			return;
		}
		if(board[j][0]=='O' && board[j][1]=='O' && board[j][2]=='O' && board[j][3] == 'O'){
			cout << "Case #" << count << ": O won" << endl;
			return;
		}
	}
	for(int j=0; j<4; ++j){
		if(board[0][j]=='X' && board[1][j]=='X' && board[2][j]=='X' && board[3][j] == 'X'){
			cout << "Case #" << count << ": X won" << endl;
			return;
		}
		if(board[0][j]=='O' && board[1][j]== 'O' && board[2][j]=='O' && board[3][j] == 'O'){
			cout << "Case #" << count << ": O won" << endl;
			return;
		}
	}
	for(int i=0; i<4; ++i)
	{
		for (int j=0; j<4; ++j)
		{
			if(board[i][j] == '.'){
				cout << "Case #" << count << ": Game has not completed" << endl;
				return;
			}
		}
	}
	cout << "Case #" << count << ": Draw" << endl;
	return;
}