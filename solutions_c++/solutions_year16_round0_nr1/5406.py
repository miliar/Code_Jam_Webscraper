#include<bits/stdc++.h>

using namespace std;
void seedigits(long long int num,int dig[])
{
	int d;
	while(num!=0)
	{
		d = num%10;
		num/=10;
		dig[d] = 1;
	}
}
int testdig(int dig[])
{
	int a=0,i;
	for(i=0;i<10;i++)
		a+=dig[i];
	if(a==10)
		return 1;
	else
		return 0;
}

 int main()
{
	 int t,cs=0;
	long long int n,i;
	scanf("%d",&t);
	while(t--)
	{	int dig[20] = {0};
		cs++;
		printf("Case #%d: ",cs);
		scanf("%lld",&n);
		if(n==0)
		{
			printf("INSOMNIA\n");
			continue;
		}
		long long int c = 0;
		long long int num = n;
		while(1)
		{
			//printf("%lld\n",num);
			seedigits(num,dig);
			c = testdig(dig);
			if(c==1)
				break;
			num+=n;

		}
		printf("%lld\n",num);
	}

	return 0;
}