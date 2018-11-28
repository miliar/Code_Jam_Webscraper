#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	int time=0,x=1;
	scanf("%d",&time);
	while(time--){
		int k=0,shy[1050];
		scanf("%d",&k);
		memset(shy,0,sizeof(shy));
		char tmp;
		scanf("%*c%c",&tmp);
		shy[0]=tmp-'0';
		int total=shy[0],need=0;
		for(int a=1;a<=k;a++){
			scanf("%c",&tmp);
			shy[a]=tmp-'0';
			if(a<=total||shy[a]==0){
				total=total+shy[a];
			}
			else{
				need=need+(a-total);
				total=a+shy[a];
			}
		}
		printf("Case #%d: %d\n",x,need);
		x++;
	}
	return 0;
}
