#include <string>
#include <iostream>
using namespace std;
int main()
{

	int n;
	cin>>n;
	for(int y=0;y<n;y++)
	{
		cout<<"Case #"<<y+1<<": ";
		int x,r,c;
		cin>>x>>r>>c;
		if(x==1)
			cout<<"GABRIEL"<<endl;
		else if(x==2)
		{
			if(r*c%2==0)
				cout<<"GABRIEL"<<endl;
			else
				cout<<"RICHARD"<<endl;
		}
		else if(x==3)
		{
			if(r<3&&c<3)
				cout<<"RICHARD"<<endl;
			else if(r==1||c==1)
				cout<<"RICHARD"<<endl;
			else if(r*c%3==0)
				cout<<"GABRIEL"<<endl;
			else
				cout<<"RICHARD"<<endl;
		}
		else
		{
			if(r<3||c<3)
				cout<<"RICHARD"<<endl;
			else if(r*c%4==0)
				cout<<"GABRIEL"<<endl;
			else
				cout<<"RICHARD"<<endl;
		}
	}
	return 0;
}