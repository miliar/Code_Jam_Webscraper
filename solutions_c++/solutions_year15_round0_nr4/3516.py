#include<iostream>
#include<cmath>
#include<cstdlib>
using namespace std;
int main()
{
	int t,tc;
	cin>>t;
	for(tc=1;tc<=t;tc++)
	{
		int x,r,c;
		cin>>x;
		cin>>r;
		cin>>c;
		if(x>4)
			cout<<"Case #"<<tc<<": RICHARD\n";
			
		else
		{
			if(x>6)
				cout<<"Case #"<<tc<<": RICHARD\n";
				
			else if(x==1)
				cout<<"Case #"<<tc<<": GABRIEL\n";
			else if(x==2)
			{
				if(r%2==0||c%2==0)
					cout<<"Case #"<<tc<<": GABRIEL\n";
				else
					cout<<"Case #"<<tc<<": RICHARD\n";
			}
			else if(x==3)
			{
				if((r%3==0)&&(c>1))
					cout<<"Case #"<<tc<<": GABRIEL\n";
				else if((c%3==0)&&(r>1))
					cout<<"Case #"<<tc<<": GABRIEL\n";
				else
					cout<<"Case #"<<tc<<": RICHARD\n";		
			}
			else if(x==4)
			{
				if((r==4)&&(c==4))
					
					cout<<"Case #"<<tc<<": GABRIEL\n";
				else if((r==3&&c==4)||(r==4&&c==3))
					cout<<"Case #"<<tc<<": GABRIEL\n";
				else
					cout<<"Case #"<<tc<<": RICHARD\n";					
					
			}
		}		
	}
	return 0;
}