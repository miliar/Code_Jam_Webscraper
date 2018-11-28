#include<bits/stdc++.h>
using namespace std;
int main(int argc, char const *argv[])
{
	int t,i,ans,x,r,c;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>x>>r>>c;
		if(x==1)ans=2;
		else if(x==2)
		{
			if(r*c%2==0)
				ans=2;
			else
				ans=1;
		}
		else if(x==3)
		{
			if(r*c == 6 || r*c == 9 || r*c == 12)
				ans=2;
			else
				ans=1;
		}
		else if(x==4)
		{
			if(r*c == 12 || r*c == 16)
				ans=2;
			else
				ans=1;
		}
		cout<<"Case #"<<i<<": "<<(ans==2?"GABRIEL":"RICHARD")<<endl;
	}
	return 0;
}