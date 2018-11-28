#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
using namespace std;
int t,i,x;
bool f[20];
int main()
{
	//freopen("t.in","r",stdin);
	//freopen("t.out","w",stdout);
	scanf("%d",&t);
	//cout<<t<<endl;
	for(int i=1;i<=t;i++)
	{
		scanf("%d",&x);
		memset(f,true,sizeof(f));
		printf("Case #%d: ",i);
		if (x==0)
			printf("INSOMNIA\n");
		else
		{
			int p=x;
			int q=p;
			int sum=0;
			while(true)
			{
				p=q;
				while(p>0)
				{
					if (f[p%10])
					{
						sum+=p%10;
						f[p%10]=false;
					}
					p/=10;	
				}
				if (sum==45 && f[0]==false)
					break;
				q=q+x;
			}
			printf("%d\n",q);
		}
	}
	return 0;
}