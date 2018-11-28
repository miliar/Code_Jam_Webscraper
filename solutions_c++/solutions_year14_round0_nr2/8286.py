#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std;


int main()
{
	freopen("B-large.in.txt","r",stdin);
	freopen("B-large.out.txt","w",stdout);
	int cases,i,n;
	double c,f,x,cur;
	cin >> cases;
	for(i = 1; i <= cases; ++i){
		cin >> c >> f >> x;
		n = 0;cur = 0;
		while (x / (n * f + f + 2) < (x - c) / (n * f + 2))
			cur += c / (n++ * f + 2);
		printf("Case #%d: %.7lf\n", i, cur + x / (n * f + 2));
	}
}