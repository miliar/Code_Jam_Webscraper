#include<iostream>
using namespace std;
int main()
{
	int T;
	cin>>T;
	for(int k=1;k<=T;k++)
	{
		int x, r, c, flag=0;
		cin>>x>>r>>c;
		if(x==1)
		{
			cout<<"Case #"<<k<<": GABRIEL"<<endl;
		}
		else if(x==2)
		{
			if((r*c)%2==0)
			{
				cout<<"Case #"<<k<<": GABRIEL"<<endl;
			}
			else
			{
				cout<<"Case #"<<k<<": RICHARD"<<endl;
			}
		}
		else if(x==3)
		{
			if((r*c)==6 || (r*c)==9 || (r*c)==12)
			{
				cout<<"Case #"<<k<<": GABRIEL\n";
			}
			else
			{
				cout<<"Case #"<<k<<": RICHARD\n";
			}
		}
		else if(x==4)
		{
			if((r*c)==12 || (r*c)==16)
			{
				cout<<"Case #"<<k<<": GABRIEL\n";
			}
			else
			{
				cout<<"Case #"<<k<<": RICHARD\n";
			}
		}
	}
}
