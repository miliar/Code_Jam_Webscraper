#include<stdio.h>
#include<conio.h>

int main()
{
     freopen("bout.in","w",stdout);
     freopen("bin.in","r",stdin);
    
    int t,y=1,z=0;
    double totalTimeElasped,c,x,f,productionPerSecond;
    
    scanf("%d",&t);
    
    while(t--)
    {
      totalTimeElasped=0.0;
      productionPerSecond=2.0;
      y=1;        
	  z++;
      scanf("%lf %lf %lf",&c,&f,&x);
	  
	    if(x<c)
		{
		  totalTimeElasped = x/2;
		}
      
        else
        {
		   while(y)
		   {
			 
			 /*case1*/
			    if((x/productionPerSecond )> ((c/productionPerSecond)+(x/(productionPerSecond+f)))) 
			    {
					totalTimeElasped = c/productionPerSecond+totalTimeElasped;
					productionPerSecond = productionPerSecond + f;
				}
			 /*case2*/
				else
				{
					 totalTimeElasped = x/productionPerSecond+totalTimeElasped;
				     y=0;
				}
			
		   }
		   
		}		
              
         printf("Case #%d: %.7lf\n",z,totalTimeElasped);       
              
              
    }
    
 getch();
return 0;
}
