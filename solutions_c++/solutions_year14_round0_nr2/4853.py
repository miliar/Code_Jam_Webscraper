#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

main()
{
 	  double c,f,x,compx,compf,cont,time;
 	  int t,tt;
 	  
 	  scanf("%d",&t);
 	  for(tt=1;tt<=t;tt++)
 	  {
          time=0;
          cont=2;
  	      scanf("%lf %lf %lf",&c,&f,&x);
  	      do{
		  compf=c/cont;
		  time+=compf;
  	      compf+=(x/(cont+f));
  	      compx=(x/cont);
  	      cont+=f;
  	      
		  }while(compx>compf);
		  cont-=f;
		  compf=c/cont;
		  time-=compf;
		  time+=compx;
		  printf("Case #%d: ",tt);
		  printf("%.7lf\n",time);
	  }
}
