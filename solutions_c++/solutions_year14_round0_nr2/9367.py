#include<iostream>
#include<stdio.h>
using namespace std;
int main(int argc, char const *argv[])
{
	int n;
	cin>>n;
	for (int m = 0; m < n; ++m)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double res=100000.0;
		for (int i = 0; i < 2000; ++i)
		{
			double aux=0;
			for (int j = 0; j < i; ++j)
			{
				aux+=c/(2+j*f);
			}
			aux+=x/(2+f*i);
			if(res>aux) res=aux;
		}
		printf("Case #%d: %.7lf\n",m+1,res);
	}
	return 0;
}