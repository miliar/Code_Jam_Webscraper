#include <cstdio>

int main(){
	int num;
	int countDot = 0;
	char box[4][4];
	char c;
	int result[1000];
	scanf("%d", &num);
	for(int i = 0; i< num; i++){

		countDot = 0;
		
		for(int j = 0; j< 4; j++){
			for(int k = 0; k<4; k++){
				scanf(" %c", &box[j][k]);
				if(box[j][k] == '.'){
					countDot ++;
				}
			}
		}
		int numWinX = 0;
		int numWinO = 0;
		int numDraw = 0;
		for(int j = 0; j< 4; j++){
			int countX = 0;
			int countO = 0;
			int countT = 0;
			for(int k = 0; k<4; k++){
				
				if(box[j][k] == 'X'){
					countX++;
				}else if (box[j][k] == 'O'){
					countO++;
				}else if (box[j][k] == 'T'){
					countT = 1;
				}
				
			}
			if(countX == 4){
				numWinX++;
			}else if(countX == 3 && countT == 1){
				numWinX++;
			}else if(countO == 4){
				numWinO++;
			}else if(countO == 3 && countT == 1){
				numWinO++;
			}else{
				numDraw++;
			}
			
		}

		for(int k = 0; k< 4; k++){
			int countX = 0;
			int countO = 0;
			int countT = 0;
			for(int j = 0; j<4; j++){
				
				if(box[j][k] == 'X'){
					countX++;
				}else if (box[j][k] == 'O'){
					countO++;
				}else if (box[j][k] == 'T'){
					countT = 1;
				}
				
			}
			if(countX == 4){
				numWinX++;
			}else if(countX == 3 && countT == 1){
				numWinX++;
			}else if(countO == 4){
				numWinO++;
			}else if(countO == 3 && countT == 1){
				numWinO++;
			}else{
				numDraw++;
			}
		}

		int countX = 0;
		int countO = 0;
		int countT = 0;
		for(int j = 0; j< 4;j++){
			
			if(box[j][j] == 'X'){
				countX++;
			}else if (box[j][j] == 'O'){
				countO++;
			}else if (box[j][j] == 'T'){
				countT = 1;
			}
			
		}
		if(countX == 4){
			numWinX++;
		}else if(countX == 3 && countT == 1){
			numWinX++;
		}else if(countO == 4){
			numWinO++;
		}else if(countO == 3 && countT == 1){
			numWinO++;
		}else{
			numDraw++;
		}

		countX = 0;
		countO = 0;
		countT = 0;
		for(int j = 0; j< 4;j++){
			
			if(box[j][3-j] == 'X'){
				countX++;
			}else if (box[j][3-j] == 'O'){
				countO++;
			}else if (box[j][3-j] == 'T'){
				countT = 1;
			}
			
		}
		if(countX == 4){
			numWinX++;
		}else if(countX == 3 && countT == 1){
			numWinX++;
		}else if(countO == 4){
			numWinO++;
		}else if(countO == 3 && countT == 1){
			numWinO++;
		}else{
			numDraw++;
		}

		if(numWinX == 0 && numWinO == 0 && numDraw == 0){
			result[i] = 0;// not complete
		}else{
			if(numWinX > numWinO){
				result[i] = 1; // X win
			}else if(numWinX < numWinO){
				result[i] = 2; //O win
			}else if(numWinX == numWinO){
				result[i] = 3; //draw
			}
		}
		if (result[i] == 3 && countDot > 0){
			result[i] = 0;
		}
		
	}
	for(int i = 0; i< num; i++){
		printf("Case #%d: ", i+1);
		switch(result[i]){
		case 0:
			printf("Game has not completed");
			break;
		case 1:
			printf("X won");
			break;
		case 2:
			printf("O won");
			break;
		case 3:
			printf("Draw");
			break;
		}
		printf("\n");
	}
	//scanf("%d", &num);
}