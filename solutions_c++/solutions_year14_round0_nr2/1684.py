#include <iostream>
#include <fstream>
#include <stdio.h> 


using namespace std;

int main()
{
	int t;
	int i,j,k;
	double ans,c,f,x,p;
	double tmp1,tmp2,tmp3;
	FILE *f2 = fopen("output2.txt","w");
	ifstream f1("B-large.in");
	f1>>t;
	for (i = 0; i < t; i++)
	{
		f1>>c>>f>>x;
		ans = 0;
		p = 2;
		while (true)
		{
			tmp1 = x / p;
			tmp2 = c / p + x / (p + f);
			tmp3 = c / p + c / (p + f) + x / (p + f + f);
			if (tmp3 < tmp2)
			{
				ans += c / p;
				p += f;
			}
			else if (tmp1 < tmp2)
			{
				ans += tmp1;
				break;
			}
			else
			{
				ans += c / p;
				p = p + f;
			}
		}
		fprintf(f2,"Case #%d: %.7lf\n",i+1,ans);
	}
	
	
}
