#include<bits/stdc++.h>
using namespace std;
int main()
{
	FILE *f=fopen("A-large.in","r");
	FILE *f1=fopen("op","w");
	int a[10];
	int t,b;
	long long int n,temp,temp1;
	fscanf(f,"%d",&t);
	for(int i=1;i<=t;i++)
	{
		fscanf(f,"%lld",&n);
		for(int i=0;i<10;i++)
		a[i]=0;
		int c=1;
		temp=n;
		fprintf(f1,"Case #%d: ",i);
		if(n==0)
		{
			fprintf(f1,"INSOMNIA\n");
		}
		else{
		while(1)
		{
			n=temp*c;
			temp1=n;
			while(n!=0)
			{
				b=n%10;
				a[b]=1;
				n=n/10;
			}
			int j;
			for(j=0;j<10;j++)
			{
				if(a[j]==0)
				{
					break;
				}
			}
			if(j==10)
			break;
			c++;
		}
		fprintf(f1,"%lld\n",temp1);
        }}
	return 0;
}
