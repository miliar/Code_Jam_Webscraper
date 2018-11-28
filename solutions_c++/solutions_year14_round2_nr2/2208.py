#include <string.h>
#include <strings.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <malloc.h>
#include <iostream>
using namespace std;
#include <vector>

void go(int A,int B,int K,int k)
{
  // stupid
  //printf("%d %d %d\n",A,B,K);
  int i,j,ans=0;
  for(i=0;i<A;i++)
    for(j=0;j<B;j++)
      {
        int q= i&j;
        if (q<K)
          ans++;
      }
  printf("Case #%d: %d\n",k,ans);
}     // FIN go()
// ********************************************************

int main(int na,char *para[]) 
{
  int i,T;
  char line[256];

  fgets(line,256,stdin);
  sscanf(line,"%d",&T);
  for(i=0;i<T;i++)
    {
      fgets(line,256,stdin);
      int A,B,K;
      sscanf(line,"%d %d %d",&A,&B,&K);
      go(A,B,K,i+1);
    }

  return 0;
}		/* FIN main() */
/* *********************************************************** */
