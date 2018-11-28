#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,k=0;
	scanf("%d",&t);
	while(t--)
	{
		int ar[10];
		memset(ar,0,sizeof(ar));
 		k++;
		ll n;
		scanf("%lld",&n);
		if(n==0)
			cout<<"Case #"<<k<<": INSOMNIA"<<endl;
		else
		{
			ll n1,n2,temp,flag;
			for(int i=1;;i++)
			{
				flag = 1;
				n1=i*n;
				n2=i*n;
				while(n1)
				{
					temp=n1%10;
					ar[temp]=1;
					n1/=10;
				}
				for(int j=0;j<10;j++)
				{
					if(ar[j]==0)
					{
						flag = 0;
						break;
					}
				}
				if(flag)
					break;
			}
			cout<<"Case #"<<k<<": "<<n2<<endl;
		}
	}
}
