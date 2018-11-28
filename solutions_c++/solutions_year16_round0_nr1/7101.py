#include<stdio.h>
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	long long int t,i=1;
	scanf("%lld",&t);
	static int ar[11];
	while(i<=t)
	{
		long long int n,m=1,temp,num,numb;
		scanf("%lld",&n);
		if(n==0)
		{
			printf("Case #%lld: INSOMNIA\n",i);
			i++;
		}
		else{
		while(1){
			temp=n*m;
			numb=temp;
			while(temp>0)
			{
				ar[temp%10]=i;
				temp/=10;
			}
			num=1;
			for(int j=0;j<10;j++)
			{
				if(ar[j]!=i)
				{
					num=0;
					break;
				}
			}
			if(num)
			{
				break;
			}
			else
			{
				m++;
			}
		}
		printf("Case #%lld: %lld\n",i,numb);
		i++;
	}
	}
	return 0;
}
