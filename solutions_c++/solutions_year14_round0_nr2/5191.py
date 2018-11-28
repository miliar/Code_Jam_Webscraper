#include<iostream>
#include<iomanip>
#include<stdio.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	double c,f,x,r;
	for(int i=0;i<t;i++)
	{
		r=2;
		double prev,curr,temp;
		cin>>c>>f>>x;
		prev=(double)(x/(double)r);
		curr=c/r+x/(r+f);
		temp=c/r;
		while(prev>curr)
		{
			prev=curr;
			r+=f;
			curr=temp+(c/r)+(x/(r+f));
			temp=temp+c/r;
		}
		cout<<"Case #"<<i+1<<": ";
		printf("%.7f\n",prev);
	}
	return 0;
}
