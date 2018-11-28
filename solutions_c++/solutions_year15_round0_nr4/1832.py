#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		int x,r,c;
		cin>>x;
		cin>>r;
		cin>>c;
		int s=r*c;
		if(x==1)
		{
			cout<<"Case #"<<k<<": "<<"GABRIEL"<<endl;
		}
		else if(x==2&&s%2==0)
		{
			cout<<"Case #"<<k<<": "<<"GABRIEL"<<endl;
		}
		else if(x==3&&(s==6||s==9||s==12))
		{
			cout<<"Case #"<<k<<": "<<"GABRIEL"<<endl;
		}
		else if(x==4&&(s==12||s==16))
		{
			cout<<"Case #"<<k<<": "<<"GABRIEL"<<endl;
		}
		else
			cout<<"Case #"<<k<<": "<<"RICHARD"<<endl;
		
			
	}
	return 0;
}
