#include <stdio.h>
#include <iostream>


void test(FILE *p,int x,FILE *q){
	int a[4][4];
	int row1,row2,i,j;
	int b[4],s=0,aux;
	fscanf(p,"%d",&row1);
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			fscanf(p,"%d",&a[i][j]);
		}
	}
	for(i=0;i<4;i++){
		b[i] = a[row1-1][i];
	}
	fscanf(p,"%d",&row2);
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			fscanf(p,"%d",&a[i][j]);
		}
	}
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if(a[row2-1][i] == b[j]){
				s++;
				aux=j;
			}
		}
	}
	if(s==0){
		printf("Case #%d: Volunteer cheated!\n\n",x);
		fprintf(q,"Case #%d: Volunteer cheated!\n",x);
	}
	else if(s==1) {
		printf("Case #%d: %d\n\n",x,b[aux]);
		fprintf(q,"Case #%d: %d\n",x,b[aux]);
	}
	else {
		printf("Case #%d: Bad magician!\n\n",x);
		fprintf(q,"Case #%d: Bad magician!\n",x);
	}
}

int main(){
	char c;
	int t,n=1;
	FILE *p,*q;
	q = fopen("output.txt","w");
	if (q==NULL){ 
		printf( "erro\n\n");
	}
	p = fopen("A-small-attempt1.in","r");
	if (p==NULL){ 
		printf( "erro\n\n");
	}
	fscanf(p,"%d",&t);
	//printf("%d\n",t);
	
	while (!feof(p)){
		test(p,n,q);
		n++;
	}
	fclose(p);
	fclose(q);
	system("PAUSE");
	return 0;
}
/*
*/