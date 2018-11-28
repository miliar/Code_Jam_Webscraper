#include <iostream>
#include<iomanip>
using namespace std;
int main() {
	// your code goes here
	double c,f,x,s,y;
	int t,cost=0,i,j;
	cin>>t;
	j=0;
	while(t--)
	{
	s=0;
	//i=2;
	cin>>c>>f>>x;
	y=2.0;
	while(cost<x)
	{
	if((x/y)<((x/(y+f))+(c/y)))
	{
	s=s+(x/y);
	goto x;
	}
	else
	{
	s=s+(c/y);
	y=y+f;
	}
	}
	x:
	cout<<"Case #"<<j<<": "<<fixed<<setprecision(7)<<s<<"\n";
	j++;
	}
	return 0;
}
