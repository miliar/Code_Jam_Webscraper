//cca.cpp
//2014-04-12 12:14:41
//ktu

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;
#define eps 1e-7

double f, c, x;
double cost(int n)
{
	int i;
	double sum = 0.0;
	for (i = 0; i < n; i++)
	{
		sum += c/(2.0+i*f);
	}
	sum += x/(2.0+n*f);
	return sum;
}

int main(int argc, char** argv)
{
	int n, i, num;
	cin >> n;
	for (i = 0; i < n; i++)
	{
		cin >> c >> f >> x;
		double th = x/c-2/f-1;
		if (th < eps) num = 0;
		else if (abs(th-round(th))<eps) num = int(round(th));
		else num = int(th)+1;
		printf("Case #%d: %.7f\n",i+1, cost(num));
	}
	return 0;
}
 
