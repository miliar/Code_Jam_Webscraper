#include <cmath>
#include <cstdlib>
#include <cstdio>

using namespace std;

const int size_board = 4;
const int size_T = 1000;

struct {
	int board [size_board] [size_board];
	int empty ;
} ex [size_T] ;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;

	scanf("%d", &t);
	for(int i = 0; i < t; i++) {
		char buffer [size_board + 1];

		gets(buffer); 
		ex[i].empty = 0;
		for(int j = 0; j < size_board; j++) {
			gets(buffer); 
			for(int k = 0; k < size_board; k++) { 
				if (buffer[k]=='O') {
					ex[i].board[j][k] = 0; 
				}	else  if (buffer[k]=='X') {
							  ex[i].board [j][k] = 1;
						  }	 else if (buffer[k]=='T') {
									  ex[i].board[j][k] = 2;
								  }   else {ex[i].board[j][k] = -1; ex[i].empty++;}

			}
		}
	}

	for(int k = 0; k < t; k++) {
		int flagW[2]={0,0};
		
		for(int it = 0; it < 2; it++) {
			for(int i = 0; i < size_board; i++) {
				int flag = 0;
				for(int j = 0; j < size_board; j++) {
					if(ex[k].board[i][j] != it && ex[k].board[i][j] != 2) {
						flag = 1;
						break;
					}
				}
				if(!flag) {
					flagW[it] = 1;
				}             			
			}
		}

		for(int it = 0; it < 2; it++) {
			for(int j = 0; j < size_board; j++) {
				int flag = 0;
				for(int i = 0; i < size_board; i++) {
					if(ex[k].board[i][j] != it && ex[k].board[i][j] != 2) {
						flag = 1;
						break;
					}
				}
				if(!flag) {
					flagW[it] = 1;
				}             			
			}
		}	

		for(int it = 0; it < 2; it++) {
			int flag = 0;
			for(int i = 0; i < size_board; i++) {
				if(ex[k].board[i][i] != it && ex[k].board[i][i] != 2) {
						flag = 1;
						break;
				 }
			}
			if(!flag) {
				flagW[it] = 1;
			}  
		}
		for(int it = 0; it < 2; it++) {
			int flag = 0;
			for(int i = 0; i < size_board; i++) {
				int j = 3 - i;
				if(ex[k].board[i][j] != it && ex[k].board[i][j] != 2) {
						flag = 1;
						break;
				}
										
			}
			if(!flag) {
					flagW[it] = 1;
				}
		}
		
		if (flagW[0]==flagW[1]) {
			if (flagW[0]==0&&ex[k].empty==0) {
				printf("Case #%d: Draw\n", k+1);
			}
			if (flagW[0]==0&&ex[k].empty!=0) {
				printf("Case #%d: Game has not completed\n", k+1);
			}
			if (flagW[0]) {
				printf("Case #%d: Draw\n", k+1);
			}
		}   else if (flagW[0]==1) {
					 printf("Case #%d: O won\n", k+1);
				 }  else
				 printf("Case #%d: X won\n", k+1);
		 		 
  //	 printf("\n%d %d %d\n", flagW[0], flagW[1], ex[k].empty );
	}
   
  //	getchar(); getchar();

	
	return 0;
}
 
