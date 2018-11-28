#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
FILE *fin,*fout;
int n;
double b[1005],f[1005];
void solve1()
{
    int castig=0;
    if(n==1)
    {
        if(b[1]>f[1]) fprintf(fout,"1 ");
        else  fprintf(fout,"0 ");
    }
    else
    {
        sort(b+1,b+n+1);
        sort(f+1,f+n+1);
        int i=1,j=1;
        int final=n;
        while(i<=n)
        {
            if(b[i]<f[j]) final--;
            else {castig++;j++;}
            i++;
        }
        fprintf(fout,"%d ",castig);
    }
}
void solve2()
{
    if(n==1)
    {
        if(b[1]>f[1]) fprintf(fout,"1\n");
        else  fprintf(fout,"0\n");
    }
    else
    {
  int i=1,j=1;
  while(i<=n && j<=n)
  {
      while(f[j]<b[i] && j<=n) j++;
      if(j==n+1) break;
      else i++;j++;
  }
  fprintf(fout,"%d \n",n-i+1);
    }
}
int main()
{
    int t,i;
        fin=fopen("t.in","r");
        fout=fopen("output.txt","w");
        fscanf(fin,"%d",&t);
        for(int j=1;j<=t;j++){
            fprintf(fout,"Case #%d: ",j);
            fscanf(fin,"%d",&n);
            for(i=1;i<=n;i++)
                fscanf(fin,"%lf",&b[i]);
            for(i=1;i<=n;i++)
                fscanf(fin,"%lf",&f[i]);
            solve1();
            solve2();
        }
}
