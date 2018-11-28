#include <stdio.h>

int main(){
	int t,x,r,c;
	scanf("%d",&t);
	for(int i=0; i<t; i++){
		scanf("%d%d%d",&x,&r,&c);
		if(x==1) {
			printf("Case #%d: GABRIEL\n", i+1);
		} else if(x==2) {
				if(r%2 == 0 || c%2==0) {
					printf("Case #%d: GABRIEL\n", i+1);
				} else {
				printf("Case #%d: RICHARD\n", i+1);
				}
		} else if(x==3){
			if((r==3 && c==2) || (r==4 && c==3) || (r==2 && c==3) ||  (r==3 && c==4) || (r==3 && c==3)){
				printf("Case #%d: GABRIEL\n", i+1);
			} else {
				printf("Case #%d: RICHARD\n", i+1);
			}
		} else if(x==4 ) {
			if(r*c>=12) {
				printf("Case #%d: GABRIEL\n", i+1);
			} else {
				printf("Case #%d: RICHARD\n", i+1);
			}
		}
	}
	return 0;
}