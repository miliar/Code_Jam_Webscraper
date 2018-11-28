#include<cstdio>
#include<stdlib.h>

using namespace std;

FILE *fin;
FILE *fout;

int t,i,j,n;
double c,f,x;
double result;
int main(){
  fin = fopen("B-large.in","r");
  fout = fopen("output.txt","w+");
  fscanf(fin,"%d",&t);
  for (i=0;i<t;i++){
    fscanf(fin,"%lf%lf%lf",&c,&f,&x);     
    double temp;
    temp = x/c-2/f-1.0;
    n = (int)temp;
    result=0;
    if (temp < 0){
      result = x / 2.0;
    }
    else{    
      for (j=0;j<=n;j++){
        double temp2;
        temp2 = j;
        result = result + c/(2.0+temp2*f);
      }
      temp = n + 1.0;
      result = result + x/(2.0+temp*f);
    }
    
    fprintf(fout,"Case #%d: %.7lf\n",i+1, result);
  }
  fclose(fin);
  fclose(fout);
  system("pause");
  return 0;    
}
