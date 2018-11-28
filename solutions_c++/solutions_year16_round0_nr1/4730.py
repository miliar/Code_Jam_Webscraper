#include<stdio.h>
int main(){
	long long int tc,n,i,j,x,count,m,inc=1,temp;
	scanf("%lld",&tc);
	while(tc--)
	{
		scanf("%lld",&n);
		count=0;
		bool b[20]={0};
		m=n;
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",inc++);
			continue;
		}
		while(count<10)
		{
			x=n;
			while(x>0)
			{
				temp=x%10;
				if(b[temp]==0)
				{
					b[temp]=1;
					count++;
				}
				x=x/10;
			}
			n+=m;
		}
		printf("Case #%d: %lld\n",inc++,n-m);
	}
	return 0;
}
