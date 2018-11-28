#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream cin;
	ofstream cout;
	cin.open("D-small-attempt0.in");
	cout.open("D-small-output0.txt");
	int t,i;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		int x,r,c;
		cin>>x>>r>>c;
		if(x==1)
		{
			cout<<"Case #"<<i<<": "<<"GABRIEL"<<endl;
			continue;
		}
		else if(x==2)
		{
			if((r==1 && c==1) || (r==1 && c==3) || (r==3 && c==1) || (r==3 && c==3) )
			{
				cout<<"Case #"<<i<<": "<<"RICHARD"<<endl;
				continue;
			}
			else
			{
				cout<<"Case #"<<i<<": "<<"GABRIEL"<<endl;
				continue;
			}
		}
		else if(x==3)
		{
			if((r==2 && c==3) || (r==3 && c==2) || (r==3 && c==3) || (r==3 && c==4) || (r==4 && c==3) )
			{
				cout<<"Case #"<<i<<": "<<"GABRIEL"<<endl;
				continue;
			}
			else
			{
				cout<<"Case #"<<i<<": "<<"RICHARD"<<endl;
				continue;
			}
		}
		else
		{
			if((r==4 && c==3) || (r==3 && c==4) || (r==4 && c==4) )
			{
				cout<<"Case #"<<i<<": "<<"GABRIEL"<<endl;
				continue;
			}
			else
			{
				cout<<"Case #"<<i<<": "<<"RICHARD"<<endl;
				continue;
			}
		}
	}
}
