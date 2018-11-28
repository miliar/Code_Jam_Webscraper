#include <string.h>
#include <strings.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <malloc.h>
#include <iostream>
using namespace std;
#include <vector>

void go(char *line,int k)
{
  int n,d;
  sscanf(line,"%d/%d",&n,&d);
  //printf("%d %d   ",n,d);
  int i,mn = (int)(sqrt(n*1.0));
  int md = (int)(sqrt(d*1.0));
  int m = mn<md ? md : mn;
  for(i=2;i<m;i++)
    {
      if (n%i==0) // i est un diviseur
	{
	  if (d%i==0)
	    {
	      n/=i;
	      d/=i;
	    }
	}
    }
  //printf("%d %d\n",n,d);

  // d pusance de 2 ?
  m =0;
  if (d==1)
    {
      if (n==0)
	{
	  printf("Case #%d: 0\n",k);
	  return ;
	}
      else
	{
	  printf("Case #%d: impossible\n",k);
	  return;
	}
    }
  for (i=d;;)
    {
      if (i%2)
	{
	  printf("Case #%d: impossible\n",k);
	  return;
	}
      m++;
      i /= 2;
      if (i==1)
	break;
    }
  //printf("m= %d\n",m);

  int pot=2;
  for (i=1;;)
    {
      if (pot>=n)
	break;
      i++;
      pot *=2;
    }
  // 2**(i-i)<n<2**i
  i--;
  //printf("n= %d i=%d\n",n,i);
  printf("Case #%d: %d\n",k,m-i);
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
      go(line,i+1);
    }

  return 0;
}		/* FIN main() */
/* *********************************************************** */
