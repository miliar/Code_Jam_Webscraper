#include<bits/stdc++.h>
#define LL long long int
using namespace std;

LL gcd(LL a,LL b)
{
	if(a==0)
		return b;
	if(b==0)
		return a;
	if(a>b)
		return gcd(b,a%b);
	else
		return gcd(a,b%a);
}

int main()
{
	LL a[50];
	a[0]=1;
	for(int i=1;i<50;i++)
		a[i]=a[i-1]*2;
	int t;
	cin>>t;
	LL p,q;
	char ch;
	for(int i=1;i<=t;i++)
	{
		cin>>p>>ch>>q;
		LL sam=gcd(p,q);
		p/=sam;
		q/=sam;
		LL d=q;
		for(int j=0;j<50;j++)
		{
			if(a[j]==q)
			{
				sam=-1;
				break;
			}
		}
		if(sam!=-1)
		{
			cout<<"Case #"<<i<<": impossible\n";
		}
		else
		{
			int cnt=0;
			while(p<q)
			{
				q/=2;
				cnt++;
			}
			cout<<"Case #"<<i<<": "<<cnt<<endl;
		}
	}
	return 0;
}
