#include <bits/stdc++.h>

using namespace std;

long long ar[100000];

int main()
{
	long long a,b,c,i,j,n,t,T,mx,ans=0;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>T;
	for(t=0;t<T;t++)
	{
		cin>>a>>b>>c;
		if((b*c)%a)
		{
			cout<<"Case #"<<t+1<<": RICHARD\n";
			continue;
		}
		if(a==1)
		{
			cout<<"Case #"<<t+1<<": GABRIEL\n";
			continue;
		}
		if(a==2)
		{
			if(max(b,c)>=2)
			{
				if((b*c)%2 == 0)
				cout<<"Case #"<<t+1<<": GABRIEL\n";
				continue;
			}
		}	
		if(a==3)
		{
			if(b==3 || c==3)
			{
				if(min(b,c)!=1)
				{
					cout<<"Case #"<<t+1<<": GABRIEL\n";
					continue;
				}
			}
		}
		if(a==4)
		{
			if(max(b,c)==4 && min(b,c)>=3)
			{	
				cout<<"Case #"<<t+1<<": GABRIEL\n";
				continue;
			}
		}
		cout<<"Case #"<<t+1<<": RICHARD\n";
	}
	return 0;
}
