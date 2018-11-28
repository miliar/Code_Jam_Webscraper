#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
int main()
{
	int tc;
	cin>>tc;
	for(int t=1;t<=tc;t++)
	{
		int x,r,c;
		cin>>x>>r>>c;
		if(r*c%x!=0)
		{
			cout<<"Case #"<<t<<": RICHARD\n";
		}
		else
		{
			if(x==1||x==2)
			{
				cout<<"Case #"<<t<<": GABRIEL\n";		
			}
			if(x==3)
			{
				if(r==1||c==1)
				{
					cout<<"Case #"<<t<<": RICHARD\n";			
				}
				else
				{
					cout<<"Case #"<<t<<": GABRIEL\n";		
				}
			}
			if(x==4)
			{
				if(r==1||c==1||r==2||c==2)
				{
					cout<<"Case #"<<t<<": RICHARD\n";
				}
				else
				{
					cout<<"Case #"<<t<<": GABRIEL\n";	
				}
			}
		}
	}
	return 0;
}
