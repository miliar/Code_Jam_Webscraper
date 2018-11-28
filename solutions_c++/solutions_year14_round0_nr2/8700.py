#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;
int main()
{
	int t;
	double c,f,x,curr=2,ans=0;
	cin>>t;/*
	for (int i=0; i<t; i++)
	{
		cin>>c>>f>>x;
		n = ceil((x/c)-(2/f));
		if (x < c) n=0;
		cout<<n<<endl;
		ans=x/(n*f+2);
		while(n>0)
		{
			ans+=c/((n-1)*f+2);
			n--;
		}
		cout<<fixed<<setprecision(7)<<"Case #"<<i+1<<": "<< ans <<endl;
	}*/
	for(int i=0; i<t; i++)
	{
		cin>>c>>f>>x;
		if (x>c)
		{
			ans+=c/curr;
			while((x-c)/curr>c/f)
			{
				curr+=f;
				ans+=c/curr;
			}
			ans+=(x-c)/curr;
		}
		else ans=x/2;
		cout<<fixed<<setprecision(7)<<"Case #"<<i+1<<": "<< ans <<endl;
		ans=0;
		curr=2;
	}
}
