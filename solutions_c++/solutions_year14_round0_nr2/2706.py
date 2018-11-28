#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	double c,f,x,div=2.0,res=0;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>c>>f>>x;
		
		while(c/div + x/(div+f) < x/div)
		{
			res+=c/div;
			div+=f;
		}
		res+=x/div;
		cout<<"Case #"<<i<<':'<<" ";
		printf("%.7lf\n",res);
		res=0;
		div=2.0;
	}
	return 0;
}
