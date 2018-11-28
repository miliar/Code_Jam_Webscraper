#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t,i,j,k;
	double c,f,x,n,t1,t2;
	double ans,r;
	cin>>t;
	while(t--)
	{
		k++;
		cin>>c>>f>>x;
		ans=0.0;r=0.0;
		n=(c)/(r+2.0);
		if((x)/(2.0)<n)
		{
			n=(x)/2.0;
		}
		else
		{
		while(ans<x)
		{
		t1=(x-c)/(r+2.0);
		t2=x/(r+f+2.0);
		if(t1<=t2)
		{
			n=n+(x-c)/(r+2.0);
			break;
		}
		else
		{
			r=r+f;
			n=n+(c)/(r+2.0);
		}
		}
		}
		printf("Case #%d: %0.7lf\n",k,n);
		
	}
	return 0;
}
			
