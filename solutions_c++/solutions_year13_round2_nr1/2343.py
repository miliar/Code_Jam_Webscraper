#include<conio.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>


int main(){
   int i,j,k, t[100], n,cas,l,prem,sol,solp,premp;




     FILE* in = NULL;
     FILE* out = NULL;
    in = fopen("A-small-0.in", "r");
    out = fopen("A-small-0.out", "w");
   fscanf(in, "%d", &cas);
   fgetc(in);
    for(l=0;l<cas;l++){sol=0;solp=0;
    fprintf(out,"Case #%d: ",l+1);            
    
         fscanf(in,"%d",&prem);
         premp=prem;
         fscanf(in,"%d",&n);
         fgetc(in);
         for(i=0;i<n;i++){
                          fscanf(in,"%d",&t[i]);
                          
                          }
                          
                           for(i=0;i<n;i++)
   {for(j=0;j<n;j++)
     {if(t[j]>t[i])
      {
       k=t[j];
       t[j]=t[i];
       t[i]=k;
       }
      }
       ;
    }
    
    for(i=0;i<n;i++){
                     if(prem>t[i]){
                                   prem=prem+t[i];
                                   
                                   }
                     else{sol=sol+1;
                          if(prem+prem-1>t[i]){
                                                    prem=prem+prem-1+t[i];}
                                                    
                          }
                                   }
                                   
                                   for(i=0;i<n;i++){
                     if(premp>t[i]){
                                   premp=premp+t[i];
                                   
                                   }
                     else{if(premp-1!=0){solp=solp+1;
                          while(premp+premp-1<=t[i]){solp=solp+1;
                          
                                                    premp=premp+premp-1;}
                                                    premp=premp+premp-1+t[i];}
                                                    else solp=1000;
                                                    
                          }
                     
                          
                                   }
                                   
                                   
                                   
                                   
    if(sol<=solp){
                     fprintf(out,"%d",sol);}
                     else{ fprintf(out,"%d",solp);}
       if(l!=cas-1) fprintf(out,"\n");
                            }
    fclose(in);
    fclose(out);
}
