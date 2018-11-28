#include <stdio.h>
int main()
{
	int T,X,R,C,i,winner;
	scanf("%d",&T);
	for(i = 1; i <= T; i++) {
		scanf("%d%d%d",&X,&R,&C);
		winner = 2;
		if(X == 1) {
			winner = 2;
		}
		else if(X == 2) {
			if(R == 1) {
				if(C == 1 || C == 3) {
					winner = 1;
				}
			}
			else if(R == 3 ) {
				if(C == 1 || C ==3) {
					winner = 1;
				}
			}
		}
		else if(X == 3) {
			if(R == 1) {
				winner = 1;
			}
			else if(R == 2) {
				if(C == 1 || C == 2 || C == 4){
					winner = 1;
				}
			}
			else if(R == 3 && C  == 1) {
				winner = 1;
			}
			else if(R == 4) {
				if(C == 1 || C == 2 || C == 4) {
					winner = 1;
				}
			}
		}
		else if(X == 4) {
			if(R == 1) {
				winner = 1;
			}
			else if(R == 2) {
				winner = 1;
			}
			else if(R == 3) {
				if(C < 4) {
					winner = 1;
				}
			}
			else if(R == 4) {
				if(C <= 2 ){
					winner = 1;
				}
			}
		}
		if(winner == 1) {
			printf("Case #%d: RICHARD\n",i);
		}
		else {
			printf("Case #%d: GABRIEL\n",i);
		}
	}
	return 0;
}
