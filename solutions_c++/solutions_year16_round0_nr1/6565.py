#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int l,t,n,i,j,k;
	FILE *ptr,*ptr1;
	ptr=fopen("A-large.in","r+");
	ptr1=fopen("A-large2.in","w+");
	fscanf(ptr,"%lld",&t);
	for(j=1;j<=t;j++)
	{
		fscanf(ptr,"%lld",&n);
		l=n;
		long long int a[10]={0};
		long long int f=0;
		while(1)
		{
			if(f==10)
			break;
			if(n==0)
			break;
			for(i=n;i>0;i/=10)
			{
				k=i%10;
				if(a[k]==0)
				{
					f+=1;
				}
				a[k]=1;
			}
			n+=l;
		}
		if(f==10)
		{
			fprintf(ptr1,"Case #%lld: %lld\n",j,n-l);
		}
		else
		{
			fprintf(ptr1,"Case #%lld: INSOMNIA\n",j);
		}
	}
	fclose(ptr);
	fclose(ptr1);
	return 0;
}
