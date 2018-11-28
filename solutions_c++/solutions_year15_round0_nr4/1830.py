#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		cout<<"Case #"<<k<<": ";
		int x,r,c;
		cin>>x>>r>>c;
		if(x==1)
		{
			cout<<"GABRIEL\n";
			continue;
		}
		if(x==2&&(r%2==0||c%2==0))
		{
			cout<<"GABRIEL\n";
			continue;
		}
		if(x==3)
		{
			if((r==2&&c==3)||(r==3&&c==2)||(r==3&&c==4)||(r==4&&c==3)||(r==3&&c==3))
			{
				cout<<"GABRIEL\n";
				continue;
			}
		}
		if(x==4)
		{
			if((r==4&&c==4)||(r==3&&c==4)||(r==4&&c==3))
			{
				cout<<"GABRIEL\n";
				continue;
			}
		}
		cout<<"RICHARD\n";
	}
	return 0;
}
