#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define LEN 17
int main(){
    FILE *fp1,*fp2;
    fp1 = fopen("B--large.in","r"); 
    fp2 = fopen("B--dataout.out","w"); 
    int m;

    fscanf(fp1,"%d",&m);
    
    
    
    for( int kk = 0 ; kk < m ; kk ++ ){
         double c,f,x;
         double ans = 0;
         double tc = 0;
         double tclast = 0;
         
         double tx = 0;
         double txlast = 0;
         double nc = 1;
         double nf = 0;
         fscanf(fp1,"%lf%lf%lf",&c,&f,&x);
         txlast = x/2.0;
        
        // fprintf(fp2,"%lf%lf%lf",c,f,x);
         for( ;; ){
              double tmp30 = tc;
              
              tc = (c+2*tclast+nf*f*tclast)/(2+nf*f);
              nf++;
              tclast = tc;
              tx   = (x+2*tclast+nf*f*tclast)/(2+nf*f);
              if( tx < txlast ){
                  txlast = tx;    
              }else{
                   break; 
              }
              tmp30++;
             // break;
         } 
         fprintf(fp2,"Case #%d: %.7lf\n",kk+1,txlast);
    }
    
   
    fclose(fp1);
    fclose(fp2);
    return 0;
    
}
