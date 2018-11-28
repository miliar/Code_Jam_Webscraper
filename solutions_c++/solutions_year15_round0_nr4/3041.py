#include <bits/stdc++.h>
using namespace std;

int main() {
	int a,t,b,d,e,x,r,c;
	freopen("input4.txt","r",stdin);
	freopen("output4.txt","w",stdout);
	cin>>t;
	for(a=1;a<=t;a++)
	{
		cin>>x>>r>>c;
		if(x==1)
		b=0;
		if(x==2)
		{
			if((r*c)%x==0)
			b=0;
			else
			b=1;
		}
		if(x==3)
		{
			if(r==1)
			b=1;
			if(r==2)
			{
				if(c==3)
				b=0;
				else
				b=1;
			}
			if(r==3)
			{
				if(c==1)
				b=1;
				else
				b=0;
			}
			if(r==4)
			{
				if(c==3)
				b=0;
				else
				b=1;
			}
		}
		if(x==4)
		{
			if(r*c==12 || r*c==16)
			b=0;
			else
			b=1;
		}
		if(b==0)
		cout<<"Case #"<<a<<": GABRIEL"<<endl;
		else
		cout<<"Case #"<<a<<": RICHARD"<<endl;

	}
	return 0;
}
