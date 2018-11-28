#include<stdio.h>
FILE *in,*out;
long long calc(int n,long long m)
{
	long long v;
	if( m<=0 ) return -1;
	v=1LL<<n;
	while( m>1 )
	{
		m/=2;
		v>>=1;
	}
	return (1LL<<n)-v;
}
int main()
{
	in=fopen("b.in","r");
	out=fopen("b.out","w");
	int tc,test;
	fscanf(in,"%d",&tc);
	for(test=1;test<=tc;test++)
	{
		fprintf(out,"Case #%d: ",test);
		int n;
		long long k;
		fscanf(in,"%d%lld",&n,&k);
		fprintf(out,"%I64d",(1LL<<n)-2-calc(n,(1LL<<n)-k));
		fprintf(out," %I64d",calc(n,k));
		fprintf(out,"\n");
	}
	return 0;
}