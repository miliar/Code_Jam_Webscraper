#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	freopen("infile.in","r",stdin);
	freopen("outfile.txt", "w", stdout);
	
	int t;
	int s;
	s = 1;
	cin>>t;
	while(t--)
	{
		double a,b,c,temp,rate;
		double x[1000];
		cin>>a;
		cin>>b;
		cin>>c;
		temp = 0.0;
		rate = 2.0;
		x[0] = 0;
		for(int i = 1; i < 1000; i++)
		{
			x[i] = c/rate + temp;
			if(i != 1)
			{
				if(x[i]>x[i-1])
				{
					printf("Case #%d: %.7f\n", s, x[i-1]);
					break;
				}
			}
			temp = temp + a/rate;
			rate = rate + b;
			
		}
		s++;
		
	}
	return 0;
}
