#include <iostream>
#include <fstream>
using namespace std;
int main(){
	int N;
	ifstream input ("A-small-attempt0.in");
	ofstream output ("A-small-attempt0.out");
	input>>N;
	for (int n=0; n<N; n++){
		char board[4][4];
		bool full(true);
		bool draw;
		char won;
		for (int i=0; i<4; i++)	input >> board[i];
		for (int i=0;i<10;i++){
			won = board[i<4?i:0][i<4?0:i<8?i:3*(i-8)];
			draw = false;
			for (int j=0;j<4 ;j++) {
				int x = i<4?i:j;
				int y = i<4?j:i<8?i-4:i<9?j:3-j;
				if (board[x][y] == '.'){
					full = false;
				}
				if (board[x][y] != won && board[x][y] != 'T'){
						draw = true;
						won = '.';
				}
			}
			if (won!='.') break;
		}
		//input.get();
		output << "Case #" << n+1 << ": ";
		if (full){
			if (draw)
				output << "Draw";
			else
				output << won << " won";
		}
		else{
			if (won=='.')
				output << "Game has not completed";
			else
				output << won << " won";
		}
		output <<endl;
	}
	input.close();
	exit(0);
}