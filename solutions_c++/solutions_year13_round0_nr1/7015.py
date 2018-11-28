#include<cstdio>


void determine_result(FILE* output_file , int test_case , int state) {
	if(state == 0) {
		fprintf(output_file,"Case #%d: X won\n" , test_case + 1);
	}else if(state == 1) {
		fprintf(output_file , "Case #%d: O won\n" , test_case + 1);
	}else if(state == 2) {
		fprintf(output_file , "Case #%d: Draw\n" , test_case + 1);
	}else if(state == 3) {
		fprintf(output_file , "Case #%d: Game has not completed\n" , test_case + 1);
	}
}

int main(int argc,char** argv)
{
	FILE* file = fopen(argv[1],"r");
	FILE* output_file = fopen("1_out.txt","w");
	int test_case_num;
	fscanf( file , "%d" , &test_case_num );
	for(int test_case = 0; test_case < test_case_num; ++test_case){
		char board[4][4];
		int dot_num = 0;
		for(int i = 0; i < 4; ++i){
			for(int j = 0; j < 4; ++j){
				fscanf( file , " %c" , &board[i][j]);
				printf("%c" , board[i][j]);
				if(board[i][j] == '.' ){
					dot_num++;
				}
			}
		}
		printf("\n");
		int state = -1;
		for(int i = 0; i < 4; ++i){
			int x_num = 0;
			int o_num = 0;
			for(int j = 0; j < 4; ++j){
				if(board[i][j] == 'X'){
					x_num++;
				}else if(board[i][j]=='O'){
					o_num++;
				}else if(board[i][j]=='T'){
					x_num++;
					o_num++;
				}
			}
			if(x_num == 4){
				state = 0;
				break;
			}
			if(o_num == 4){
				state = 1;
				break;
			}
		}
		if(state != -1){
			determine_result(output_file, test_case , state);
			continue;
		}
		for(int j = 0; j < 4; ++j){
			int x_num = 0;
			int o_num = 0;
			for(int i = 0; i < 4; ++i){
				if(board[i][j] == 'X'){
					x_num++;
				}else if(board[i][j]=='O'){
					o_num++;
				}else if(board[i][j]=='T'){
					x_num++;
					o_num++;
				}
			}
			if(x_num == 4){
				state = 0;
				break;
			}
			if(o_num == 4){
				state = 1;
				break;
			}
		}
		if(state != -1){
			determine_result(output_file, test_case , state);
			continue;
		}
		int x_num = 0;
		int o_num = 0;
		for(int i = 0; i < 4; ++i){
			if(board[i][i] == 'X'){
				x_num++;
			}else if(board[i][i] == 'O'){
				o_num++;
			}else if(board[i][i] == 'T'){
				x_num++;
				o_num++;
			}
		}
		if(x_num == 4){
			state = 0;
		}
		if(o_num == 4){
			state = 1;
		}
		if(state != -1){
			determine_result(output_file, test_case , state);
			continue;
		}
		x_num = 0;
		o_num = 0;
		for(int i = 0; i < 4; ++i){
			if(board[i][3-i] == 'X'){
				x_num++;
			}else if(board[i][3-i] == 'O'){
				o_num++;
			}else if(board[i][3-i] == 'T'){
				x_num++;
				o_num++;
			}
		}
		if(x_num == 4){
			state = 0;
		}
		if(o_num == 4){
			state = 1;
		}
		if(state != -1){
			determine_result(output_file, test_case , state);
			continue;
		}
		if(dot_num == 0){
			state = 2;
			determine_result(output_file, test_case , state);
			continue;
		}else{
			state = 3;
			determine_result(output_file, test_case , state);
			continue;

		}


	}


	fclose(file);
	fclose(output_file);
}