#include <cstdio>
#include <iostream>
using namespace std;

int main()
{
	int t, i, k;
	double c, f, x, a, b, m, f1, temp, temp2;
	scanf("%d", &t);
	for(k=1; k<=t; k++)
	{
		scanf("%lf %lf %lf", &c, &f, &x);
		f1=2.0;
		a=c/f1;
		b=x/c;
		m=a*b;
		while(1)
		{
			f1+=f;
			temp=c/f1;
			temp2=temp*b;
			if((a+temp2) <= m)
			{
				m=a+temp2;
				a+=temp;
			}
			else
				break;
		}
		printf("Case #%d: %.7lf\n", k, m);
	}
	return 0;
}
