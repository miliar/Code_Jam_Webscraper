#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
int a[100];
int b[100];
int n;
int total,es;
int jud(int x,int y)
{
  if( x==-1 && y==-1)
    return 0;
  else if( x==y )
  {
    if(a[x]<2)
      return 0;
  }
  else if(x==-1)
  {
    if(a[y]<1)
      return 0;
  }
  else if(y==-1)
  {
    if(a[x]<1)
      return 0;
  }
  else
  {
    if(a[x]<1||a[y]<1)
      return 0;
  }
  
  int i;
  int aa[100],tt=0;
  for(i=0;i<100;i++)
    aa[i] = a[i];
  
  if(x!=-1)
    aa[x]--;
  if(y!=-1)
    aa[y]--;
  
  for(i=0;i<n;i++)
    tt+=aa[i];
  
  for(i=0;i<n;i++)
    if((double)aa[i]/tt>0.5)
      return 0;
  
  return 1;
}
int main() {
  int i,j;
  int bj;
  int t,T;

  FILE *in = fopen("/Users/Basun/Desktop/test.txt","r");
  FILE *out = fopen("/Users/Basun/Desktop/a.txt", "w");
  fscanf(in,"%d", &T);
  for(t=1;t<=T;t++)
  {
    for(i=0;i<100;i++)
    {
      a[i]=0;
      b[i]=0;
    }
    fprintf(out, "Case #%d: ",t );
    fscanf(in,"%d",&n);
    total = 0;
    es = 0;
    for(i=0;i<n;i++)
      fscanf(in,"%d",&a[i]);
    for(i=0;i<n;i++)
      total += a[i];
    while(total > 0)
    {
      bj = 1;
      for(i=-1;i<n && bj;i++)
      {
        for(j=-1;j<n && bj;j++)
        {
          cout<<i<<" "<<j<<endl;
          if(jud(i, j))
          {
            if(i!=-1 && j!= -1)
            {
              fprintf(out, "%c%c ",'A'+i,'A'+j);
              a[i] -= 1;
              a[j] -= 1;
              total -=2;
            }
            else if(i==-1)
            {
              fprintf(out, "%c ",'A'+j);
              a[j] -= 1;
              total -=1;
            }
            else
            {
              fprintf(out, "%c ",'A'+i);
              a[i] -= 1;
              total -=1;
            }
            bj = 0;
          }
        }
      }
    }
    fprintf(out, "\n");
  }
  
  return 0;
}
