#include <string.h>
#include <strings.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <malloc.h>
#include <iostream>
using namespace std;
void go(double *x,double *y,int N,int *r0,int *r1);
#define _PROTO_QSORT (int (*)(const void *, const void *))
int mycmp(double *i,double *j){return (*i) > (*j);}

void go(double *x,double *y,int N,int *r0,int *r1)
{
  int i;

  qsort(x,N,sizeof(double),_PROTO_QSORT mycmp);
  qsort(y,N,sizeof(double),_PROTO_QSORT mycmp);

  // for(i=0;i<N;i++)
  //   printf("%lf ",x[i]);
  // printf("\n");
  // for(i=0;i<N;i++)
  //   printf("%lf ",y[i]);
  // printf("\n");

  // vraie war
  int v = 0;
  int h = N-1;
  for(i=N-1;i>=0;i--)
    {
      if (x[i]>y[h])
        {
          //    int j;
          // elle gagne
          //for(j=0;j<i;j++)
          //  y[j]=y[j+1];
          v++;
        }
      else
        h--;
    }
  *r1 = v;

  // vraie war
  v = 0;
  int hlui = N-1;
  int blui = 0;
  int hl = N-1;
  int bl=0;
  for(i=N-1;i>=0;i--)
    {
      // elle,annonce entre y[hlui-1] et y[hlui]
      if (x[hl]>y[hlui])
        {
          v++;
          hl --;
          hlui--;
        }
      else
        {
          bl++;
          hlui--;
        }
    }
  *r0 = v;
}  // FIN  void go(double *x,double *y,int N,int *r0,int *r1)
// ************************************************************


int main(int na,char *para[]) 
{
  int i,T;
#define _MMAX (1000*8+10)
  double x[1000];
  double y[1000];
  char line[_MMAX];
  fgets(line,_MMAX,stdin);
  sscanf(line,"%d",&T);
  for(i=0;i<T;i++)
    {
      int N;
      fgets(line,_MMAX,stdin);
      sscanf(line,"%d",&N);
      // 1er ligne
      fgets(line,_MMAX,stdin);
      char * pch;
      pch = strtok (line," ");
      int nb=0;
      while (pch != NULL)
        {
          //printf("%s\n",pch);//Ps[i++]= strtol(pch);
          sscanf(pch,"%lf",&x[nb++]);
          pch = strtok (NULL," ");
        }
      // 2em ligne
      fgets(line,_MMAX,stdin);
      pch = strtok (line," ");
      nb=0;
      while (pch != NULL)
        {
          //printf("%s\n",pch);//Ps[i++]= strtol(pch);
          sscanf(pch,"%lf",&y[nb++]);
          pch = strtok (NULL," ");
        }

      int r0,r1;
      go(x,y,N,&r0,&r1);
      printf("Case #%d: %d %d\n",i+1,r0,r1);
    }

  return 0;
}		/* FIN main() */
/* *********************************************************** */
