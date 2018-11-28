//shjj-cook

#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

double Now,C,F,X,V,Time;

int main()
{
int Test,tt=0;scanf("%d",&Test);
for (;Test--;)
  {
  scanf("%lf%lf%lf",&C,&F,&X);
  Now=Time=0;V=2;
  for (;;)
    {
	double t1=(X-Now)/V;
	double t2=(C-Now)/V+X/(V+F);
	if (t1<t2) {Time+=t1;break;}
	  else Time+=(C-Now)/V,Now=0,V+=F;
	}
  printf("Case #%d: %.7lf\n",++tt,Time);
  }
}