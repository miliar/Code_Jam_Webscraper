#include<stdio.h>
#include<conio.h>
#include<iostream.h>

int main()
{
    freopen("B-large.in","r",stdin);
     freopen("outp.in","w",stdout);
     
    int i,n;
    double C,F,X;
    double t1,t2;
    double r=2.0;
    cin>>n;
   
   for(i=0;i<n;i++)
   {
                    cin>>C>>F>>X;
                    
                    r=2;
                    
                    t1=C/r;
                    t2=X/r;
                    
                    if(t2<t1)
                     printf("Case #%d: %0.7lf\n",i+1,t2);
                     
                     else
                     {
                    
                    while( (t1+(X/(r+F))) <= t2 )
                    {
                           r=r+F;
                           
                           t2=t1+X/r;
                           t1=t1+C/r;
                           
                    }
                    
                    if((t1+(X/(r+F))) >= t2 )
                     printf("Case #%d: %0.7lf\n",i+1,t2);
                     
                     }
                               
                    
   }
   
   getch();
   return 0;
    
}
