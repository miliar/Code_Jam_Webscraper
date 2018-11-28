#include <iostream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
using namespace std;


int cmpFunc (const void *a, const void *b)
{
	return (*(int*)a) < (*(int*)b);
}

int main (void)
{
	int T;
	cin>>T;
	for(int ti=1; ti<=T; ti++)
	{
		int X;
		cin >> X;
		int R, C;
		cin >> R >> C;
		if(X==1)
		{
			cout<<"Case #"<<ti<<": GABRIEL"<<endl;
		}
		else if(X==2)
		{
			if(R*C%X!=0||R*C<X)
			{
				cout<<"Case #"<<ti<<": RICHARD"<<endl;
			}
			else
			{
				cout<<"Case #"<<ti<<": GABRIEL"<<endl;
			}
		}
		else if(X==3)
		{
			if(R*C%X!=0||R*C<=X)
			{
				cout<<"Case #"<<ti<<": RICHARD"<<endl;
			}
			else
			{
				cout<<"Case #"<<ti<<": GABRIEL"<<endl;
			}
		}
		else if(X==4)
		{
			if(R*C==12||R*C==16)
			{
				cout<<"Case #"<<ti<<": GABRIEL"<<endl;
			}
			else
			{
				cout<<"Case #"<<ti<<": RICHARD"<<endl;
			}
		}
	}
	return 0;
}
