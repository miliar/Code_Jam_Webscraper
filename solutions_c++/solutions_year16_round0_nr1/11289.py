#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
	FILE *f1=freopen("A-small-attempt0.in","r",stdin);
	FILE *f2=freopen("output1.txt","w",stdout);
	long long t,n,l=1;
	scanf("%lld",&t);
	while(t--)
	{
		long long h[40]={0},f=1,k=2,i,temp;
		scanf("%lld",&n);
		temp=n;
		if(n==0)
		{
			f=0;
		}
		while(f==1)
		{
			while(temp>0)
			{
				h[temp%10]=1;
				temp=temp/10;
			}
			f=0;
			for(i=0;i<=9;i++)
			{
				if(h[i]==0)
				{
					f=1;
					break;
				}
			}
			temp=n*k;
			k++;
		}
		if(n==0)
		{
			printf("Case #%lld: INSOMNIA\n",l);
		}	
		else
		{
			printf("Case #%lld: %lld\n",l,n*(k-2));
		}	
		l++;
	}
	fclose(f1);
	fclose(f2);
	return 0;
}
