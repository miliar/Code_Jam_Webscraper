#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
int main()
{
	int i ,j , k, n , m, t;
	double a, b, c;
	freopen("B-large.in", "r", stdin);
	freopen("out.txt","w",stdout);
	scanf("%d", &t);
	for (int ii = 0; ii < t; ++ii)
	{
		scanf("%lf%lf%lf", &a, &b, &c);
		double ret = 2;
		double sum = 0;
		for (int i = 1;;++i)
		{
			if (c / ret <= (a / ret + c / ( ret + b )))
			{
				sum += c / ret;
				break;
			}
			sum += a / ret;
			ret += b;
		}
		printf("Case #%d: %.8f\n", ii + 1, sum);
	}
	
}
		
		
			
		
