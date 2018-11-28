#include<iostream>
#include<cmath>

using namespace std;

typedef long long ll;

int palindrome(ll no)
{
	ll rev=0,temp=no;
	while(temp!=0)
	{
		int r=temp%10;
		rev=rev*10+r;
		temp/=10;
	}
	if(rev==no)
		return 1;
	return 0;
}

int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int count=0;
		ll a,b;
		cin>>a>>b;
		for(a;a<=b;a++)
		{
			int r=a%10;
			if(r!=1 && r!=4 && r!=5 && r!=6 && r!=9)
				continue;
			if(!palindrome(a))
				continue;
			ll x=sqrt(long double(a));
			if(a==x*x && palindrome(x))
				count++;
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	return 0;
}