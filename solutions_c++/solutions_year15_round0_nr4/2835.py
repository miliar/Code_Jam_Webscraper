#include <iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int z=1;z<=t;z++)
	{
		int x,r,c;
		cin>>x>>r>>c;
		cout<<"Case #"<<z<<": ";
		int area;
		area=r*c;
		if(x==1)
			cout<<"GABRIEL\n";
		else if(area%x!=0)
			cout<<"RICHARD\n";
		else if(x>r && x>c)
			cout<<"RICHARD\n";
		else if(x==2)
		{
			cout<<"GABRIEL\n";
		}
		else if(x==3)
		{
			if(area==6||area==9||area==12)
				cout<<"GABRIEL\n";
			else
				cout<<"RICHARD\n";
		}
		else if(x==4)
		{
			if(area==4||area==8)
				cout<<"RICHARD\n";
			else
				cout<<"GABRIEL\n";
		}
	}
	return 0;
}

		
