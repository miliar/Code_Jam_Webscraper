#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <vector>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"
#define lim 21
#define lim2 201
#define lim3 1<<20
#define lim4 41
#define pb push_back

int cs,c,i,j,k,p,n;
int R[lim][lim4],C[lim2],T[lim],K[lim],A[lim4];
vector <int> V2,V[lim3];
bool M[lim3];

int main()
{
  scanf("%d",&cs);
  for(c=1;c<=cs;c++)
  {
    scanf("%d%d",&k,&n);
    for(i=0;i<k;i++)
    {
      scanf("%d",&A[i]);
      A[i]--;
    }
    for(i=0;i<n;i++)
    {
      scanf("%d%d",&T[i],&K[i]);
      T[i]--;
      for(j=0;j<K[i];j++)
      {
        scanf("%d",&R[i][j]);
        R[i][j]--;
      }
    }
    for(i=0;i<1<<n;i++)
      V[i].clear();
    memset(M,0,sizeof M);
    M[0]=1;
    for(i=0;i<1<<n;i++)
    {
      memset(C,0,sizeof C);
      for(j=0;j<k;j++)
        C[A[j]]++;
      for(j=0;j<n;j++)
        if(i&1<<j)
        {
          C[T[j]]--;
          for(p=0;p<K[j];p++)
            C[R[j][p]]++;
        }
      if(M[i])
        for(j=0;j<n;j++)
          if(!(i&1<<j) && C[T[j]])
          {
            V2=V[i];
            V2.pb(j);
            if(M[i|1<<j])
            {
              if(V2<V[i|1<<j])
                V[i|1<<j]=V2;
            }
            else
            {
              M[i|1<<j]=1;
              V[i|1<<j]=V2;
            }
          }
    }
    printf("Case #%d:",c);
    if(M[(1<<n)-1])
    {
      for(i=0;i<n;i++)
        printf(" %d",V[(1<<n)-1][i]+1);
      printf("\n");
    }
    else
      printf(" IMPOSSIBLE\n");
  }
  return 0;
}
