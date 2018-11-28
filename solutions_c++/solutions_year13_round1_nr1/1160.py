#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <cmath>
#include <cstring>
using namespace std;
int main()
{
	int T;
	scanf("%d",&T);
	for(int iter=0;iter<T;iter++)
	{
		long long int r,t,sol;
		scanf("%lld%lld",&r,&t);
		long long int j=sqrt(((4*r*r)-(4*r)+(8*t)+1));		
		long long int k=1-2*r;
		sol=(j+k)/4;	  
		printf("Case #%d: %lld\n",iter+1,sol);
	}
}
