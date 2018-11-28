#include<iostream>
#include<fstream>

using namespace std;

char msg[4][30] = {
		"X won",
		"O won",
		"Draw",
		"Game has not completed"
	};

int combo[10][4] = {
		{0,1,2,3},	{4,5,6,7},
		{8,9,10,11},	{12,13,14,15},
		{0,4,8,12},	{1,5,9,13},
		{2,6,10,14},	{3,7,11,15},
		{0,5,10,15},	{3,6,9,12}
	};

class Tic {
	char board[20];
	public:
	int score, eFlag;
	Tic() {
		eFlag=0;
	}
	void readBoard(char, int index);	
	void checkCombo(int);
};

void Tic::readBoard(char symbol, int index) {
	board[index]=symbol;
}

void Tic::checkCombo(int cIndex) {
	score=0;
	for(int i=0; i<4; i++) {
		if(board[combo[cIndex][i]]=='X')
			score++;
		if(board[combo[cIndex][i]]=='O')
			score--;
		if(board[combo[cIndex][i]]=='T')
			score+=10;
		if(board[combo[cIndex][i]]=='.')
			eFlag=1;
	}
}

int main() {
	ifstream inFile;
	inFile.open("A-large.in");
	int c=1, T, res;
	char sym;
	inFile >> T;
	while(T--) {
		res=2;
		Tic *t = new Tic();
		for(int i=0; i<16; i++) {
			inFile >> sym;
			t->readBoard(sym, i);
		}
		for(int i=0; i<10; i++) {
			t->checkCombo(i);
			if(t->score==4 ||t->score==13) {
				res=0; break;
			}
			if(t->score==-4 ||t->score==7) {
				res=1; break;
			}
		}
		if(t->eFlag==1 && res==2)
			res=3;
		delete(t);
		cout<<"Case #"<<c<<": "<<msg[res]<<endl; c++;
	}
	inFile.close();
	return 0;
}

