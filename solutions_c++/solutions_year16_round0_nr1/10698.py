#include<cstdio>
#include<iostream>
using namespace std;
int a[11];
int main()
{
	int t;
	FILE *f,*h;
	f=fopen("a.out","w");
	h=fopen("A-large.in","r");
	fscanf(h,"%d",&t);
	for(int i=1;i<=t;i++)
	{
		unsigned long long n;
		fscanf(h,"%lld",&n);
		fprintf(f,"Case #%d: ",i);
		if(!n)
		fprintf(f,"INSOMNIA\n");
		else
		{
			for(int j=0;j<=9;j++)
			a[j]=1;
			long long k=1,m=10,q=0;
			while(m)
			{
				n=n*k;
				long long l=n;
				while(l)
				{
					q=l%10;
					if(a[q]==1)
					{
						m--;
						a[q]--;
					}
					l=l/10;
				}
				n=n/k;
				k++;
			}
			fprintf(f,"%lld\n",n*(k-1));
		}
	}
	fclose(f);
	fclose(h);
}
