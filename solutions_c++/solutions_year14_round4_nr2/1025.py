#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <vector>
#include <map>
#include <queue>
#include <cassert>
using namespace std;
#define p(x) cerr<<#x<<":"<<x<<"\n"
int cs,c,i,n,mn,s,j;
int L[1001],R[1001],A[1001];
void f(int* M)
{
  int i,j;
  for(i=1;i<=n;i++)
    for(j=1,M[i]=M[i-1];j<i;j++)
      if(A[j]>A[i])
        M[i]++;
}
int main()
{
  scanf("%d",&cs);
  for(c=1;c<=cs;c++)
  {
    scanf("%d",&n);
    for(i=1;i<=n;i++)
      scanf("%d",&A[i]);
    //if(n!=9)
    //  continue;
    memset(L,0,sizeof L);
    memset(R,0,sizeof R);
    for(i=1;i<=n;i++)
    {
      for(j=1;j<i;j++)
        if(A[j]>A[i])
          L[i]++;
      for(j=i+1;j<=n;j++)
        if(A[j]>A[i])
          R[i]++;
    }
    /*f(L);
    reverse(A+1,A+n+1);
    f(R);
    reverse(R+1,R+n+1);*/
    mn=1000000000;
    //for(i=1;i<=n;i++)
    //  mn=min(mn,L[i]+R[i+1]);
    for(i=1;i<=n;i++)
    {
      s=0;
      for(j=1;j<=n;j++)//i;j++)
        s+=min(L[j],R[j]);//L[j];
      //for(j=i+1;j<=n;j++)
      //  s+=R[j];
      mn=min(mn,s);
    }
    printf("Case #%d: %d\n",c,mn);
    /*vector<int> V,V2;
    queue <vector<int> > Q;
    map<vector<int>,int> M;
    //reverse(A+1,A+n+1);
    for(i=1;i<=n;i++)
      V.push_back(A[i]);
    M[V]=1;
    Q.push(V);
    while(1)
    {
      V=Q.front();
      Q.pop();
      for(i=0;i+1<n && V[i]<V[i+1];i++);
      for(;i+1<n && V[i]>V[i+1];i++);
      if(i+1==n)
      {
        printf("%d\n",M[V]-1);
        p(mn);
        assert(M[V]-1==mn);
        break;
      }
      for(i=0;i+1<n;i++)
      {
        V2=V;
        swap(V2[i],V2[i+1]);
        if(!M[V2])
        {
          M[V2]=M[V]+1;
          Q.push(V2);
        }
      }
    }
    cout<<flush;
    p(c);*/
  }
	return 0;
}
