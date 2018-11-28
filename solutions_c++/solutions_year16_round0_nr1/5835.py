#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
	ll t,i,j,k,m,n,r,a[10];
	freopen("A-small-practice.in", "r", stdin);
	freopen("A-small-practice.out", "w", stdout);
	cin>>t;
	i=1;
	sree:
	while(i<=t)
	{
		for(j=0;j<10;j++) a[j]=0;
		cin>>r;ll f=r;
		if(r==0)
		{
			printf("Case #%lld: INSOMNIA\n",i);
		}
		else
		{
			m=2;n=r;
			while(1)
			{
				n=r;
				while(n)
				{
					k=n%10;
					a[k]++;
					n=n/10;
					if(a[1]>0&&a[2]>0&&a[3]>0&&a[4]>0&&a[5]>0&&a[6]>0&&a[7]>0&&a[8]>0&&a[9]>0&&a[0]>0)
					{
						printf("Case #%lld: %lld\n",i,r);i++;
						goto sree;
						
					}
				}
				r=m*f;m++;
			}
		}
		i++;
	}
}
