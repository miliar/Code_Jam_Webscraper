#include <cstdlib>
#include <cstdio>
#include <iostream>

using namespace std;

FILE *f1=fopen("B-large.in","r");
FILE *f2=fopen("B-large.out","w");

int t;
double c,f,x,mintime,nowtime,s;

int main(int argc, char *argv[])
{
    fscanf(f1,"%d",&t);
    for(int k=1;k<=t;k++)
    {
      fscanf(f1,"%lf%lf%lf",&c,&f,&x);
      mintime=x/2;s=2;nowtime=0;
      while(nowtime<mintime)
      {
        nowtime=nowtime+c/s;s=s+f;
        if(nowtime+x/s<mintime)mintime=nowtime+x/s;
      }
      fprintf(f2,"Case #%d: %.7f\n",k,mintime);
    }
    return 0;
}
