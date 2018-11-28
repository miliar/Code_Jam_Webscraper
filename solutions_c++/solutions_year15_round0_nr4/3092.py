#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#define lli long long int
#define gc getchar

using namespace std;

void scan(lli &x)
{
    register lli c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output1.txt","w",stdout);
	lli flag=0,x,r,c,t;
	scan(t);
	for(lli z=1;z<=t;z++)
	{
		flag=0;
		cin>>x>>r>>c;
		if(x==1)
		{
			flag=1;
			goto end;
		}
		else if(x==2)
		{
			if(r==1 && c==2)
			flag=1;
			if(r==1 && c==4)
			flag=1;
			if(r==2)
			flag=1;
			if(r==3 && c==2)
			flag=1;
			if(r==3 && c==4)
			flag=1;
			if(r==4)
			flag=1;
		}
		else if(x==3)
		{
			if(r==2 && c==3)
			flag=1;
			if(r==3 && c==2)
			flag=1;
			if(r==3 && c==4)
			flag=1;
			if(r==4 && c==3)
			flag=1;
			if(r==3 && c==3)
			flag=1;
			
		}
		else if(x==4)
		{
			if(r==4 && c==3)
			flag=1;
			if(r==3 && c==4)
			flag=1;
			if(r==4 && c==4)
			flag=1;
		}
		end:
		if(flag==1)
		cout<<"Case #"<<z<<": GABRIEL"<<endl;
		else
		cout<<"Case #"<<z<<": RICHARD"<<endl;
	}
	return 0;
}
