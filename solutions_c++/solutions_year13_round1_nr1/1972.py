#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
using namespace std;
main()
{   freopen ("A-small-attempt0.in", "r", stdin);
    freopen ("Q1small.in", "w", stdout);
	long int tc,cases=1;
	cin>>tc;
	while(tc--)
	{   long int count=0;
		long double r,t;
		cin>>r>>t;
		while(t>0)
		{
		   	t-=pow((r+1),2)-pow(r,2);
		   	r+=2;
		   	if(t>=0)
		   	count+=1;
		}
		cout<<"Case #"<<cases<<": ";	
		cout<<count<<"\n"; 
		cases++;
	}
}
