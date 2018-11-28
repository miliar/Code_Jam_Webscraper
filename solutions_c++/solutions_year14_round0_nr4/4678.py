#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int func (const void * a, const void * b)
{
 if (*(float*)a > *(float*)b)
  return 1;
 if (*(float*)a == *(float*)b)
  return 0;
 if (*(float*)a < *(float*)b)
  return -1;
}


main()
{
 	  int i,t,tt,size,s,x,cont;
 	  float *vetk,*vetn;
 	  scanf("%d",&t);
 	  for(tt=1;tt<=t;tt++)
 	  {   
	  	  printf("Case #%d: ",tt);
		  scanf("%d",&size);
		  vetk=(float *) malloc (size*sizeof(float));
		  vetn=(float *) malloc (size*sizeof(float));
		  
		  for(s=0;s<size;s++)
			 scanf("%f",&vetn[s]);
		  for(s=0;s<size;s++)
			 scanf("%f",&vetk[s]);
		  
		  qsort(vetn,size,sizeof(float),func);
		  qsort(vetk,size,sizeof(float),func);
		  
		  x=0;
		  cont=0;
		  for(i=0;i<size;i++)
		  {
			 for(s=x;s<size;s++)
			    {
		 				if(vetn[i]>vetk[s])
		 				{
	                     cont++;
						 x=s+1;
						 break;
						}
			 	}
		  }
		  
		  printf("%d ",cont);
		  
		  x=0;
		  cont=0;
		  for(i=0;i<size;i++)
		  {
			 for(s=x;s<size;s++)
			    {
		 				if(vetk[i]>vetn[s])
		 				{
	                     cont++;
						 x=s+1;
						 break;
						}
			 	}
		  }
		  
		  printf("%d\n",(size-cont));
	  }
}
