#include <stdio.h>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>

#define LLI long long int
#define LLU long long unsigned int
#define LI  long int
#define LU  long unsigned
#define MAX(a,b) ((b)^(((a)^(b))&-((a)>(b))))
#define MIN(a,b) ((b)^(((a)^(b))&-((a)<(b))))
#define BUG printf("BUGGEeee");
#define PRINT(n) printf("%d",n);
#define MOD 1000000007
#define POWER2(v) (v && !(v & (v - 1)))
#define kk argv[1]



using namespace std;


int main(int argc,char* argv[])
{
	int T,K=0;
	scanf("%d",&T);
	while(T--)
	{
		K++;
		double C,F,X,rate=2;
		scanf("%lf %lf %lf",&C,&F,&X);
		double a1,b1=0,c1=0,c2=0;
		a1=X/rate;
		while(true)
		{
			c2=C/rate;
			b1=c1+c2+X/(rate+F);
			
			if(b1<a1)
			{c1+=c2;a1=b1;rate+=F;
				//printf("%lf %lf\n",c2,c1);
				}
			else {break;}
			
	}
	printf("Case #%d: %lf\n",K,a1);
}
	return 0;
	}


