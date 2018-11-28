#include<stdio.h>
FILE *in=fopen("1.in","r");
FILE *out=fopen("1.out","w");
long long int TT;
long long int P,Q,GCD,TmpQ;
long long int gcd(long long int big,long long int small)
{
   if(small==0) return big;
   else if(big>small) return gcd(small,big%small);
   else return gcd(big,small%big);
}
int main()
{
	long long int i,j;
	fscanf(in,"%lld",&TT);
	for(i=1;i<=TT;i++)
	{
		fscanf(in,"%lld/%lld",&P,&Q);
		GCD=gcd(Q,P);
		P/=GCD;
		Q/=GCD;
		TmpQ=Q;
		while(TmpQ%2==0 && TmpQ!=1)TmpQ/=2;
		if(TmpQ!=1)fprintf(out,"Case #%lld: impossible\n",i);
		else
		{
			for(j=1;;j++)
			{
				P*=2;
				if(P>=Q)break;
			}
			fprintf(out,"Case #%lld: %lld\n",i,j);
		}
	}
	return 0;
}