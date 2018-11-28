 #include<iostream>
#include<cstdio>
#include<map>
#include<cstring>
using namespace std;
int taken[11];
int main()
{
	long long n,i,p,q,x,co,l,number;
	cin>>n;
	for(i=1;i<=n;i++)
	{
		scanf("%lld",&p);
		printf("Case #%lld: ",i);
		if(p==0)
			printf("INSOMNIA\n");
		else
		{
			memset(taken,0,sizeof(taken));
			co=0;
			l=1;
			q=p;
			while(1)
			{
				number=p*l;
				q=number;
				while(q)
				{
                  x=q%10;
				  q=q/10;
				if(taken[x]==0)
				{
					co++;
					taken[x]=1;
				}
				}
				
				if(co==10)
					break;
				l=l+1;


			}
			printf("%lld\n",number);
		}
	}

}