#include <iostream>
#include <stdio.h>
#include <vector>
FILE *fin = fopen("input.in","r");
FILE *fout = fopen("output.txt","w");
using namespace std;
void pro()
{
    unsigned long long int r,t;
    fscanf(fin,"%llu",&r);
    fscanf(fin,"%llu",&t);
     unsigned long long int cnt=0,sum,r1=r,r2=r+1;
     sum=(r2*r2)-(r1*r1);
     while(1)
     {
          if(sum<=t)
          {
            cnt++;
            t-=sum;
            sum+=4;
          }
          else
            break;
     }
     fprintf(fout,"%llu\n",cnt);
}
int main()
{
    int n;
    fscanf(fin,"%d",&n);
    for(int i=0;i<n;i++)
    {
        fprintf(fout,"Case #%d: ",i+1);
        pro();
    }
}
