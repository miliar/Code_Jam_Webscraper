#include <stdio.h>
int main(){
	FILE *f = fopen("outD.txt","wt");
	int T,i;
	scanf("%d",&T);
	for(i=0;i<T;i++){
		fprintf(f,"Case #%d: ",i+1);
		int K,C,S;
		scanf("%d %d %d",&K,&C,&S);
		for(int j=0;j<S;j++){
			fprintf(f,"%d ", j+1);
		}
		fprintf(f,"\n");
	}
	fclose(f);
}