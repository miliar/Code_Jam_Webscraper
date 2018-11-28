#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;
int main()
{

freopen("B-small-attempt0.in","r",stdin);
freopen("output","w",stdout);
double c , f , x , wfarm1 , wfarm2 , nfarm , total , persec;
int t,a;
scanf("%d",&t);
for(a=1;a<=t;a++)
{
  scanf("%lf %lf %lf",&c,&f,&x);
  persec = 2;
  total = 0;
  while(1)
  {
  nfarm = x/persec ;

  wfarm1 = c/persec ;
  persec += f ;

  wfarm2 = wfarm1 + x/persec ;

  if(wfarm2>=nfarm)
  {
    total += nfarm ;
    break;
  }
  else
    total += wfarm1;

  }

   printf("Case #%d: %0.7lf\n",a,total) ;

}
return 0;
}
