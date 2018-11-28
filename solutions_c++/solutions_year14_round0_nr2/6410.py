#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	double s_pre=0,s=0,s_next=0,c,f,x,k=2;
	long t,count=0;
	cin>>t;
	while(t-->0)
	{	count++;
		cin>>c>>f>>x;
		s_pre=x/2;
		k=2;
		
		while(1)
		{
			s=s_pre-x/k+c/k;
			k=k+f;
			s=s+x/k;
			if(s>s_pre)
			break;
			else
			s_pre=s;
		}
		printf("case #%d: %.7f\n",count,s_pre);
		
	}
	return 0;
} 
