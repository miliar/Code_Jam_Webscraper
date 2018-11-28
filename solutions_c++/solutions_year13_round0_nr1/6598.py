#include<iostream>
#include<fstream>
using namespace std;
ifstream in("input.txt");
ofstream out("output.txt");
int T;
char board[4][4];
int main(){
	in >> T;
	for(int i=0;i<T;i++){
		out << "Case #" << i+1 << ": ";
		for(int k=0;k<4;k++){
			in >> board[k];
		}
		int won = 0;
		int completed = 1;
		for(int k=0;k<4 && !won;k++){
			int horzx = 0;
			int vertx = 0;
			int horzo = 0;
			int verto = 0;
			for(int l=0;l<4 && !won;l++){
				horzx = 0;
				vertx = 0;
				horzo = 0;
				verto = 0;
				for(int p=0;p<4;p++){
					if(board[l][p] == '.')
						completed = 0;
					if(board[l][p] == 'X' || board[l][p] == 'T')
						horzx++;
					if(board[l][p] == 'O' || board[l][p] == 'T')
						horzo++;
					if(board[p][l] == 'X' || board[p][l] == 'T')
						vertx++;
					if(board[p][l] == 'O' || board[p][l] == 'T')
						verto++;
				}
				if(horzx == 4){
					out << "X won\n";
					won = 1;
				}
				else if(horzo == 4){
					out << "O won\n";
					won = 1;
				}
				else if(vertx == 4){
					out << "X won\n";
					won = 1;
				}
				else if(verto == 4){
					out << "O won\n";
					won = 1;
				}
			}
		}
		int crosx = 0;
		int rcrsx = 0;
		int croso = 0;
		int rcrso = 0;
		for(int k=0;k<4 && !won;k++){
			if(board[k][k] == 'X' || board[k][k] == 'T')
				crosx++;
			if(board[k][k] == 'O' || board[k][k] == 'T')
				croso++;
			if(board[k][3-k] == 'X' || board[k][3-k] == 'T')
				rcrsx++;
			if(board[k][3-k] == 'O' || board[k][3-k] == 'T')
				rcrso++;
		}
		if(crosx == 4 && !won){
			out << "X won\n";
			won = 1;
		}
		else if(croso == 4 && !won){
			out << "O won\n";
			won = 1;
		}
		else if(rcrsx == 4 && !won){
			out << "X won\n";
			won = 1;
		}
		else if(rcrso == 4 && !won){
			out << "O won\n";
			won = 1;
		}
		else if(!won && !completed){
			out << "Game has not completed\n";
		}
		else if(!won && completed){
			out << "Draw\n";
		}
	}
}
