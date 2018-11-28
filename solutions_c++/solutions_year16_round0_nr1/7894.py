#include<iostream>
#include<stdio.h>
using namespace std;
void dig(long int a[],long int n)
{
	while(n)
	{
		a[n%10]++;
		n/=10;
	}
}
int main()
{
	int t;
	FILE *fp;
	fp=fopen("op.txt","w");
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		long int n,j,a,ta,k,b[10]={0,0,0,0,0,0,0,0,0,0};
		scanf("%ld",&n);
		if(n==0)
			fprintf(fp,"Case #%d: INSOMNIA\n",i);
		else
		{
			a=n;
			dig(b,a);
			for(j=2,ta=0;j<=1000000&&ta!=10;j++)
			{
				a=n*j;
				dig(b,a);
				for(k=0,ta=0;k<10;k++)
				{
			//		cout<<b[k]<<" ";
					if(b[k]>0)
						ta++;
				}
			//	cout<<"\n";
			}
			fprintf(fp,"Case #%d: %ld\n",i,a);
		}
	}
	return 0;
}
