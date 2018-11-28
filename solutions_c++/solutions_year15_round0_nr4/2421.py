#include <stdio.h>

int main(){
	int T,X,R,C;
	bool win;
	freopen("D-small-attempt0.in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for(int i=0; i<T; i++){
		win = false;
		printf("Case #%d: ",i+1);
		scanf("%d",&X);
		scanf("%d",&R);
		scanf("%d",&C);

		switch(X){
			case 1:
				win = true;
				break;
			case 2:
				if(R%2==0 || C%2==0) win = true;
				break;
			case 3:
				if(R>1 && C>1 && (R%3==0 || C%3==0)) win = true;
				break;
			case 4:
				if(R*C==12 || R*C==16) win = true;
		}
		if(win) printf("GABRIEL\n");
		else printf("RICHARD\n");
	}
	return 0;
}