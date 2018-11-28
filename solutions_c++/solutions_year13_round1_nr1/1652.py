#include<conio.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
  int n,l,r,t,solution=0;
  char a;
     FILE* in = NULL;
     FILE* out = NULL;
    in = fopen("A-small-0.in", "r");
    out = fopen("A-small-0.out", "w");
   fscanf(in, "%d", &n);
   fgetc(in);
   
   for(l=0;l<n;l++){
                    solution=0;
                    fscanf(in,"%d",&r);
   fscanf(in,"%d",&t);
   while(t>=0){ t=t-(((r+1)*(r+1))-(r*r));
   r=r+2;
   solution++;}
   fgetc(in);
   
   if(t!=0){ solution=solution-1;}
   
  
       
	   
	   fprintf(out,"Case #%d: %d",l+1,solution);
                    
       if(l!=n-1) fprintf(out,"\n");}
                           
    fclose(in);
    fclose(out);
}
