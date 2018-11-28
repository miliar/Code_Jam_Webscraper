#include <iostream>

using namespace std;

char board[4][4];

char analyse(int i, int j, int di, int dj){
	bool has_o = false, has_x = false;
	
	for(int k = 0; k < 4; k++){
		char c = board[i][j];
		
		if(c == '.' || (has_o && c == 'X') || (has_x && c == 'O')){
			return '.';
		}
		
		if(c == 'X')
			has_x = true;
		else if(c == 'O')
			has_o = true;
			
		i += di;
		j += dj;
	}

	return (has_o ? 'O' : 'X');
}

char analyse_row(int i){
	return analyse(i, 0, 0, 1);
}

char analyse_column(int j){
	return analyse(0, j, 1, 0);
}

char analyse_main_diagonal(){
	return analyse(0, 0, 1, 1);
}

char analyse_secondary_diagonal(){
	return analyse(0, 3, 1, -1);
}

int main(){
	int T;
	cin >> T;
	
	for(int t = 1; t <= T; t++){
		bool draw = true;
		
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				cin >> board[i][j];
				draw = draw && board[i][j] != '.';
			}
		}	
		
		char winner = '.';
		
		for(int i = 0; winner == '.' && i < 4; i++){
			winner = analyse_row(i);
		}
		
		for(int j = 0; winner == '.' && j < 4; j++){
			winner = analyse_column(j);
		}
		
		if(winner == '.')
			winner = analyse_main_diagonal();
			
		if(winner == '.')
			winner = analyse_secondary_diagonal();
		
		cout << "Case #" << t << ": ";
		
		if(winner != '.')
			cout << winner << " won\n";
		else if(draw)
			cout << "Draw\n";
		else
			cout << "Game has not completed\n"; 
	}
}
