
#include <cstring>
#include <string.h>
#include <sstream>
#include <iostream>

using namespace std;


#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)


int N;
int n=4;
int t;
char winner='N';

char board[4][4];

//#define SMALL
#define LARGE
int main() {
#ifdef SMALL
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small.out","w",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
#endif


	cin >> N;
	rep2(nn,1,N+1) {

		rep(i,n)
					cin>>board[i];

		printf("Case #%d: ", nn);

		rep(i,n){ //horizontal
			winner = board[i][0];
			rep(j,n){
				if(board[i][j] == winner || winner == 'T' ) winner = board[i][j] ;
				else {if(board[i][j] != 'T')	winner = 'N';}

			}
			if(winner == 'X' || winner == 'O'){
				printf("%c won\n", winner);
				goto END;
			}

		}

		rep(j,n){ //vertical
			winner = board[0][j];
			rep(i,n){
				if(board[i][j] == winner || winner == 'T' ) winner = board[i][j] ;
				else if(board[i][j] != 'T')	winner = 'N';
			}
			if(winner == 'X' || winner == 'O'){
				printf("%c won\n", winner);
				goto END;
			}

		}
		//diagonal 1
		winner = board[0][0];
		rep(i,n){


			if(board[i][i] == winner || winner == 'T' ) winner = board[i][i] ;
			else if(board[i][i] != 'T')	winner = 'N';
		}
		if(winner == 'X' || winner == 'O'){
			printf("%c won\n", winner);
			goto END;
		}

		//diagonal 2
		winner = board[0][n-1];
		rep(i,n){


			if(board[i][n-1-i] == winner || winner == 'T' ) winner = board[i][n-1-i] ;
			else if(board[i][n-1-i] != 'T')	winner = 'N';
		}
		if(winner == 'X' || winner == 'O'){
			printf("%c won\n", winner);
			goto END;
		}

		rep(i,n)
		rep(j,n)
		if(board[i][j]== '.'){//not completed
			printf("Game has not completed\n");
			goto END;
		}


		printf("Draw\n");

		END:;
		//cin>>t; //skip emplty line

	}
	return 0;


}




