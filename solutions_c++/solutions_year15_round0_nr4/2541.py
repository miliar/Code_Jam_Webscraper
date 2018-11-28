#include <iostream>
#include <cstdio>
using namespace std;


int main()
{
	int t,t1,x,r,c;
	freopen("sol.txt", "w", stdout);
	freopen("test.txt", "r", stdin);
	cin>>t;
	t1  = t;
	while(t--)
	{
		cin>>x>>r>>c;
		if((x < 3) && ((r*c) % x == 0))
		{
			cout<<"Case #"<<t1-t<<": "<<"GABRIEL"<<endl;
			continue;
		}
		if((r*c) % x != 0)
		{
			cout<<"Case #"<<t1-t<<": "<<"RICHARD"<<endl;
			continue;
		}
		else
		{
			if(x == 3)
			{
				if((c==2 && r==3) || (c==3 && r==2) || (c==3 && r==3) || (c==3 && r==4) || (c==4 && r==3))
				{
					cout<<"Case #"<<t1-t<<": "<<"GABRIEL"<<endl;
					continue;
				}
				else
				{
					cout<<"Case #"<<t1-t<<": "<<"RICHARD"<<endl;
					continue;
				}
			}
			if(x == 4)
			{
				if((c==3 && r==4) || (c==4 && r==3) || (c==4 && r==4))
				{
					cout<<"Case #"<<t1-t<<": "<<"GABRIEL"<<endl;
					continue;
				}
				else
				{
					cout<<"Case #"<<t1-t<<": "<<"RICHARD"<<endl;
					continue;
				}
			}
		}
	}
	return 0;
}
