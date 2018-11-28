#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
ifstream cin("D-small-attempt0.in.txt");
ofstream cout("out.txt");

int main()
{
	int t,x,r,c,caseNum=0;

	cin>>t;
	while (t--)
	{
		caseNum++;
		cout<<"Case #"<<caseNum<<": ";
		cin>>x>>r>>c;
		if (x==1)
		{
			cout<<"GABRIEL";
		}
		else if (x==2)
		{
			if ((r*c)%2!=0)
				cout<<"RICHARD";
			else
				cout<<"GABRIEL";
		}
		else if (x==3)
		{
			if ((r*c)%3!=0)
				cout<<"RICHARD";
			else if (r==1||c==1)
				cout<<"RICHARD";
			else
				cout<<"GABRIEL";
		}
		else if (x==4)
		{
			if ((r*c)%4!=0)
				cout<<"RICHARD";
			else if (r<=2||c<=2)
				cout<<"RICHARD";
			else 
				cout<<"GABRIEL";
		}
		cout<<endl;
	}
	return 0;
}