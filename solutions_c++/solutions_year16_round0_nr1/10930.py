#include<iostream>
#include<map>
using namespace std;
typedef long long ll;
map<int,int> mp;
void count(ll n)
{
	ll k;
	while(n)
	{
		k=n%10;
		mp[k]=1;
		n/=10;
	}
}
int main()
{
	int t;
	cin>>t;
	ll n;
	int flag;
	ll m;
	for(int i=0;i<t;i++)
	{
		flag=0;
		mp.clear();
		cin>>n;
		if(n==0)
			;
		else
		{
			for(int j=1;j<=100000;j++)
			{
				m=n*j;
				count(m);
				if(mp.size()==10)
					break;
			}
			if(mp.size()==10)
				flag=1;
		}

		if (flag==0)
			cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		else
			cout<<"Case #"<<i+1<<": "<<m<<endl;


	}
}