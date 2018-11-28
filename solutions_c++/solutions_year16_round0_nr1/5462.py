#include<bits/stdc++.h>
using namespace std;
long long a[10];
void sett(long long k)
{
	while(k>0)
	{
		a[k%10]=1;
		k/=10;
	}
}

bool open()
{
	for(long long j=0;j<10;j++)
	{
		if(a[j]==0) return 1;
	}
	return 0;
}

long long ans[1000006];
int main()
{
	long long i,j,k;
	ans[0]=-1;
	for(i=1;i<=1000001;i++)
	{
		for(j=0;j<10;j++) a[j]=0;
		k=0;
		while(open())
		{
			k+=i;
			sett(k);
		}
		//cout<<i<<' '<<k/i<<endl;
		ans[i]=k;
		/*if((k/i) >= maxiter)
		{
			maxiter=(k/i);
			maxpoint=i;
			//cout<<"hello "<<k/i<<' '<<maxiter<<' '<<maxpoint<<endl;
		}*/
	}
	scanf("%lld",&j);
	for(i=1;i<=j;i++)
	{
		scanf("%lld",&k);
		printf("Case #%lld: ",i);
		if(ans[k]==-1) printf("INSOMNIA\n");
		else printf("%lld\n",ans[k]);
	}
}
