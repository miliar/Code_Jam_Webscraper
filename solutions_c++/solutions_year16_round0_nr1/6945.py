#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int checkArray[10]={0};
bool check();
int main(){
	int T,input,slice,cnt_i,cnt_j;
	scanf("%d",&T);
	for(cnt_i=0;cnt_i < T;cnt_i++){
		for(cnt_j=0;cnt_j<10;cnt_j++){
			checkArray[cnt_j] = 0;
			//printf("checkArray[%d]: %d\n",cnt_j,checkArray[cnt_j]);
		}
		scanf("%d",&input);
		if(input == 0)
			printf("Case #%d: INSOMNIA\n",cnt_i+1);
		else{
			for(cnt_j=1;!check();cnt_j++){
				slice = input*cnt_j;
				while(slice>0){
					checkArray[slice%10] = 1;
					slice = slice/10;
				}
			}
			printf("Case #%d: %d\n",cnt_i+1,input*(cnt_j-1));
		}
	}
	return 0;
}

bool check(){
	for(int cnt_j=0;cnt_j<10;cnt_j++)
		if(checkArray[cnt_j]==0)
			return false;
	return true;
}
