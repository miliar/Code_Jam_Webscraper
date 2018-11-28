#include<iostream>
using namespace std;
int main()
{
	int t=0,j=1;
	cin>>t;
	int x=0,r=0,c=0;
	while(t--)
	{
		cin>>x>>r>>c;
		int total=0,formation=x-1;
		total=r*c;

		if(total%x==0)
		{
			if(formation>r||formation>c)
			{
				cout<<"Case #"<<j<<": RICHARD"<<endl;
			j++;
			}
			else{
				cout<<"Case #"<<j<<": GABRIEL"<<endl;
			j++;
			}
		}
		else{
			cout<<"Case #"<<j<<": RICHARD"<<endl;
			j++;
		}
	}
	return 0;
}
