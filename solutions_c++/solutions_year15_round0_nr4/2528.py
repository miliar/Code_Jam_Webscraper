#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int x,r,c;
		cin>>x>>r>>c;

		if((r*c)%x!=0)
		{
			cout<<"Case #"<<i<<": RICHARD\n";
			continue;
		}
		if(x==4 && min(r,c)<3)
		{
			cout<<"Case #"<<i<<": RICHARD\n";
			continue;
		}
		if(x==3 && min(r,c)<2)
		{
			cout<<"Case #"<<i<<": RICHARD\n";
			continue;
		}
		
		cout<<"Case #"<<i<<": GABRIEL\n";
	}
}
