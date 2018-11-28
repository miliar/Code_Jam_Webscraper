#include<iostream>
#include<cstdlib>
#include<cstdio>//old c library
#include<cmath>//ceil,floor,round,M_PI,,trig,pow(ambigous)
#include<cstring>
#include<iomanip>//set precisions
#include <algorithm>//using swap
#include<fstream>//used to manipulate files.
//#include <boost/multiprecision/cpp_int.hpp>//algerbric operations on string
//namespace mp=boost::multiprecision;
using namespace std;
int main()
{
	freopen("test.in","r",stdin);
	freopen("test.txt","w",stdout);
	int t,x,r,c;
	cin>>t;
	for(int y=1;y<=t;y++)
	{
		cin>>x>>r>>c;
		int total=(r*c);
		if(x==1)
		{
		cout<<"Case #"<<y<<": GABRIEL"<<endl;
		}
		
		if(x==2 && total%2!=0)
		cout<<"Case #"<<y<<": RICHARD"<<endl;
		else if(x==2 && total%2==0)
		cout<<"Case #"<<y<<": GABRIEL"<<endl;
		
		if(x==3)
		{
			if(r==1 || c==1)
			cout<<"Case #"<<y<<": RICHARD"<<endl;
			else if(r==2 || c==2)
			{
			if(total==6)
			cout<<"Case #"<<y<<": GABRIEL"<<endl;
			else
			cout<<"Case #"<<y<<": RICHARD"<<endl;	
			}
			else if(r==3 || c==3)
			{
				if(total==9 || total==12)
				cout<<"Case #"<<y<<": GABRIEL"<<endl;
			}
			else if(r==4 || c==4)
			{
				cout<<"Case #"<<y<<": RICHARD"<<endl;
				}
			}
		
		 if(x==4)
		 {
			if(r==1 || c==1)
			{
				
			cout<<"Case #"<<y<<": RICHARD"<<endl;
			}
			else if(r==2 || c==2)
			{
				cout<<"Case #"<<y<<": RICHARD"<<endl;
			}
			else if(r==3 || c==3)
			{
				if(total==9)
				{
				cout<<"Case #"<<y<<": RICHARD"<<endl;
				}
				else
				{
				cout<<"Case #"<<y<<": GABRIEL"<<endl;
				}			
			}
			else if(r==4 || c==4)
			{
				cout<<"Case #"<<y<<": GABRIEL"<<endl;
				
				}
			 }
		
		}
	
		
		
	return 0;
}
