#include <string.h>
#include <strings.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <malloc.h>
#include <iostream>
using namespace std;
double go(double C,double F,double X);

double gogo(double C,double F,double X)
{
  int i,nfermeachetees = (int)X/C-1;
  double t0=0;
  for(i=0;i<nfermeachetees;i++)
    t0 += C/(2+i*F);
  double rapport = 2+nfermeachetees*F;
  t0 += X/rapport;

  nfermeachetees++;
  double t1=0;
  for(i=0;i<nfermeachetees;i++)
    t1 += C/(2+i*F);
  rapport = 2+nfermeachetees*F;
  t1 += X/rapport;
    
  return t0<t1 ? t0 : t1;
}     // FIN       double gogo(double C,double F,double X);
// ************************************************************

double go(double C,double F,double X)
{
  int i,nfermeachetees;
  double ans;
  double t0=-C/(2-F);
  for(nfermeachetees=0;nfermeachetees<(int)X/C;nfermeachetees++)
    {
      double t=0;
      for(i=0;i<nfermeachetees;i++)
        t += C/(2+i*F);
      t0 +=  C/(2+(nfermeachetees-1)*F);
      double rapport = 2+nfermeachetees*F;
      t += X/rapport;
      if ((t<ans)||(nfermeachetees==0))
        ans = t;
    }
  return ans;
}     // FIN double go(double C,double F,double X);
// ************************************************************
double go1(double C,double F,double X)
{
  int i,nfermeachetees;
  double ans;
  for(nfermeachetees=0;nfermeachetees<(int)X/C;nfermeachetees++)
    {
      double t=0;
      for(i=0;i<nfermeachetees;i++)
        t += C/(2+i*F);
      double rapport = 2+nfermeachetees*F;
      t += X/rapport;
      if ((t<ans)||(nfermeachetees==0))
        ans = t;
    }
  return ans;
}     // FIN       double go(double C,double F,double X);
// ************************************************************


int main(int na,char *para[]) 
{
  int i,T;
  char line[6];
  int p[4],q[4],P[4];

  fgets(line,6,stdin);
  sscanf(line,"%d",&T);
  for(i=0;i<T;i++)
    {
      double C,F,X;
      char line[256];
      fgets(line,255,stdin);
      sscanf(line,"%lf %lf %lf",&C,&F,&X);
      double ans = go(C,F,X);
      printf("Case #%d: %.7lf\n",i+1,ans);
    }

  return 0;
}		/* FIN main() */
/* *********************************************************** */
