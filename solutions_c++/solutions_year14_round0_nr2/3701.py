#include <stdio.h>
#include <iostream>
#include <unistd.h>
using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double r = 2.0;
		double ans = 0.0;
		while(1)
		{
			double a = x/r;
			double b = c/r + x/(r+f);
			// cout<<a<<"\t"<<b<<endl;
			// sleep(5);
			if(a <= b)
			{
				ans = ans + a;
				break;
			}
			else
			{
				ans += c/r;
				r += f;
			}
		}
		printf("Case #%d: %.7lf\n",t,ans);
	}
}