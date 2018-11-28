#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	for(int j=1;j<=t;j++)
	{
		int has[10]={0};
		long long n,x,y,i=1,k,z;
		scanf("%lld",&n);
		if(n==0) {
			printf("Case #%d: INSOMNIA\n",j);
			continue;
		}
		while(1)
		{
			x=i*n;
			z=x;
			while(x>0)
			{
				y=x%10;
				has[y]=1;
				x/=10;
			}
			for(k=0;k<10;k++)
				if(has[k]==1)
					continue;
				else break;
			
			if(k==10)
				break;	
			i++;	
		}
		printf("Case #%d: %lld\n",j,z);
	}
	return 0;
}
