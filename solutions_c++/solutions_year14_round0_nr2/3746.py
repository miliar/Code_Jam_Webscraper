#include<stdio.h>

int main()
{
  long int t,i;
  double c,f,x,r=2,act_sec, nxt_step_sec,final_sec;
  scanf("%ld",&t);
  for (i=1L; i<=t;i++)
  {
    r=2.0000000; act_sec=0.0000000;
    nxt_step_sec=0.0000000,final_sec=0.0000000;
    scanf("%lf %lf %lf",&c,&f,&x);
    if(c>=x)
      final_sec = x/r;
    else
    {
      do
      {
        act_sec = (x/r);
        nxt_step_sec = (c/r) + (x/(r+f));

        if(act_sec > nxt_step_sec)
        {

	  final_sec +=(c/r);
	  r+=f;
        }
        else
        {
  	  final_sec +=act_sec;

	  break;
        }
      }while(1);
    }
     printf("Case #%ld: %.7lf\n",i,final_sec);
  }
  return 0;
}
