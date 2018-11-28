#include <iostream>
using namespace std;

int main() {
	int t=0,inc =1;
	cin>>t;
	while(t--!=0)
	{
		cout<<"Case #"<<inc++<<": ";
		int x=0,r=0,c=0;
		cin>>x>>r>>c;
		if((r*c)%x!=0)
		cout<<"RICHARD";
		else if(x>2)
		{
			if(r==1 || c==1)
				cout<<"RICHARD";
			else if(x==4 && (r==2 || c==2))
				cout<<"RICHARD";
			else
				cout<<"GABRIEL";
		}
		else
			cout<<"GABRIEL";
		cout<<endl;
	}
	return 0;
}
