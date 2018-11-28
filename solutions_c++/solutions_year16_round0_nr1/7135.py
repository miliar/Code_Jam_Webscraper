#include<bits/stdc++.h>
using namespace std;
typedef long long int des;
des hash[10];
int main()
{	int t;
	des n,counta,rem,copy,i;
	des hash[10];
	int k=1;
	scanf("%d",&t);
	while(t--)
	{	for(i=0;i<10;i++)hash[i]=0;
		counta=0;	
		scanf("%lld",&n);
		copy=n;
		if(n==n*2)
		{	printf("Case #%d: INSOMNIA\n",k++);//INSOMIAN\n");
			continue;
		}
		while(copy>0)
		{	rem=copy%10;
			if(hash[rem]==0)
			{	hash[rem]=1;
				counta++;
			}
			copy/=10;
		}
		if(counta==10)
		{	printf("Case #%d: %lld\n",k++,n);          // Case #1: INSOMNIA
		}
		else
		{	i=2;
			while(true)
			{	copy=i*n;
				while(copy>0)
				{	rem=copy%10;
					if(hash[rem]==0)
					{	hash[rem]=1;
						counta++;
					}
					copy/=10;
				}
				
				if(counta==10)
				{	printf("Case #%d: %lld\n",k++,i*n);
					break;
				}
				i++;
			}
		}
	}
	return 0;
}
			
	
	
