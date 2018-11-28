#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
	int t,y,r,c,dan;
	cin>>t;
	dan=1;
	while(dan<=t)
	{
		int abcd=0;
		cin>>y>>r>>c;
		if((r*c)%y!=0)abcd=1;
		if(y>r && y>c)abcd=1;
		if(y==3 && r*c==3)abcd=1;
		if(y==4 && (r*c==8 || r*c==4))abcd=1;
		cout<<"Case #"<<dan<<": ";
		if(abcd==1)cout<<"RICHARD"<<endl;
		else cout<<"GABRIEL"<<endl;
		dan++;
	}
	return 0;
}