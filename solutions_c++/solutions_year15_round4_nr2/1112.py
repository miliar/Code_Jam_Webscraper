//Khagan

#include <algorithm>
#include <stdio.h>
#define  maxn      100
using    namespace std;

int T,n;
double V,X;
double R[maxn];
double C[maxn];

int main()
{
  freopen("B-small-attempt3.in","r",stdin);
  freopen("cikti.txt","w",stdout);
  scanf("%d",&T);
  for(int t=1 ; t<=T ; t++)
  {
    scanf("%d%lf%lf",&n,&V,&X);
    for(int i=0 ; i<n ; i++)
      scanf("%lf%lf",&R[i],&C[i]);
    if(n==1)
    {
      if(X!=C[0])
        printf("Case #%d: IMPOSSIBLE\n",t);
      else
        printf("Case #%d: %.9lf\n",t,V/R[0]);
    }
    else if(n==2)
    {
      if(C[0]>C[1])
      {
        swap(R[0],R[1]);
        swap(C[0],C[1]);
      }
      if(X<C[0])
        printf("Case #%d: IMPOSSIBLE\n",t);
      else if(X>C[1])
        printf("Case #%d: IMPOSSIBLE\n",t);
      else
      {
        if(C[0]==C[1])
        {
          printf("Case #%d: %.9lf\n",t,V/(R[0]+R[1]));
          continue;
        }
        double T0=(V*(C[1]-X))/(C[1]-C[0]);
        double T1=V-T0;
        double a=T0/R[0];
        double b=T1/R[1];
        if(a>b) swap(a,b);
        printf("Case #%d: %.9lf\n",t,b);
      }
    }
  }
  return 0;
}
