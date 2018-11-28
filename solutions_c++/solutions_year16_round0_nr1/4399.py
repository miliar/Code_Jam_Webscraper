#include <bits/stdc++.h>
using namespace std;
#define ll long long
bool b[10];
int a[50];
vector <ll> v;
vector <ll> v2;
int main()
{
	ll t,n;
	scanf("%lld",&t);
	ll c=1;
	while(t--)
	{
		scanf("%lld",&n);
		if(n!=0)
		{
			int z=n;
			memset(b,0,sizeof(b));
			while(z>0)
			{
				v.push_back(z%10);
				v2.push_back(z%10);
				z/=10;
			}
			for(int i=0;i<20;i++)
			{
				v2.push_back(0);
			}
			for(int i=0;i<v.size();i++)
			{
				b[v[i]]=true;
			}
			int curr=n;
			while(true)
			{
				bool flag=true;
				for(int i=0;i<10;i++)
				{
					if(b[i]==false)
					{
						flag=false;break;
					}
				}
				if(flag==true)
				{
					break;
				}
				int carry=0,temp;
				for(int i=0;i<v.size();i++)
				{

					temp=(v[i]+v2[i]+carry)/10;
					v[i]=(v[i]+v2[i]+carry)%10;
					b[v[i]]=true;
					carry=temp;
				}
				while(carry>0)
				{
					b[carry%10]=true;
					v.push_back(carry%10);
					carry/=10;
				}
			}
			cout<<"Case #"<<c<<": ";
			for(int i=v.size()-1;i>=0;i--)
			{
				cout<<v[i];
			}
			cout<<endl;
		}
		else
		{
			cout<<"Case #"<<c<<": "<<"INSOMNIA"<<endl;
		}
		
		c++;
		v.clear();
		v2.clear();
	}


}
