#include <string.h>
#include <strings.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <malloc.h>
#include <iostream>
using namespace std;

int main(int na,char *para[]) 
{
  int i,T;
  char line[6];
  int p[4],q[4],P[4];

  fgets(line,6,stdin);
  sscanf(line,"%d",&T);
  for(i=0;i<T;i++)
    {
      int j,k,x,a0,a1,a2,a3;
      char line[256];
      for(k=0;k<2;k++)
        {
          fgets(line,256,stdin);
          sscanf(line,"%d",&x);
          for(j=0;j<4;j++)
            {
              fgets(line,256,stdin);
              if (j+1==x)
                {
                  sscanf(line,"%d %d %d %d",&a0,&a1,&a2,&a3);
                  if (k==0)
                    {
                      p[0]=a0;
                      p[1]=a1;
                      p[2]=a2;
                      p[3]=a3;
                    }
                  else
                    {
                      q[0]=a0;
                      q[1]=a1;
                      q[2]=a2;
                      q[3]=a3;
                    }
                }
            }
        }
      // est-ce que ca match ?
      for(j=0;j<4;j++)
        P[j] = 0;
      for(j=0;j<4;j++)
        {
          // est-ce que p[j] est aussi ds q
          for(k=0;k<4;k++)
            if (q[k]==p[j])
              P[j]=1;
        }
      int z= P[0]+P[1]+P[2]+P[3];
      if (z==1)
        {
          for (j=0;j<4;j++)
            if (P[j]==1)
              break;
          printf("Case #%d: %d\n",i+1,p[j]);
        }
      else if (z==0)
        printf("Case #%d: Volunteer cheated!\n",i+1);
      else
        printf("Case #%d: Bad magician!\n",i+1);
    }

  return 0;
}		/* FIN main() */
/* *********************************************************** */
