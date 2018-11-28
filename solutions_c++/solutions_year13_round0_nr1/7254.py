#include <stdio.h>
#include <iostream>

using namespace std;

int main(){

int N, caso=1;
scanf("%d\n",&N);

char board[4][4];
bool vazio = false;
bool resultado = false;

int T=0, X=0, O=0;

while(caso<=N){
	if(caso!=1)
		scanf("\n");

	for(int i=0;i<4; i++){
		for(int j=0;j<4; j++){
			scanf("%c",&board[i][j]);
		}
		scanf("\n");
	}

	vazio = false;
	resultado = false;

	for(int i=0; i<4; i++){
		T=0;
		X=0;
		O=0;
		for(int k=0;k<4; k++){
			if(board[k][i] == 'T')
				T++;
			else if(board[k][i] == 'X')
				X++;
			else if(board[k][i] == 'O')
				O++;
			else if(board[k][i] == '.')
				vazio = true;
		} 
		if(X==4 || (X==3 && T==1)){
			printf("Case #%d: X won\n",caso);
			resultado = true;
		}else if(O==4 || (O==3 && T==1)){
			printf("Case #%d: O won\n",caso);
			resultado = true;}		
	}

	if(resultado == false){
		for(int k=0; k<4; k++){
			T=0;
			X=0;
			O=0;
			for(int i=0;i<4; i++){
				if(board[k][i] == 'T')
					T++;
				else if(board[k][i] == 'X')
					X++;
				else if(board[k][i] == 'O')
					O++;
				else if(board[k][i] == '.')
					vazio = true;
			}
			if(X==4 || (X==3 && T==1)){
				printf("Case #%d: X won\n",caso);
				resultado = true;
			}else if(O==4 || (O==3 && T==1)){
				printf("Case #%d: O won\n",caso);
				resultado = true;}		
		}
	}
	
	if(resultado == false){
		T=0;
		X=0;
		O=0;
		for(int k=0, i=0; k<4; k++, i++){
				if(board[k][i] == 'T')
					T++;
				else if(board[k][i] == 'X')
					X++;
				else if(board[k][i] == 'O')
					O++;
				else if(board[k][i] == '.')
					vazio = true;		
		}
		
		if(X==4 || (X==3 && T==1)){
			printf("Case #%d: X won\n",caso);
				resultado = true;
		}else if(O==4 || (O==3 && T==1)){
			printf("Case #%d: O won\n",caso);
				resultado = true;}
	}

	if(resultado == false){
		T=0;
		X=0;
		O=0;
		for(int k=0, i=3; k<4; k++, i--){
				if(board[k][i] == 'T')
					T++;
				else if(board[k][i] == 'X')
					X++;
				else if(board[k][i] == 'O')
					O++;
				else if(board[k][i] == '.')
					vazio = true;		
		}
		
			if(X==4 || (X==3 && T==1)){
				printf("Case #%d: X won\n",caso);
				resultado = true;
			}else if(O==4 || (O==3 && T==1)){
				printf("Case #%d: O won\n",caso);
				resultado = true;}
	}

	if(resultado==false){
		if(vazio==false)
			printf("Case #%d: Draw\n",caso);
		else
			printf("Case #%d: Game has not completed\n",caso);
	}

caso++;
}
return 0;
}
