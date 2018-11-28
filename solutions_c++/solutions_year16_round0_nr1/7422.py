#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t,j,k,i,a[10],l=1;
	
	scanf("%d",&t);
	long long n,r,q,m;
	while(l<=t)
	{
		for(i=0;i<10;i++)
			a[i]=0;
		scanf("%lld",&n);
		if(n==0)
			printf("Case #%d: INSOMNIA\n",l);
		else
		{
			j=1;i=1;k=0;
			while(j==1)
			{
				q=i*n;
				m=q;
				while(q)
				{
					r=q%10;
					if(a[r]==0)
					{
						a[r]=1;
						k++;	
					}
					
					q=q/10;
				}
				//printf("%d\n",k);
				if(k==10)
					break;
				i++;
			}
			printf("Case #%d: %lld\n",l,m);
		}
		l++;	
	}
	return 0;
}