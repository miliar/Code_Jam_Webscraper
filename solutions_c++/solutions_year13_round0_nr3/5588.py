#include <stdio.h>
#include <stdlib.h>

FILE *fi=fopen("C-small-attempt0.in","r");
FILE *fo=fopen("C-small-attempt0.out","w");


int main()
{
	int j[100]={0};
	int T=0, A=0, B=0, i=0, a=0;

	fscanf(fi,"%d",&T);
	for(a=0;a<T;a++){
		fscanf(fi,"%d %d",&A,&B);
		for(i=A;i<=B;i++){
			if(i==1||i==4||i==9||i==121||i==484){
				j[a]++;
			}
		}
	}
	for(a=0;a<T;a++){
		fprintf(fo,"Case #%d: %d\n",a+1,j[a]);
	}

	return 0;
}