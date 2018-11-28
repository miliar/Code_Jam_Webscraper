#include <stdio.h>

int main(int argc,char *argv[]){
int t;
double c,f,x;
FILE *fpr = fopen(argv[1],"r");
fscanf(fpr,"%d",&t);
int p=0;
while(p<t)
{ 
  fscanf(fpr,"%lf",&c);
  fscanf(fpr,"%lf",&f);
  fscanf(fpr,"%lf",&x);
  
  double sec=0.0; double rate=2.0; double cookies=0.0;
  sec=c/rate; cookies = c;
  while(1)
  {
   if(x/(rate+f) < (x-cookies)/rate)
     {
     rate+=f; 
     sec+= c/rate;
     cookies = c;
     }
    else {sec+= (x-cookies)/rate;
     break;
    }
   }
   printf("Case #%d: %lf\n",p+1,sec);
  p++;
}
fclose(fpr);
return 0;
}
