#include<bits/stdc++.h>
#define li long int

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A1large111.out.txt","w",stdout);

    int t;
	li n,p,i=1,j,f,k;
	scanf("%d",&t);
	while(i<=t)
	{
		scanf("%ld",&n);
		if(n==0)
			printf("Case #%d: INSOMNIA\n",i);
		else
		{
			bool d[10]={false};
			j=0;
			while(true)
			{
				++j;
				f=0;
				for(k=0;k<=9;++k)
				{
					if(d[k]==false)
					{
						f=1;
						break;
					}
				}
				if(f==0)
				{
					printf("Case #%d: %ld\n",i,(j-1)*n);
					break;
				}
				else
				{
					p=n*j;
					//printf("%ld*%ld=%ld\n",n,j,p);
					while(p>0)
					{
						d[p%10]=true;
						p=p/10;
					}
				}
			}
		}
		++i;
	}

    return 0;
}
