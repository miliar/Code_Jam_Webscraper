#include <iostream>

int main(int argc, char *argv[])
{
    int T,Case=0;
	long long r, reqt, inr, outr, y;
	long double t, pu;
    scanf("%d", &T);
    do
    {
       scanf("%lld%lf", &r, &t);	   
	   inr = r;
	   y=0;
	   pu=0;
	   while(1)
	   {
		   pu+= (((2 * inr) + 1)); //3.1415926535897932384626433
		   if((t-pu)>=0)
			   ++y;
		   else 
			   break;
		   inr += 2;
	   }
	   printf("Case #%d: %lld\n", ++Case, y);
	}while(--T);
}
