#include<bits/stdc++.h>
using namespace std;
 
typedef long long int lli;
   
#define pc(x) putchar_unlocked(x);
#define gc() getchar_unlocked();
#define F(i, n) for(i = 0;i < n; ++i)
#define M 1000003

#define MAX 210
#define MAXN 200010

lli mint(lli a,lli b)
{
	if(a<b)
	return a;
	else return b;
}

int main(){
lli q=1,t;
cin>>t;
while(t--)
{int x,r,c;
cin>>x>>r>>c;
int b,a=r*c;
if(x==1)
cout<<"Case #"<<q<<": GABRIEL"<<"\n";
else if(x==2)
{
	if(a%2==0)
	cout<<"Case #"<<q<<": GABRIEL"<<"\n";
	else cout<<"Case #"<<q<<": RICHARD"<<"\n";
}
else if(x==3)
{
	if(a%3!=0)
	cout<<"Case #"<<q<<": RICHARD"<<"\n";
	else
	{
	
		if(r==3)
		{
			b=r;
			r=c;
			c=b;}
			if(r==1)
			cout<<"Case #"<<q<<": RICHARD"<<"\n";
			else cout<<"Case #"<<q<<": GABRIEL"<<"\n"; }}
else 
{if(a%4!=0)
	cout<<"Case #"<<q<<": RICHARD"<<"\n";
	else
	{
		if(r==2&&c==2)
		cout<<"Case #"<<q<<": RICHARD"<<"\n";
		else
		{
			if(r==4)
		{
			b=r;
			r=c;
			c=b;}
			if(r==1||r==2)
				cout<<"Case #"<<q<<": RICHARD"<<"\n";
				else cout<<"Case #"<<q<<": GABRIEL"<<"\n";
			}}

	
}
	
q++;}
    return 0;
}
