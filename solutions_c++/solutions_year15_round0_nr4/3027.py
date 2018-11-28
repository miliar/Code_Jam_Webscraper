#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#define s(x) scanf("%d",&x)
using namespace std;

int main()
{
	int t;
	s(t);
	int j,i;
	for(j=1;j<=t;j++)
	{
		int x,r,c;
		s(x);s(r);s(c);
		int m=r*c;
		if(m%x==0 && m>=x*(x-1))
			printf("Case #%d: Gabriel\n",j);
		else
			printf("Case #%d: Richard\n",j);
	}
	return 0;
}
