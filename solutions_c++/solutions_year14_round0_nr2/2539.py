#include <stdio.h>
#include <stdlib.h>

double farmcost;
double farmrate;
double targets;
double lasts;
double nows;
double timefarm;
double timecomplete;
double rates;
double pluss;
int t;
main()
{
 freopen("B-large.in","r",stdin);
 freopen("B-large.out","w",stdout);
 scanf("%d",&t);
 for(int tests=1;tests<=t;tests++)
 {
  timefarm=0;
  lasts=1000000;
  scanf("%lf%lf%lf",&farmcost,&farmrate,&targets);
  rates=2;
  for(int i=0;;i++)
  {
   if(i>0){pluss=farmcost/rates;timefarm=timefarm+pluss;rates=rates+farmrate;}
   timecomplete=targets/rates;
   nows=timefarm+timecomplete;
   if(nows<lasts){lasts=nows;}
   else{break;}
  }
  printf("Case #%d: %.7lf\n",tests,lasts);
 }
 return 0;
}
