#include<iostream>
using namespace std;

int main()
{
	int t,pos=1,x,r,c;
 	cin>>t;
	while(t--)
	{

		cin>>x>>r>>c;
		if((r*c)%x)
		{
			cout<<"Case #"<<pos<<": RICHARD\n";
		}
		else
		{
			if(x<=2)
			{
				cout<<"Case #"<<pos<<": GABRIEL\n";
			}
			else if(x==3)
			{
				if((r*c)==3)
				{
					cout<<"Case #"<<pos<<": RICHARD\n";
				}
				else
				{
					cout<<"Case #"<<pos<<": GABRIEL\n";
				}
			}
			else if((r*c)==4 )
			{
				cout<<"Case #"<<pos<<": RICHARD\n";
			}
			else if((r*c)==8 )
			{
				cout<<"Case #"<<pos<<": RICHARD\n";
			}
			else if((r*c)==12)
			{
				cout<<"Case #"<<pos<<": GABRIEL\n";
			}
			else if((r*c)==16)
			{
				cout<<"Case #"<<pos<<": GABRIEL\n";
			}
		}
		pos++;
	}
	return 0;
}
