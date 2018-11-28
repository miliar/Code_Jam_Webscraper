#include<bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define mod 1000000007
#define bitcount __builtin_popcountll
#define ll long long
int arr[10];
int main()
{
	int i,j,k;
	int t,n;
	freopen("A-large.in","r",stdin);
	freopen("outputi.txt","w",stdout);
	sd(t);
	for(i=1;i<=t;i++)
	{
		for(j=0;j<=9;j++)
			arr[j]=0;
		sd(n);
		if(n==0)
			printf("Case #%d: INSOMNIA\n",i);
		else
		{
			k=1;
			do
			{
				j=k*n;
				while(j!=0)
				{
					arr[j%10]=1;
					j/=10;
				}
				for(j=0;j<=9;j++)
				{
					if(arr[j]==0)
						break;
				}
				if(j==10)
					break;
				k++;
			}while(true);
			printf("Case #%d: %d\n",i, k*n);
		}
	}
	return 0;
}