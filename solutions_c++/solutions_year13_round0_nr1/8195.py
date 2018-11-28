#include <iostream>
#include <stdio.h>
using namespace std;
int rows[4], cols[4], diag[2], dot=0;
char board[4][4];
int main(){
	int T, i, j, t, f;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		dot=0;
		f=0;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				cin>>board[i][j];
			}
			rows[i]=cols[i]=diag[i%2]=0;
		}
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(board[i][j]=='T'){
					if (board[i][(j+1)%4] == 'X' && board[i][(j+2)%4] == 'X' && board[i][(j+2)%4] == 'X')	board[i][j]='X';
					else if(board[(i+1)%4][j]== 'X' && board[(i+2)%4][j]== 'X' && board[(i+3)%4][j]=='X')	board[i][j]='X';
					else if (board[i][(j+1)%4] == 'X' && board[i][(j+2)%4] == 'X' && board[i][(j+3)%4] == 'X')	board[i][j]='X';
					else if (board[(i+1)%4][(j+1)%4]== 'X' && board[(i+2)%4][(j+2)%4]== 'X' && board[(i+3)%4][(j+3)%4]=='X')	board[i][j]='X';
					else if (board[(i+1)%4][j]=='O' && board[(i+2)%4][j]=='O' && board[(i+3)%4][j]=='O')	board[i][j]='O';
					else if (board[i][(j+1)%4]=='O' && board[i][(j+2)%4]=='O' && board[i][(j+3)%4]=='O')	board[i][j]='O';
					else {
						board[i][j]='X';
						if(board[0][3]=='X' && board[1][2]=='X' && board[2][1]=='X' && board[3][0]=='X')	board[i][j]='X';
						else	board[i][j]='O';
							//cout<<endl<<"SH "<<board[i][(j+1)%4]<<board[i][(j+2)%4]<<board[i][(j+3)%4]<<endl;
					}
				}
				if(board[i][j]=='X'){
					rows[i]+=1;
					cols[j]+=1;
					if(i==j){
						diag[0]+=1;
					}
					if((i+j)==3){
						diag[1]+=1;
					}
				}
				else if(board[i][j]=='O'){
					rows[i]+=-1;
					cols[j]+=-1;
					if(i==j){
						diag[0]+=-1;
					}
					if((i+j)==3){
						diag[1]+=-1;
					}
				}
				else{
					dot++;
				}
			}
		}
		for(i=0;i<4;i++){
			if(rows[i]==4||cols[i]==4||diag[i%2]==4){
				cout<<"Case #"<<t<<": X won"<<endl;
				f=1;
				break;
			}
			else if(rows[i]==-4||cols[i]==-4||diag[i%2]==-4){
				cout<<"Case #"<<t<<": O won"<<endl;
				f=1;
				break;
			}
		}
		if(f==0 ){
			if(dot==0) cout<<"Case #"<<t<<": Draw"<<endl;
			else cout<<"Case #"<<t<<": Game has not completed"<<endl;
		}
		// for(i=0;i<4;i++){
			// for(j=0;j<4;j++){
				// printf("%c",board[i][j]);
			// }
			// printf("\n");
		// }
		// printf("\n");
	}
	return 0;
}