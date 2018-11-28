#include <bits/stdc++.h>
void count(int digits[],long long int n)
{
	long long int a=n;
	while(a>0)
	{
		digits[a%10]=1;
		a=a/10;
	}
}
int sum(int digits[])
{
	int i,s=0;
	for(i=0;i<10;i++)
		s+=digits[i];
	return s;
}
int main()
{
	FILE *in,*out;
	in=fopen("A-large.in","r");
	out=fopen("output.txt","w");
	int t,digits[11],i,k=1;
	long long int n,j;
	fscanf(in,"%d",&t);
	while(t--)
	{
		fscanf(in,"%lld",&n);
		for(i=0;i<=10;i++)
			digits[i]=0;
		fprintf(out,"Case #%d: ",k++ );
		if(n==0)
			fprintf(out,"INSOMNIA\n");
		else
		{
			i=2;
			j=n;
			while(sum(digits)<10)
			{
			//	printf("\t%d",sum(digits) );
				count(digits,j);
				j=n*(i++);

			}
			fprintf(out,"%lld\n",j-n );
		}
	}

	fclose(in);
	fclose(out);
	return 0;
}