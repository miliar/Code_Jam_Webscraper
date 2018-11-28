#include <cstdio>
#include <cstring>

using namespace std;

int t,cases=1;
char board[5][5];
int winner;
bool dot;

void check_diagonal(){
	
	int x_count = 0;
	int o_count = 0;
	bool have_t = false;

	for (int i=0;i<4;i++){
		if (board[i][i] == 'X'){
			x_count++;
			o_count = 0;
		}else if (board[i][i] == 'O'){
			o_count++;
			x_count = 0;
		}else if (board[i][i] == 'T'){
			have_t = true;
		}else if (board[i][i] == '.'){
			dot = true;
		}
	}

	if ((x_count == 4 && have_t == false)|| (x_count == 3 && have_t)){
		winner = 1;
		return;
	}
	else if ((o_count == 4 && have_t == false)|| (o_count == 3 && have_t)){
		winner = 2;
		return;
	}

	x_count = 0;
	o_count = 0;
	have_t = false;

	for (int i=0; i < 4; i++){
		if (board[i][3-i] == 'X'){
			x_count++;
			o_count=0;
		}else if (board[i][3-i] == 'O'){
			o_count++;
			x_count=0;
		}else if (board[i][3-i] == 'T'){
			have_t = true;
		}else if (board[i][3-i] == '.'){
			dot = true;
		}
	}

	if ( (x_count == 4 && have_t == false) || (x_count == 3 && have_t == true  ) ){
		winner = 1;
		return;
	}else if (  (o_count == 4 && have_t == false) || (o_count == 3 && have_t == true) ){
		winner = 2;
		return;
	}
	
	
}

void check_row(){

	int x_count;
	int o_count;

	bool have_t;

	for (int i=0; i < 4;i++){

		have_t = false;
		x_count = 0;
		o_count = 0;

		for (int j=0; j < 4;j++){
			if (board[i][j] == 'X'){
				x_count++;
				o_count = 0;
			}else if (board[i][j] == 'O'){
				o_count++;
				x_count = 0;
			}else if (board[i][j] == 'T'){
				have_t = true;
			}else if (board[i][j] == '.'){
				dot = true;
			}
		}
		if ( (x_count == 4 && have_t == false) || (x_count == 3 && have_t == true) ){
			winner = 1;
			return;
		}else if (  (o_count == 4 && have_t == false ) || (o_count == 3 && have_t == true) ){
			winner = 2;
			return;
		}
	}
}

void check_column(){

	int x_count = 0;
	int o_count = 0;

	bool have_t = false;

	for (int i=0;i<4;i++){

		have_t = false;
		x_count = 0;
		o_count = 0;

		for (int j=0;j<4;j++){

			if (board[j][i] == 'X'){
				x_count++;
				o_count = 0;
			}else if (board[j][i] == 'O'){
				o_count++;
				x_count = 0;
			}else if (board[j][i] == 'T'){
				have_t = true;
			}else if (board[j][i] == '.'){
				dot = true;
			}
		}

		if ( (x_count == 4 && have_t == false) || (x_count == 3 && have_t == true) ){
			winner = 1;
			return;
		}else if (  (o_count == 4 && have_t == false ) || (o_count == 3 && have_t == true) ){
			winner = 2;
			return;
		}
	}
}

int main(){

	
	scanf("%d\n",&t);

	while (t--){

		memset(board,0,sizeof(board));
		winner = -1;
		dot = false;

		for (int i=0;i<4;i++){
			scanf("%s\n",board[i]);
		}
		
		scanf("\n");

		if (winner == -1) check_diagonal();
		if (winner == -1) check_row();
		if (winner == -1) check_column();
		
		if (winner == 1){
			printf("Case #%d: X won\n",cases++);
		}else if (winner == 2){
			printf("Case #%d: O won\n",cases++);
		}else if (winner == -1){
			if (dot){
				printf("Case #%d: Game has not completed\n",cases++);
			}else{
				printf("Case #%d: Draw\n",cases++);
			}
		}
	}


	return 0;
}
