#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int x,r,c;
		cin>>x>>r>>c;
		if(x>=7 || (r*c)%x!=0 || x/2>=min(r,c))
		{
			if((r*c)%x==0 && x<=2)
				cout<<"Case #"<<i<<": GABRIEL"<<endl;
			else
				cout<<"Case #"<<i<<": RICHARD"<<endl;
		}
		else
			cout<<"Case #"<<i<<": GABRIEL"<<endl;
	}
	return 0;
}
