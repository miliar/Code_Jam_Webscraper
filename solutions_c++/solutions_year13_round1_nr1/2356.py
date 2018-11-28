#include <stdio.h>
#include <stdlib.h>

FILE *fi=fopen("A-small-attempt0.in","r");
FILE *fo=fopen("A-small-attempt0.out","w");

int main()
{
	int r[1000],t[1000];
	int c=0, T=0, i=0, j=0, cir=0;
	
	fscanf(fi,"%d",&T);
	for(i=0;i<T;i++){
		fscanf(fi,"%d %d",&r[i],&t[i]);
	}

	for(i=0;i<T;i++){
		for(j=0;t[i]>=0;j++){
			cir=(r[i]+2*j+1)*(r[i]+2*j+1)-(r[i]+2*j)*(r[i]+2*j);
			t[i]=t[i]-cir;
		}
		fprintf(fo,"Case #%d: %d\n",i+1,j-1);
	}

	return 0;
}