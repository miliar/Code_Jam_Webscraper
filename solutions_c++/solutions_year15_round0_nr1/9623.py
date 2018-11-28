#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

int i,j,x,y,cont,aux;
char cad[10000];


int  main () {
    
   FILE * pw;
   FILE * pr;
   
   
   pr = fopen ("A-large.in","r");
   pw = fopen ("A-large.out","w"); 
    
   fscanf(pr,"%d",&j); 
    
    for(i=0; i<j; i++) {
        
        fscanf(pr,"%d ",&y);
        fgets(cad,10000,pr);
     
        
        cont = aux = 0;
        
        for(x=0; x<=y; x++) {
            
            if(cont < x){
            
              aux += x-cont;
              cont += x-cont;
                
            } 
            
          cont += cad[x] - '0';  
            
        }
        
        fprintf(pw,"Case #%d: %d\n",i+1,aux);
        
              
        
    }
    
    
   fclose (pw);
   fclose (pr);
   
    
    
    
  return 0;   
}

