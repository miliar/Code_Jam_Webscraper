
#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define mod 1000000007
int main()
{
	int t,x,r,c,count=1;
	scanf("%d",&t);
	while(count<=t)
	{
		scanf("%d%d%d",&x,&r,&c);
		if((r*c)%x!=0)
		{
			cout<<"Case #"<<count<<": "<<"RICHARD\n";
		}
		else
		{
			if(x==1)
			{
				cout<<"Case #"<<count<<": "<<"GABRIEL\n";
			}
			else if(x==2)
			{
				cout<<"Case #"<<count<<": "<<"GABRIEL\n";
			}
			else if(x==3)
			{
				if(r==1 && c==3)
				{
					cout<<"Case #"<<count<<": "<<"RICHARD\n";
				}
				else if(r==3 && c==1)
				{
					cout<<"Case #"<<count<<": "<<"RICHARD\n";
				}
				else
				{
					cout<<"Case #"<<count<<": "<<"GABRIEL\n";
				}
			}
			else
			{
				if(r==1 && c==4)
				{
					cout<<"Case #"<<count<<": "<<"RICHARD\n";
				}
				else if(r==4 && c==1)
				{
					cout<<"Case #"<<count<<": "<<"RICHARD\n";
				}
				else if(r==2 && c==2)
				{
					cout<<"Case #"<<count<<": "<<"RICHARD\n";
				}else if(r==2 && c==4)
				{
					cout<<"Case #"<<count<<": "<<"RICHARD\n";
				}
				else if(r==4 && c==2)
				{
					cout<<"Case #"<<count<<": "<<"RICHARD\n";
				}
				else
				{
					cout<<"Case #"<<count<<": "<<"GABRIEL\n";
				}
			}
		}
		count++;
	}
	return 0;
}