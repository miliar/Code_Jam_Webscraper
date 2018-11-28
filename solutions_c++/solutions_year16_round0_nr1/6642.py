#include<bits/stdc++.h>

int main()
{
	int t,i,j,k,n,p,u,T,m;
	int a[10];
	char c[1000000],e;
	scanf("%d",&t);
	for(T=1;T<=t;++T)
	{
		scanf("%d",&n);
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",T);
			continue;
		}
		i=1;
		for(j=0;j<10;++j)
			a[j]=0;
		while(1)
		{
			k=i*n;
			while(k)
			{
				a[k%10]=1;
				k=k/10;
			}
			p=0;
			for(j=0;j<10;++j)
				if(a[j])
					p++;
			if(p==10)
				break;
			i++;
		}
		k=i*n;
		printf("Case #%d: %d\n",T,k);
	}
	return 0;
}
