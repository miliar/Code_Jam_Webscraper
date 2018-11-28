#include<iostream>
using namespace std;
int main()
{	freopen("D-small-attempt2.in","r",stdin);
	freopen("final.txt","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int x,r,c;
		cin>>x>>r>>c;
		int m=r*c,mn,mx;
		mn=min(r,c);
		mx=max(r,c);
		if(x==1)
		{
			cout<<"Case #"<<i<<": GABRIEL\n";
			continue;
		}
		if(m%x!=0)
		{
			cout<<"Case #"<<i<<": RICHARD\n";
		}
		else
		{
			if(r==c)
			{
				if(x<=r)
				cout<<"Case #"<<i<<": GABRIEL\n";
				else cout<<"Case #"<<i<<": RICHARD\n";
	
			}
			else if(x==r)
			{
				if(x<c)
				{
					cout<<"Case #"<<i<<": GABRIEL\n";
				}
				else 
				{
					if(abs(x-c)==1)
					cout<<"Case #"<<i<<": GABRIEL\n";
					else
					cout<<"Case #"<<i<<": RICHARD\n";
				}
				
				
				
			}
			else if(x==c)
			{
				if(x<r)
				cout<<"Case #"<<i<<": GABRIEL\n";
				else
				{
					if(abs(x-r)==1)
					cout<<"Case #"<<i<<": GABRIEL\n";
					else
					cout<<"Case #"<<i<<": RICHARD\n";
				}
				
			}
			else if(x>mn&&x<mx)
			{
				cout<<"Case #"<<i<<": GABRIEL\n";
			}
			else if(x>mx)
			cout<<"Case #"<<i<<": RICHARD\n";
			else if(x<mn)
			cout<<"Case #"<<i<<": GABRIEL\n";
		}
	}
	return 0;
}