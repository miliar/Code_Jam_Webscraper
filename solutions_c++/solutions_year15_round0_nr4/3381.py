#include <iostream>
#include<cmath>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int i=1; i<=t; i++)
	{
		int x,r,c;
		cin>>x>>r>>c;
		if( (r*c)%x !=0)
		cout<<"Case #"<<i<<": RICHARD\n";
		else
		{
			if( log2(x) > min(r,c) || x> max(r,c))
			{	
				cout<<"Case #"<<i<<": RICHARD\n";
			}
			else
				if(x==4 && r*c==8)
					cout<<"Case #"<<i<<": RICHARD\n";
				else
				cout<<"Case #"<<i<<": GABRIEL\n";
		}
	}
	return 0;
}