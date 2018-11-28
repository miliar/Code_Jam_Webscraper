#include<iostream>
using namespace std;
int main()
{
	int i,t,flag=0,a[11],p;
	long long n,j,b,c,k;
		freopen("large.in","r",stdin);
		freopen("output1.txt","w",stdout);
	scanf("%d",&t);
	p=0;
	while(t--)
	{
		p++;
		flag=1;
		scanf("%lld",&n);
		j=1;
		k=0;
		for(i=0;i<10;i++)
		{
			a[i]=0;
		}
		while(flag==1)
		{
			b=j*n;
			if(b==k)
			{
				break;
			}
		    k=b;
			while(b!=0)
			{
				c=b%10;
				a[c]=1;
				b=b/10;
			}
			j++;
			for(i=0;i<10;i++)
			{
				if(a[i]==0)
				{
					flag=1;
					break;
				}
			}
			if(i==10)
			{
				flag=0;
			}
		}
		if(flag==1)
		{
			printf("Case #%d: INSOMNIA\n",p);
		}
		else
		{
		
		printf("Case #%d: %lld\n",p,k);
		}
		
	}
	
	fclose(stdin);
	fclose(stdout);
	
	return 0;
}
