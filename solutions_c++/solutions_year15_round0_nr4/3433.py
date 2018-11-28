#include <stdlib.h>
#include <stdio.h>

int main(){
	//freopen("input.in","r",stdin);
	freopen("D-small-attempt2.in","r",stdin);
	freopen("D-small-attempt2.out","w",stdout);

	int lines;
	int x, r, c;

	scanf("%d", &lines);

	for(int i = 0; i < lines; ++i){
		scanf("%d", &x);
		scanf("%d", &r);
		scanf("%d", &c);

		switch(x){
			case 1:
				printf("Case #%d: GABRIEL", i + 1);
				break;
			case 2:
				if((r * c) % 2 == 0){
					printf("Case #%d: GABRIEL", i + 1);
				}else{
					printf("Case #%d: RICHARD", i + 1);
				}
				break;
			case 3:
				if((r * c) % x == 0 && r > 1 && c > 1){
					printf("Case #%d: GABRIEL", i + 1);
				}else{
					printf("Case #%d: RICHARD", i + 1);
				}
				break;
			case 4:
				if((r * c) > 9){
					printf("Case #%d: GABRIEL", i + 1);
				}else{
					printf("Case #%d: RICHARD", i + 1);
				}
				break;
		}
		printf("\n");
	}


	return 0;
}
