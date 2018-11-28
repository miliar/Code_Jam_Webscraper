//============================================================================
// Name        : gcj.cpp
// Author      : 
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int not_filled(int b[])
{
	for(int i=0;i<10;i++)
		if(b[i]==0)
			return 1;
	return 0;
}


int main()
{
	int t;
	cin>>t;
	int test=0;
	while(test++<t)
	{
		int n,n1,tn,d,c,i;
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<test<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		int b[10];
		for(i=0;i<10;i++)
			b[i]=0;

		c=1;
		while(not_filled(b))
		{
			n1=n*c;
			tn=n1;//temporary no. for extracting digits

			while(tn)
			{
				d=tn%10;
				b[d]=1;
				tn=tn/10;
			}
			c++;
		}
		cout<<"Case #"<<test<<": "<<n1<<endl;

	}
	return 0;
}
