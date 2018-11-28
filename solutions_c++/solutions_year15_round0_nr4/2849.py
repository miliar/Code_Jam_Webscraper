#include <stdio.h>

int main() {
	int T, X, R, C;

	scanf("%d", &T);

	for(int t=0; t<T; t++) {

		scanf("%d %d %d", &X, &R, &C);

		if(X == 1) {
			printf("Case #%d: GABRIEL\n", t+1);
			continue;
		}

		if(X > R && X > C) {
			printf("Case #%d: RICHARD\n", t+1);
			continue;
		}

		if(X == 2) {
			if(R==1 && C==1) {
				printf("Case #%d: RICHARD\n", t+1);
				continue;
			}

			else if((R==1 && C==3) || (R==3 && C==1)) {
				printf("Case #%d: RICHARD\n", t+1);
				continue;
			}

			else if(R==3 && C==3) {
				printf("Case #%d: RICHARD\n", t+1);
				continue;
			}

			else {
				printf("Case #%d: GABRIEL\n", t+1);
				continue;
			}
		}

		else if(X==3) {
			if((R==2 && C==3) || (R==3 && C==2)) {
				printf("Case #%d: GABRIEL\n", t+1);
				continue;
			}
			else if((R==4 && C==3) || (R==3 && C==4)) {
				printf("Case #%d: GABRIEL\n", t+1);
				continue;
			}
			else if(R==3 && C==3) {
				printf("Case #%d: GABRIEL\n", t+1);
				continue;
			}
			else {
				printf("Case #%d: RICHARD\n", t+1);
				continue;
			}
		}

		else if(X==4) {
			if ((R==3 && C==4) || (R==4 && C==3)) {
				printf("Case #%d: GABRIEL\n", t+1);
				continue;
			} else if(R==4 && C==4) {
				printf("Case #%d: GABRIEL\n", t+1);
				continue;
			} else {
				printf("Case #%d: RICHARD\n", t+1);
				continue;
			}
		}
	}
	return 0;
}