#include <iostream>
#include <cstdio>
#include <math.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <climits>
#define MAX(a,b) a>b?a:b;
#define MIN(a,b) a<b?a:b;
typedef long long int lld;
using namespace std;

int main()
{
	double c,x,f,n,time;
	int t,l;
	cin>>t;
	l=0;
	while(t--)
	{
		l++;
		cin>>c>>f>>x;
		n=2;
		time=0;
		while( x/n > ( c/n+ x/(n+f) ) )
		{
			time+=c/n;
			n+=f;
		}
		time+=x/n;
		printf("Case #%d: %.7lf\n",l,time);
	}
	return 0;
}
