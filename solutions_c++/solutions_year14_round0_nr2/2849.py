#include<iostream>
#include<cstdio>

using namespace std;

void farm(double c, double f, double x,int k)
{
 double r,t;
 if(x/2 < c/2 + x/(2+f))
   {  printf("Case #%d: %0.7lf\n", k,x/2);
     return ;
	 }
  else
    {
       t = c/2;
	   for(int i=1; ;i++)
         {
            r = (2 + (f*i));
			if((t + x/r) > (t + c/r + x/(2 + f*(i+1))))
			    { t+=c/r;
				  continue;
				  }
			else
               {
                  printf("Case #%d: %0.7lf\n",k,(t + x/r));
                  break;
                }
         }
    }
	return ;
 }



int main()
{
  int t;
  scanf("%d",&t);
  for(int k=1;k<=t;k++)
  {
    double c,f,x;
	scanf("%lf%lf%lf",&c,&f,&x);
	farm(c,f,x,k);
	}
	return 0;
	}
