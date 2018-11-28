#include <fstream>
#include <iostream>
using namespace std;
#define SIZE 4
#define FILE "A-small-attempt1.in"

class GameState{
public:
	GameState();
	bool checkEnd();
	bool checkWin();
	char getstateRel(int, int, char);
	char state[SIZE][SIZE];
	char winner;
	

private:
	bool checkLineWin();
	bool checkDiagonalWin();
	bool checkLine(int, char);
	
};

GameState::GameState(){
	winner='.';
}
char GameState::getstateRel(int i, int j, char mimic){
	if(state[i][j]=='.')
		return '.';
	else if (state[i][j]=='T')
		return mimic;
	else
		return state[i][j];
}
bool GameState::checkLine(int k, char sq){
	int count=0;
	char odd;
	for(int i=0;i<SIZE;i++)
		if(state[i][k]==sq)
			count++;
		else
			odd= state[i][k];
	if ((count==SIZE)||(count==SIZE-1&&odd=='T'))
		return true;
	count= 0;
	for(int j=0;j<SIZE;j++)
		if(state[k][j]==sq)
			count++;
		else
			odd= state[j][k];
	if ((count==SIZE)||(count==SIZE-1&&odd=='T'))
		return true;
	return false;
	
}

bool GameState::checkLineWin(){
	bool boolean;
	for(int i=0; i<SIZE; i++)
		if(checkLine(i,'X')){
			winner= 'X';
			return true;
		}else if(checkLine(i,'O')){
			winner='O';
			return true;
		}
	return false;
}

bool GameState::checkDiagonalWin(){
	bool boolean = true;
	for(int j=0; j<SIZE-1; j++)
		if(state[j][j]=='.')
			boolean= false;
		else if(getstateRel(j,j,state[j+1][j+1])==getstateRel(j+1,j+1,state[j][j]))
			winner=getstateRel(j,j,state[j+1][j+1]);
		else
			boolean= false;
	if (boolean)
		return true;
	else
		boolean= true;
	for(int j=0; j<SIZE-1; j++)
		if(state[SIZE-1-j][j]=='.')
			boolean= false;
		else if(getstateRel(SIZE-1-j,j,state[SIZE-2-j][j+1])==getstateRel(SIZE-2-j,j+1,state[SIZE-1-j][j]))
			winner=getstateRel(SIZE-1-j,j,state[SIZE-2-j][j+1]);
		else
			return false;
	return boolean;
}
bool GameState::checkWin(){
	bool win=checkLineWin();
	if (win)
		return win;
	win=checkDiagonalWin();
	if (win)
		return win;
	return false;
}
bool GameState::checkEnd(){
	for(int i=0; i<SIZE; i++)
		for(int j=0; j<SIZE; j++)
			if (state[i][j]=='.')
				return false;
	return true;
}

int main(){
	int no;
	ifstream input;
	ofstream output;
	GameState game;
	input.open(FILE, ios::in);					//initailizes an input file stream object
	output.open("output.out", ios::out);					//initailizes an input file stream object

	if(!(input))												
	{
		cout << "No input file found........exiting program.";
		exit(1);
	}

	input>> no;
	for(int k=0; k<no; k++){
		cout<< "k="<< k<<endl;
		for(int i=0; i<SIZE; i++)
			for(int j=0; j<SIZE; j++)
				input>> game.state[i][j];
		output<< "Case #"<< k+1<< ": ";
		if(game.checkWin())
			output<< game.winner<< " won";
		else if(game.checkEnd())
				output<< "Draw";
		else 
			output<< "Game has not completed";
		output<< endl;
	}
	system("pause");
	return 0;

}