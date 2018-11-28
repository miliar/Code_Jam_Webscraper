#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	freopen("hello.txt","r",stdin);
	freopen("Bans2.txt","w",stdout);
	long long int test;	
	cin>>test;
	long long int f=1;
	while(test--)
	{
	long long 	int r,t;
		
		cin>>r>>t;
	long long 	int d=0;
		long long int c=0;
		long long int incre=3;
		long long int i=0;
		while(c<=t)
		{
			
			long long int temp=(r+1+i)*(r+1+i)-(r+i)*(i+r);
			c=c+temp;
			if(c<=t)
			d++;
			i=i+2;
			
		}
		cout<<"Case #"<<f<<": "<<d<<endl;
		f++;
	}
	
	return 0;
}
