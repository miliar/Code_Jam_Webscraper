#include<stdio.h>
#include<math.h>
FILE*in=fopen("input.txt","r");
FILE*out=fopen("output.txt","w");
int T;
long double R,P;
int main()
{
	fscanf(in,"%d",&T);
	int t;
	long double A,B,C;
	long double X1,X2;
	for(t=1;t<=T;t++)
	{
		fscanf(in,"%lf %lf",&R,&P);
		fprintf(out,"Case #%d: ",t);
		A=2; B=2*R-1; C=-P;
		X2=(-B+sqrt(B*B-4*A*C))/(2*A);
		fprintf(out,"%lld\n",(long long)X2);
	}
}