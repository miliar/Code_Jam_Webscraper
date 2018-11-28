#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<iostream>
using namespace std;

int main()
{
	int r,t,y,T,exp,k=0;
	scanf("%d",&T);
	double x;
	while(T--)
	{
		k++;
		scanf("%d %d",&r,&t);
		x = (pow((double)(4*r*r + 1 - 4*r + 8*t),0.5) - 2*r +1)/((double)4) ;
		y= x;
		
		printf("Case #%d: %d\n",k,y);
	}
	return 0;
}
