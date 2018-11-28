#include <stdio.h>

int main(void){
	//printf("%d\n", 3-3/2);
	int testcase;
	scanf("%d", &testcase);

	for(int i=1; i<=testcase; i++){
		int x, r, c;
		scanf("%d %d %d", &x, &r, &c);
		//printf("%d %d %d ", x, r, c);

		if((r*c) % x != 0){
			printf("Case #%d: %s\n", i, "RICHARD");
		}
		else if(r < x && c < x){
			printf("Case #%d: %s\n", i, "RICHARD");
		}
		else if((r < x-x/2 || c < x-x/2) || ((x==4) && (r<3 || c < 3))){
			printf("Case #%d: %s\n", i, "RICHARD");
		}
		else{
			printf("Case #%d: %s\n", i, "GABRIEL");
		}			
	}
	return 0;
}