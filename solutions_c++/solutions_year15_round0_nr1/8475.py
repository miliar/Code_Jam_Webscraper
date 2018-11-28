#include <stdio.h>

int main(){
	int kolk;
	scanf("%i",&kolk);

	for(int i=0;i<kolk;i++){
		int vstali=0,sMAX,poklicani=0;
		char sTemp;
		scanf("%i ",&sMAX);

		while(scanf("%c",&sTemp)!=EOF and (sTemp>'9' or sTemp<'0'));
		vstali+=sTemp-'0';

		for(int j=1;j<sMAX+1;j++){
			scanf("%c",&sTemp);
			if(j>vstali+poklicani){
				poklicani+=j-(vstali+poklicani);
			}
			vstali+=sTemp-'0';
		}
		printf("Case #%i: %i\n",i+1,poklicani);
	}
	return 0;
}
