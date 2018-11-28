#include <bits/stdc++.h>

using namespace std;

// RICHARD n GABRIEL

int main(int argc, char** argv) {
	freopen("inD1.txt","r",stdin);
	freopen("outD.txt","w",stdout);
	
	int cases;
	cin>>cases;
	
	int n=1;
	while(cases--)
	{
		cout<<"Case #"<<n++<<": ";
		int x,r,c;
		cin>>x>>r>>c;
		int maxe = max(r,c);
		int mine = min(r,c);
		if(x==1)
		{
			cout<<"GABRIEL\n";
			continue;
		}
		
		if(x==2)
		{
			if(!((r*c)%2))
			{
				cout<<"GABRIEL\n";
			}
			else
			{
				cout<<"RICHARD\n";
			}
			continue;
		}
		
		if(x==3)
		{
			if(!((r*c)%3) && mine>=2)
			{
				cout<<"GABRIEL\n";
			}
			else
			{
				cout<<"RICHARD\n";
			}
			continue;
		}
		
		if(x==4)
		{
			if(((r*c)%4))
			{
				cout<<"RICHARD\n";
			}
			else
			{
				
				if(mine <= 2)
				{
					cout<<"RICHARD\n";
				}
				else
				{
					cout<<"GABRIEL\n";
				}
			}
		}
		
	}
	return 0;
}

