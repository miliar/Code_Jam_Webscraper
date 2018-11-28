#include <iostream>
#include <fstream>


using namespace std;

void transpose(char in[][4]){

	int temp;

	for (int i = 0 ; i < 4 ; i++){
	
		for (int j = i ; j < 4 ; j++){
		
			temp = in[i][j];
			in[i][j] = in[j][i];
			in[j][i] = temp;
		}

	}

	

}


void boardin(char b[][4],fstream& fin){



	for (int  i = 0 ; i < 4 ; i++){
	
		for (int j = 0 ; j < 4 ; j++){
		
			fin>>b[i][j];

		}

	}

	
}

void copy(char out[][4],char in[][4]){

	for (int  i = 0 ; i < 4 ; i++){
	
		for (int j = 0 ; j < 4 ; j++){
		
			out[i][j] = in[i][j];

		}

	}


}


bool check(char in[][4], char c){

	for (int i = 0 ; i < 4 ; i++){
	
		if (in[i][0] != '.'&& in[i][1] == c && in[i][0] == in[i][1] && in[i][1] == in[i][2] && in[i][2] == in[i][3]){
		
			return true;

		}

	}

	if ( in[0][0] == c&&in[0][0]== in[1][1] && in[1][1] == in[2][2] && in[2][2] == in[3][3] ){
	
		return true;

	}

	if (in[0][3] == c&&in[0][3] == in[1][2] && in[1][2] == in[2][1] && in[2][1]==in[3][0]  ){
	
		return true;

	}

	return false;

}


bool find(char in[][4],char c){




		for (int  i = 0 ; i < 4 ; i++){
	
			for (int j = 0 ; j < 4 ; j++){
		
				if (in[i][j] == c){
				
					return true;

				}

			}

		}
		return false;
}

void main(){

	fstream fin;
	fstream fout;

	fin.open("input.in",ios::in || ios::binary);
	fout.open("output.txt",ios::out );

	int n;
	fin>>n;

	char board[4][4];

	char boardX[4][4];
	char boardY[4][4];


	for (int m = 0  ; m < n ; m++){
	
		boardin(board,fin);
		copy(boardX,board);
		copy(boardY,board);
		
		bool found = false;

		for (int  i = 0 ; i < 4 ; i++){
	
			for (int j = 0 ; j < 4 ; j++){
		
				if (board[i][j] == 'T'){
				
					boardX[i][j] = 'X';
					boardY[i][j] = 'O' ;
					found = true;
					break;

				}

			}
			if (found){break;}


		}

		if (check(boardX,'X')){
		
			fout<<"Case #"<<m+1<<": X won"<<endl;

		}else {
		
			transpose(boardX);
			if (check(boardX,'X')){
			
				fout<<"Case #"<<m+1<<": X won"<<endl;

			}else if (check(boardY,'O')){
			
				fout<<"Case #"<<m+1<<": O won"<<endl;

			}else {
			
				transpose(boardY);
				if (check(boardY,'O')){
			
					fout<<"Case #"<<m+1<<": O won"<<endl;


				}else if (find(board,'.')){
		
					fout<<"Case #"<<m+1<<": Game has not completed"<<endl;

				}else {
		
					fout<<"Case #"<<m+1<<": Draw"<<endl;
				}

			}


		}
	}
	fin.close();
	fout.close();

}