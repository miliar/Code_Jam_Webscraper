#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

typedef long long int LL;
typedef unsigned long long int ULL;

int main()
{
	int x, r, c, t, tno=0;
	
	cin>>t;
	
	while(t--)
	{
		++tno;
		
		cin>>x>>r>>c;
		
		cout<<"Case #"<<tno<<": ";
		
		if(x == 1)
		{
			cout<<"GABRIEL"<<endl;	
		}
		
		else if(x == 2)
		{
			if(r == 1 && c == 1)cout<<"RICHARD"<<endl;
			else if(r == 1 && c==2)cout<<"GABRIEL"<<endl;
			else if(r == 1 && c == 3)cout<<"RICHARD"<<endl;
			else if(r == 1 && c == 4)cout<<"GABRIEL"<<endl;
			
			if(r == 2 && c == 1)cout<<"GABRIEL"<<endl;
			else if(r == 2 && c==2)cout<<"GABRIEL"<<endl;
			else if(r == 2 && c == 3)cout<<"GABRIEL"<<endl;
			else if(r == 2 && c == 4)cout<<"GABRIEL"<<endl;
			
			if(r == 3 && c == 1)cout<<"RICHARD"<<endl;
			else if(r == 3 && c==2)cout<<"GABRIEL"<<endl;
			else if(r == 3 && c == 3)cout<<"RICHARD"<<endl;
			else if(r == 3 && c == 4)cout<<"GABRIEL"<<endl;
			
			if(r == 4 && c == 1)cout<<"GABRIEL"<<endl;
			else if(r == 4 && c==2)cout<<"GABRIEL"<<endl;
			else if(r == 4 && c == 3)cout<<"GABRIEL"<<endl;
			else if(r == 4 && c == 4)cout<<"GABRIEL"<<endl;
		}
		
		else if(x == 3)
		{
			if(r == 1 && c == 1)cout<<"RICHARD"<<endl;
			else if(r == 1 && c==2)cout<<"RICHARD"<<endl;
			else if(r == 1 && c == 3)cout<<"RICHARD"<<endl;
			else if(r == 1 && c == 4)cout<<"RICHARD"<<endl;
			
			if(r == 2 && c == 1)cout<<"RICHARD"<<endl;
			else if(r == 2 && c==2)cout<<"RICHARD"<<endl;
			else if(r == 2 && c == 3)cout<<"GABRIEL"<<endl;
			else if(r == 2 && c == 4)cout<<"RICHARD"<<endl;
			
			if(r == 3 && c == 1)cout<<"RICHARD"<<endl;
			else if(r == 3 && c==2)cout<<"GABRIEL"<<endl;
			else if(r == 3 && c == 3)cout<<"GABRIEL"<<endl;
			else if(r == 3 && c == 4)cout<<"GABRIEL"<<endl;
			
			if(r == 4 && c == 1)cout<<"RICHARD"<<endl;
			else if(r == 4 && c==2)cout<<"RICHARD"<<endl;
			else if(r == 4 && c == 3)cout<<"GABRIEL"<<endl;
			else if(r == 4 && c == 4)cout<<"RICHARD"<<endl;
		}
		
		else if(x == 4)
		{
			if(r == 1 && c == 1)cout<<"RICHARD"<<endl;
			else if(r == 1 && c==2)cout<<"RICHARD"<<endl;
			else if(r == 1 && c == 3)cout<<"RICHARD"<<endl;
			else if(r == 1 && c == 4)cout<<"RICHARD"<<endl;
			
			if(r == 2 && c == 1)cout<<"RICHARD"<<endl;
			else if(r == 2 && c==2)cout<<"RICHARD"<<endl;
			else if(r == 2 && c == 3)cout<<"RICHARD"<<endl;
			else if(r == 2 && c == 4)cout<<"RICHARD"<<endl;
			
			if(r == 3 && c == 1)cout<<"RICHARD"<<endl;
			else if(r == 3 && c==2)cout<<"RICHARD"<<endl;
			else if(r == 3 && c == 3)cout<<"RICHARD"<<endl;
			else if(r == 3 && c == 4)cout<<"GABRIEL"<<endl;
			
			if(r == 4 && c == 1)cout<<"RICHARD"<<endl;
			else if(r == 4 && c==2)cout<<"RICHARD"<<endl;
			else if(r == 4 && c == 3)cout<<"GABRIEL"<<endl;
			else if(r == 4 && c == 4)cout<<"GABRIEL"<<endl;
		}
	}
	return 0;
}
