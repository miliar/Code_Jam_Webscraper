#include<stdio.h>
using namespace std;
long double C;
long double F;
long double X;
long double y;
long double f2;
int main()
{
//	FILE* fin = fopen("A-small-attempt0.in","r");
	FILE* fin = fopen("input.txt","r");
	FILE* fout = fopen("output.txt","w+");
	int n=0;
	fscanf(fin,"%d",&n);
	for(int i = 1; i <= n ; i++)
	{
		C=0.0;
		F=0.0;
		X=0.0;
		fscanf(fin,"%lle",&C);
		fscanf(fin,"%lle",&F);
		fscanf(fin,"%lle",&X);
		long double f1 = 2;
		y=0.0;
		while(1)
		{
			f2=f1+F;
			long double lhs = C/f1 + X/f2;
			long double rhs = X/f1;
			if(lhs < rhs)
			{
				y=y+C/f1;
				f1=f2;
			}
			else
			{
				y = y + X/f1;
				break;
			}
		}
		fprintf(fout,"Case #%d: %lle\n",i,y);

	}
	fclose(fin);
	fclose(fout);
	return 0;
}
