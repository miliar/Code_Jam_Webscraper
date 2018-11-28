#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,x,n,m,j=0;
	cin>>t;
	while(t--)
	{	j++;
		cin>>x>>n>>m;
		if(x>max(n,m))
		{
			cout<<"Case #"<<j<<": "<<"RICHARD\n";
		}
		else
		{
			if(x==1)	cout<<"Case #"<<j<<": "<<"GABRIEL\n";
			if(x==2)
			{
				if((n*m)%2==0)
					cout<<"Case #"<<j<<": "<<"GABRIEL\n";
				else
					cout<<"Case #"<<j<<": "<<"RICHARD\n";
			}
			if(x==3)
			{
				if(min(n,m)==1)
					cout<<"Case #"<<j<<": "<<"RICHARD\n";
				else if((n*m)%3!=0)
					cout<<"Case #"<<j<<": "<<"RICHARD\n";
				else
					cout<<"Case #"<<j<<": "<<"GABRIEL\n";

			}
			if(x==4)
			{
				if((n*m)%4!=0)
					cout<<"Case #"<<j<<": "<<"RICHARD\n";
				else if(min(n,m)<=2)
					cout<<"Case #"<<j<<": "<<"RICHARD\n";
				else
					cout<<"Case #"<<j<<": "<<"GABRIEL\n";
			}
		}
	}
	return 0;
}