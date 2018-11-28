#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>




int main(){
    
           int t,e=0,l;
           double i,j;
           scanf("%d",&t);
           
           double X,C,F;
           //double tim,t1=0;
           double d[t];
           double k=2;
           
         
          int a=1;
           
           while(t--){
                      scanf("%lf%lf%lf",&C,&F,&X);
                      double a1=0;
                      double k=2;
                      
                      while(1)
                      {
                              if(X/k >( C/k +(X/(k+F))))
                              {
                                     a1+=C/k;
                                     k=k+F;
                                     }
                                     else
                                     break;
                                     }
                          a1+=X/k;
                          d[e++]=a1;
                                     
                              
                      
                        
                          }
                          
                          
                          
                                                                                                                                         
                        for(l=0;l<e;l++)printf("Case #%d: %.7f\n",a++,d[l]) ;                    
                
                      
                      
                      
                      
                      
                      
         
           return 0;
           }

