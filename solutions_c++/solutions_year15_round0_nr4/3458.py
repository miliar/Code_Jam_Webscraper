#include<iostream>
using namespace std;
int main()
{
	int t=0,j=1;
	cin>>t;
	int x=0,r=0,c=0;
	
	for(j=1; j<=t; j++)
	{
		cin>>x>>r>>c;
		int total=0;
		total=r*c;
	
		if(total%x==0)
		{
			if(x-1>r||x-1>c)
			{
				cout<<"Case #"<<j<<": RICHARD"<<endl;
				
			}
			else{
				cout<<"Case #"<<j<<": GABRIEL"<<endl;
			
			}
		}
		else{
			cout<<"Case #"<<j<<": RICHARD"<<endl;
			
		}
	}
	return 0;
}