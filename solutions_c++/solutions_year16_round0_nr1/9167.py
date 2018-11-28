#include<bits/stdc++.h>
#define ll  long long int
using namespace std;
int check(int a[])
{
	int flag=1;
	for(int i=0;i<10;i++)
	{
		if(a[i]==0)
		{
			flag=0;
			break;
		}
	}
	if(flag==1)
	return 1;
	else
	return 0;
}
int main (void)
{
	freopen("A-large.in","r",stdin);
	freopen("out2.out","w",stdout);
	int t;
	cin>>t;
	for(int x=1;x<=t;x++)
	{
		ll n,sol;
		cin>>n;
		int a[10];
		for(int k=0;k<10;k++)
		a[k]=0;
		ll i;
		if(n==0)
		cout<<"Case #"<<x<<": INSOMNIA"<<endl;
		else
		{
			i=1;
			while(check(a)!=1)
			{
				ll curr=i*n;
				sol=curr;
				while(curr>0)
				{
					ll d=curr%10;
					a[d]=1;
					curr=curr/10;
				}
				i++;
			}
			cout<<"Case #"<<x<<": "<<sol<<endl;
		}
		
	}
}

