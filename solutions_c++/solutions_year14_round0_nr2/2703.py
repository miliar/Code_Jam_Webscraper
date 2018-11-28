#include<iostream>
#include <cmath>
#include <algorithm>
#include<vector>
#include <string>
#include <set>
#include <sstream>
#include<fstream>
#include<cstdio>
using namespace std;
 int main() {
freopen("B-large.in","r",stdin);
freopen("out234.out","w",stdout);
 long int t, i, test;
	double c, f, x, p, q, out, sec, count, count2;
	scanf("%ld", &t);
	for(test=1; test<=t; test++)
	{
		scanf("%lf %lf %lf", &c, &f, &x);
		sec=2.0;
		p=c/sec;
		q=x/c;
		out=p*q;
		while(1)
		{
			sec+=f;
			count=c/sec;
			count2=count*q;
			if((p+count2) <= out)
			{
				out=p+count2;
				p+=count;
			}
			else
				break;
		}
		printf("Case #%ld: %.7lf\n", test, out);
	}
	return 0;
}
