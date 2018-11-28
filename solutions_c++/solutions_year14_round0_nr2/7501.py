#include <iostream>
#include <string>
#include <fstream>
#include <cstdio>
using namespace std;
int T;
int CountT;

double C,F,X;
double step;
double buy,wait;
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int i,j,k,f;
    scanf("%d",&T);
	double result;
	double result2;
	double remain;
    for(CountT=1;T>0;T--,CountT++)
    {
        scanf("%lf %lf %lf",&C,&F,&X);
		step=2;

		remain=0;
		while(true)
		{
			result=X/step;

			result2=C/step+X/(step+F);
			if(result+remain<result2+remain)break;
			
			remain+=C/step;
			step+=F;
		}

        printf("Case #%d: %.7f\n",CountT,remain+result);
		
    }
	
}
