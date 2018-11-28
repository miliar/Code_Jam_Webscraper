#include<iostream>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<cstdio>
#include<string>

using namespace std;

int main()
{
	double c, f, x, t, a, b, ans;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		cin>>c>>f>>x;
		double a = 2, b=0;
		while(1)
		{
			double y = x/a;
			double z = c/(a) + x/(a+f);
			if(y>z)
			{
				b += c/(a);
				a += f;
			}
			else
			{
				b += y; 
				break;
			}
		}
		//cout<<"Case #"<<k<<": "<<b<<endl;
		printf("Case #%d: %.7lf\n", k, b);
	}


return 0;
}