#include<stdio.h>
#include<math.h>

int f(int x,int y){
	return (int)((-2*x+1+sqrt((double)((2*x-1)*(2*x-1)+8*y)))/4);
}
int main()
{
	FILE *fi=fopen("A-small-attempt0.in","r");
	FILE *fo=fopen("A-small-attempt0.out","w");
	int T,r,t,i;

	fscanf(fi,"%d",&T);
	for(i=0;i<T;i++){
		fscanf(fi,"%d %d",&r,&t);
		fprintf(fo,"Case #%d: %d\n",i+1,f(r,t));
	}

	return 0;
	
}