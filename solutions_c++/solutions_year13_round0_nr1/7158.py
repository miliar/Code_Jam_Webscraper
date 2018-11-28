#include <iostream>
#include <cstring>
#include <vector>

#define N 4

using namespace std;

vector < vector <char> > board;
vector <char> tmp;

int
check(char c){
	int amount=0;
	for(int i=0; i<N; i++){
		// Horizontal
		if((board[i][0]==c || board[i][0]=='T') && (board[i][1]==c || board[i][1]=='T') && (board[i][2]==c || board[i][2]=='T') && (board[i][3]==c || board[i][3]=='T')){
			amount=3;
			break;
		}
		// Vertical
		if((board[0][i]==c || board[0][i]=='T') && (board[1][i]==c || board[1][i]=='T') && (board[2][i]==c || board[2][i]=='T') && (board[3][i]==c || board[3][i]=='T')){
			amount=3;
			break;
		}
		// Diagonal
		if((board[0][0]==c || board[0][0]=='T') && (board[1][1]==c || board[1][1]=='T') && (board[2][2]==c || board[2][2]=='T') && (board[3][3]==c || board[3][3]=='T')){
			amount=3;
			break;
		}
		// La otra Diagonal
		if((board[0][3]==c || board[0][3]=='T') && (board[1][2]==c || board[1][2]=='T') && (board[2][1]==c || board[2][1]=='T') && (board[3][0]==c || board[3][0]=='T')){
			amount=3;
			break;
		}
	}
	return amount;
}

string
set(void){
	string s;
	int amountx=0, amounto=0, b=0;
	// Checkeo si gano X.
	amountx = check('X');
	// Checkeo si gano O.
	amounto = check('O');
	// Checkeo si hay un empate pero el juego no termino.
	if(amountx==amounto){
		for(int i=0; i<N; i++){
			for(int j=0; j<N; j++){
				if(board[i][j]=='.'){
					b=1;
					break;
				}
			}
		}
	}
	// Seteo el string
	if(amountx>amounto){
		// Gano X
		s = "X won";
	}
	else if(amountx<amounto){
		// Gano O
		s = "O won";
	}
	else if (amountx==amounto && b){
		// No termino el juego
		s = "Game has not completed";
	}
	else if(amountx==amounto && !b){
		// Ya termino el juego y hubo un empate
		s = "Draw";
	}
	return s;
}

int
main(void){
	int t=0;
	char e;
	string s;
	cin>>t;
	// Tests Cases
	for(int i=0; i<t; i++){
		// Read input
		for(int k=0; k<N; k++){
			for(int j=0; j<N; j++){
				cin>>e;
				tmp.push_back(e);
			}
			board.push_back(tmp);
			tmp.clear();
		}
//		// La matriz es:
//		for(int f=0; f<N; f++){
//			for(int o=0; o<N; o++){
//				cout << board[f][o];
//			}
//			cout << endl;
//		}
//		cout << endl;
		// Set String s
		s = set();
		cout << "Case #" << i+1 << ": "<< s << endl;
		board.clear();
	}
	return 0;
}
