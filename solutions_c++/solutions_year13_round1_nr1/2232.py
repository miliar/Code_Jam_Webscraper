#include<stdio.h>


int main()
{
	FILE* ip=fopen("A-small-attempt0.in","r");
	FILE* op=fopen("A-small-attempt0.out","w");

	long long k,T;
	long long int t,r;
	fscanf(ip,"%lld",&T);

	for(k=0;k<T;k++)
	{
		long long int n=1;
		fscanf(ip,"%lld%lld",&r,&t);
		long long int S=2*r+4*n-3;
		while(t>=S)
		{
			t-=S;
			n++;
			S=2*r+4*n-3;
		}
		fprintf(op,"Case #%lld: %lld\n",k+1,n-1);

	}
	return 0;
}