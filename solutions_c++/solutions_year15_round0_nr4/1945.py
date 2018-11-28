#include <iostream>
using namespace std;

int main()
{

	long t = 0;
	
	cin>>t;
	
	for(int ti = 0; ti < t; ti++)
	{
		int x,r,c;
		
		cin>>x>>r>>c;
		
		int winner=0;
		int prod = r*c;
		if(x==1)
		{
			winner=1;
		}
		else if(x==2)
		{
			if(prod%2==0)
			{
				winner=1;
			}
		}
		else if(x==3)
		{
			if(prod>3 && prod % 3==0)
			{
				winner=1;
				
			}
		}
		else {
			if(prod == 12 || prod == 16)
			{
				winner=1;
			}
		}
//		cout<<x<<" "<<r<<" "<<c<<" ";
		cout<<"Case #"<<(ti+1)<<": ";
		if(winner == 0)
		{
			cout<<"RICHARD"<<endl;
		}
		else 
		{
			cout<<"GABRIEL"<<endl;
		}
		
	}
	return 0;	
}
