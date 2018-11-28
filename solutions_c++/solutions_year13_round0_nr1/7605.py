#include <iostream>
#include <fstream>

using namespace std;



class Board {
public:
	bool x_win, o_win, has_blank;
	int x_count, o_count, t_count;
	char board[4][4];
	Board(char boardin[6][5]){
		x_win   = o_win   = has_blank = 0;
		x_count = o_count = t_count   = 0;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				board[i][j] = boardin[i][j];
				//cout << board[i][j];
			}
			//cout << endl;
		}
		//cout << "!" << endl;
	}
	void reset_counts(){
		x_count = o_count = t_count = 0;
	}
	void check_counts(){
		if ((x_count == 3 && t_count == 1) || (x_count == 4)){
			x_win = true;
		}
		if ((o_count == 3 && t_count == 1) || (o_count == 4)){
			o_win = true;
		}
	}
	void check_all(){
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				check_coords(i, j);
			}
			check_counts();
			reset_counts();
		}
		
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				check_coords(j, i);
			}
			check_counts();
			reset_counts();
		}
		check_coords(0, 0);
		check_coords(1, 1);
		check_coords(2, 2);
		check_coords(3, 3);
		check_counts();
		reset_counts();
		
		check_coords(0, 3);
		check_coords(1, 2);
		check_coords(2, 1);
		check_coords(3, 0);
		check_counts();
		reset_counts();
	}
	void check_coords(int x, int y){
		switch (board[x][y]){
			case '.':
				has_blank = true;
				break;
			case 'T':
				t_count += 1;
				break;
			case 'O':
				o_count += 1;
				break;
			case 'X':
				x_count += 1;
				break;
		}
	}
	string get_results(){
		check_all();
		if (x_win){
			return "X won";
		} else if (o_win){
			return "O won";
		} else if (has_blank){
			return "Game has not completed";
		} else {
			return "Draw";
		}
	}
};



int main(int argc, char** argv){

	if (argc < 3){ return -1; }
	
	ifstream inputreader(argv[1]);
	ofstream outputprinter(argv[2]);
	
	int lines;
	inputreader >> lines;
	inputreader.ignore(2000, '\n');
	int line_count = 1;

	while (inputreader.good()){
		char line[6][5];
		for (int i = 0; i < 5; i++){
			inputreader.getline(line[i], 5);
		}
		outputprinter << "Case #" << line_count << ": " << Board(line).get_results() << endl;
		if (line_count++ == lines){
			break;
		}
		//cout << "Case #" << line_count-1 << endl;
	}


	return 0;
}
