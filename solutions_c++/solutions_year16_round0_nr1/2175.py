#include<stdio.h>

int main(void)
{
	int t,n,i,m,j,cnt,tmp;
	int check[10];
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d",&n);
		printf("Case #%d: ",i);
		if(n==0)
		{
			printf("INSOMNIA\n");
			continue;
		}
		m=0;
		for(j=0;j<10;j++)
			check[j]=0;
		cnt=0;
		while(1)
		{
			m+=n;
			tmp=m;
			while(tmp)
			{
				check[tmp%10]=1;
				tmp/=10;
			}
			cnt=0;
			for(j=0;j<10;j++)
				cnt+=check[j];
			if(cnt==10)
				break;
		}
		printf("%d\n",m);
	}
}