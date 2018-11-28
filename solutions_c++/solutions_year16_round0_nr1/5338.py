#include<bits/stdc++.h>
using namespace std;
#define ll long long
long long ans[1000005]={0},t,n,c=0;

ll func(ll x,ll mask,ll mul)
{
	if(__builtin_popcount(mask)==10)
		return x-mul;
	
	int temp=x,rem;
	while(temp)
	{
		rem=temp%10;
		mask|=(1<<rem);
		temp/=10;
	}
	return func(x+mul,mask,mul);
}

int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	cin>>t;
	while(t--)
	{
		c++;
		cin>>n;	
		if(n==0)
		{
			cout<<"Case #"<<c<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		if(ans[n])
		{
			cout<<"Case #"<<c<<": "<<ans[n]<<endl;
			continue;	
		}	
		
		ans[n]=func(n,0,n);
		cout<<"Case #"<<c<<": "<<ans[n]<<endl;
	}
	return 0;
}
