#include <iostream>
#include <stdio.h>
using namespace std;

long int func()
{
	int x,r,c;
	cin>>x>>r>>c;
	if(x==1)
		return 1;
	if(x>=7)
		return 0;
	if( (x==2) && (r*c==x) )
		return 1;
	if( (r*c<=x) || ((r*c)%x) )
		return 0;
	if(x==2)
		return 1;
	if(x==3)
		return !(min(r,c)<=1);
	if(x==4)
		return !(min(r,c)<=2);
	if(x==5)
		return !((max(r,c)<=4)||(min(r,c)<=2));
	if(x==6)
		return !((max(r,c)<=5)||(min(r,c)<=3));
}

int main()
{
	//freopen("1.in","r",stdin);
	//freopen("aout.out","w",stdout);
	long int t;
	string str[2];
	str[0] = "RICHARD";
	str[1] = "GABRIEL";
	cin>>t;
	for(long int i=0;i<t;i++)
	    cout<<"Case #"<<i+1<<": "<<str[func()]<<"\n";
	return 0;
}