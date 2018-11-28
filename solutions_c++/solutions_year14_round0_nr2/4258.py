#include<stdio.h>
int main()
{
	  int t,i=0,cas=1,j;
	  double c,f,x,nw=0.0,old=0.0,temp=0,s;
	  scanf("%d",&t);
	  while(t--)
	     {
		    i=0;
		    scanf("%lf %lf %lf",&c,&f,&x);
		    
		    old=x/2;
		    
		    while(1)
		      {
			    
			    
				
				temp+=c/(2+i*f);
			      
			    nw=temp+x/(2+((i+1)*f));
			    if(nw>old)
			    {
			    	break;
			    }
			    else 
			    old = nw;
		      
		       // printf("value of old and new are %lf %lf and i is %d \n ",old,nw,i);
			    i++;
			  }
		
		      printf("Case #%d: %.7lf\n",cas,old);
		      i=0;
		      cas++;
		      temp=0;
		      nw=0;
		      old=0;
	    }
	return 0;
	
}
