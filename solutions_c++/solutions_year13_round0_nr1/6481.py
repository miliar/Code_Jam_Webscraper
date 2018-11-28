#include <stdio.h>
#include <conio.h>
#include <iostream>

using namespace std;

void main(){
	int T;
	scanf("%d", &T);
	for(int cases = 1; cases <= T; cases++){
		char table[5][5];
		int score[5][5];
		for(int i = 0; i < 4; i++){
			scanf("%s", table[i]);
		}
		char dummy[1024];
		cin.getline (dummy, sizeof(dummy));

		int dot = 0;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
			if(table[i][j]=='X'){
					score[i][j] = -10;
				}else if(table[i][j]=='O'){
					score[i][j]	= 10;
				}
				else if(table[i][j]=='T'){
					score[i][j] = 1;
				}
				else if(table[i][j]=='.'){
					score[i][j] = 0;
					dot++;
				}
			}
		}
		bool nowon = true;
		printf("Case #%d: ", cases);
		//row
		int sum = 0;
		if(nowon){
			for(int i = 0; i < 4; i++){
				sum = score[i][0] + score[i][1] + score[i][2] + score[i][3];
				if(sum == 40 || sum == 31 ){
					printf("O won\n");
					nowon = false;
					break;
				}
				else if(sum == -40 || sum == -29){
					printf("X won\n");
					nowon = false;
					break;
				}
			}
		}
		//col
		if(nowon){
			for(int i = 0; i < 4; i++){
				sum = score[0][i] + score[1][i] + score[2][i] + score[3][i];
				if(sum == 40 || sum == 31){
					printf("O won\n");
					nowon = false;
					break;
				}
				else if(sum == -40 || sum == -29){
					printf("X won\n");
					nowon = false;
					break;
				}
			}
		}
		//cross1
		sum = score[0][0] + score[1][1] + score[2][2] + score[3][3];
		if((sum == 40 || sum == 31) && nowon){
			printf("O won\n");
			nowon = false;
		}
		else if((sum == -40 || sum == -29) && nowon){
			printf("X won\n");
			nowon = false;
		}
		//cross2
		sum = score[0][3] + score[1][2] + score[2][1] + score[3][0];
		if((sum == 40 || sum == 31) && nowon){
			printf("O won\n");
			nowon = false;
		}
		else if((sum == -40 || sum == -29) && nowon){
			printf("X won\n");
			nowon = false;
		}

		if(nowon){
			if(dot > 0){
				printf("Game has not completed\n");
			}else{
				printf("Draw\n");
			}
		}
	}
	//getch();
}
