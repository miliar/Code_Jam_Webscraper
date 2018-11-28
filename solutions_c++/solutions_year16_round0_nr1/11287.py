#include<stdio.h>
int a[10],ans;
//FILE *fp=fopen("test.txt", "w");;
void func(long long int n)
{
	int d;
	while(n!=0)
	{
		d=n%10;
		n=n/10;
		if(a[d]!=1)
		{
			a[d]=1;
			ans++;
		}
	}
}

int main()
{
	int t,i;
	long long int n,k;
	int j=1;
	scanf("%d",&t);
	while(t--)
	{
		for(i=0;i<n;i++)
		{
			a[i]=0;
		}
		ans=0;
		scanf("%lld",&n);
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",j);
			j=j+1;
		}
		else
		{
			//printf("ans:%d  n:%lld  ",ans,n);
			
		for(i=0;i<10;i++)
		{
			a[i]=0;
		}
			i=2;
			k=n;
			while(ans!=10)
			{
				//printf("adf %lld ppp \n",ans,k);
				func(k);
			//	printf("k:111 %lld ",k);
				k=i*n;
				i=i+1;
			}
			printf("Case #%d: %lld \n",j,k-n);
			j=j+1;
		}		
	}
	return 0;
}
