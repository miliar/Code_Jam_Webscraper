#include <stdio.h>
int main(void){
int t,T,ans,ans2,mat1[5][5],mat2[5][5],cont;
int sol=0;
freopen("A-small-attempt0.in","r",stdin);
freopen("A-small-attempt0.out","w",stdout);
scanf("%d",&T);
for(t=1;t<=T;t++){
	scanf("%d",&ans);
	for(int i=1;i<=4;i++){
		for(int j=1;j<=4;j++){
			scanf("%d",&mat1[i][j]);
		}
	}
	scanf("%d",&ans2);
	for(int i=1;i<=4;i++){
		for(int j=1;j<=4;j++){
			scanf("%d",&mat2[i][j]);
		}
	}
	cont=0;
	for(int i=1;i<=4;i++){
		//printf("\n%d-> ",mat1[ans][i]);
		for(int j=1;j<=4;j++){
			//printf("%d ",mat2[ans2][j]);
			if(mat1[ans][i]==mat2[ans2][j]){
				cont++;
				sol=mat1[ans][i];
			}
		}
	}
	//printf("cont: %d",cont);
	printf("Case #%d: ",t);
	if(cont==1){
		printf("%d",sol);
	}
	else if(cont==0){
		printf("Volunteer cheated!");
	}
	else{
		printf("Bad magician!");
	}
	if(t<T)puts("");
}
getchar();
getchar();
return 0;
}
