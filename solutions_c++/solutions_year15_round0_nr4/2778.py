#include<iostream>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int x,r,c;
		cin>>x>>r>>c;
		if(x==1)
		cout<<"\nCase #"<<i<<": GABRIEL";
		else if(x==2)
		{
			if((r*c)%2==0)
				cout<<"\nCase #"<<i<<": GABRIEL";
			else
				cout<<"\nCase #"<<i<<": RICHARD";
				
		}
		else if(x==3)
		{
			if((r*c)%3==0)
				{	
					if(r==1||c==1)
					cout<<"\nCase #"<<i<<": RICHARD";
					else
				cout<<"\nCase #"<<i<<": GABRIEL";
			}
			else
				cout<<"\nCase #"<<i<<": RICHARD";
		}
		else if(x==4)
		{
			if((r*c)%4!=0)
				{	
				cout<<"\nCase #"<<i<<": RICHARD";
				}
			else
				{
					if(r==1||c==1 || r==2||c==2)
					cout<<"\nCase #"<<i<<": RICHARD";
					else
					cout<<"\nCase #"<<i<<": GABRIEL";
				
				}	
		}
	}
}
