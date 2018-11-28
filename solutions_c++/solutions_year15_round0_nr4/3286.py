//I hope this works

#include <iostream>
#include <string>
using namespace std;

int main()
{
	int t;
	
	cin>>t;
	for(int i=0;i<t;i++)
	{
		
		int x;
		int r;
		int c;
		string winner;
		
		cin>>x;
		cin>>r;
		cin>>c;
		
		if((r>1&&c>1&&x>=(r+c))||((r==1||c==1)&&x>=3)||(x>c&&x>r)||(x>=7))
		{
			winner="RICHARD";
			
		}
		else if(x>=4&&2*x==r*c)
		{
			winner="RICHARD";
		}	
		else if((r*c)%x==0)
		{
			
			winner="GABRIEL";
			
		}
		else
		{
			winner="RICHARD";
		}	
		cout<<"Case #"<<i+1<<": "<<winner<<endl;
	}
		return 0;
}		