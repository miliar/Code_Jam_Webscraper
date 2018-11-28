#include<bits/stdc++.h>
using namespace std;
typedef long long ll;



int main()
{
	ll t;
	cin>>t;
	for(ll tt=1;tt<=t;tt++)
	{
		cout<<"Case #"<<tt<<": ";
		ll n;
		cin>>n;
		if(n==0)
			cout<<"INSOMNIA"<<endl;
		else
		{
			int buf[10]={0};
			ll num=0;
			for(ll i=1;;i++)
			{
				num+=n;
				char temp[20];
				sprintf(temp,"%lld",num);
				for(ll j=0;j<strlen(temp);j++) buf[temp[j]-'0']=1;
				int flag=0;
				for(int j=0;j<10;j++)
				{
					if(buf[j]==1) flag++;
				}
				if(flag==10) break;
			}
			cout<<num<<endl;
		}
	}
	return 0;
}
