#include<stdio.h>
#include<conio.h>

int main()
{
    freopen("bcclargeout.in","w",stdout);
    freopen("bcclargein.in","r",stdin);
 
    int t,i,j,n,a,deceit,war,z=0;
	float temp,Noami[1000],Ken[1000],NoamiW[1000],KenW[1000];
	scanf("%d",&t);
	
	while(t--)
	{
		z++;
		deceit=0;	
  	    scanf("%d",&n);
        war=0;
        		
		for(i=0;i<n;i++)
		{
		    scanf("%f",&Noami[i]);
 		}
		
		for(i=0;i<n;i++)
		{
		    scanf("%f",&Ken[i]);
 		}
		for (i = 0; i < n; i++)
        {
          for (j = 0; j < (n - i - 1); j++)
          {
            if (Noami[j] > Noami[j + 1])
            {
                temp = Noami[j];
                Noami[j] = Noami[j + 1];
                Noami[j + 1] = temp;
            }
          }
        }
        for (i = 0; i < n; i++)
        {
            for (j = 0; j < (n - i - 1); j++)
            {
                if (Ken[j] > Ken[j + 1])
                {
                temp = Ken[j];
                Ken[j] = Ken[j + 1];
                Ken[j + 1] = temp;
                }      
            }
        }
         
     for(i=0;i<n;i++)
	  {
         KenW[i]   =Ken[i];
         NoamiW[i] =Noami[i];
        
       }
	
          for(i=0;i<n;i++)
              {
                              for(j=0;j<n;j++)
                              if(KenW[j]>NoamiW[i])
                              {
                                   KenW[j]=-1;
                                   break;
                              }
                              if(j==n)
                              war++;        
              }  

        a=n;
        j=0;
        
		for(i=0;i<n;i++)
		{
		  
		    if(Noami[i]<Ken[j])
			{
             a=a-1;                  
			 deceit++;
			 Ken[a]= -1.0;
			}
			else
			{
              j++; 
            }
	     }
                        deceit=n-deceit;  
                        printf("Case #%d: %d %d\n",z,deceit,war);    
      } 
getch();
return 0;
}
