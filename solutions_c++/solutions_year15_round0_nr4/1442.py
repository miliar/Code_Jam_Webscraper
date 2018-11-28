#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int T=0;T<t;T++)
	{
		int x,r,c;
		cin>>x>>r>>c;
		int s=1;
		if(r>=3&&c>=3&&x>=7)
		s=0;
		else if((r*c)%x)
		s=0;
		else if(x%2==1)
		{
			int z=x-x/2;
			//if(T==33)cout<<x<<" "<<z<<endl;
			if(r<z||c<z)
			s=0;
		}
		else if(x%2==0)
		{
			//cout<<x<<" "<<r<<" "<<c<<endl;
			if(r<x/2||c<x/2)
			s=0;
			else if(x==4)
			{
				if(r==2||c==2)s=0;
				if(r==3&&c==3)s=0;
			}
			else if(x==6)
			{
				if(r==3||c==3)s=0;
				if(r==4&&c==4)s=0;
			}
		}
		cout<<"Case #"<<T+1<<": ";
		if(s==0)
		cout<<"RICHARD\n";
		else 
		cout<<"GABRIEL\n";
	}
	return 0;
}