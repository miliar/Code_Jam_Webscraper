#include <cstdio>
#include <cstdlib>
#include <iostream>

int main(){
	int T;

	scanf("%d",&T);
	for(int i=1;i<=T;i++){
		int SMax,count=0,accuAu=0;
		char shyLvl[1005];

		scanf("%d",&SMax);
		scanf("%s",shyLvl);
		accuAu+=shyLvl[0]-'0';
		for(int j=1;j<=SMax;j++){
			if(accuAu + count < j){
				count=count + j - (accuAu+count);
			}
			accuAu+=shyLvl[j]-'0';
		}
		printf("Case #%d: %d\n",i,count);
	}
	return 0;
}
