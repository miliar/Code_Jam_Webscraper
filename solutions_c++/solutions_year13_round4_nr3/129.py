#include <stdio.h>
#include <ctype.h>
#include <iostream>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <time.h>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <assert.h>

//#define M_PI 3.141592653589793238462643
#define eps 1e-8
#define inf ((int)1e9)
#define pb push_back
#define mp make_pair

using namespace std;

int A[2100], B[2100];
//vector <int> VA[2100], VB[2100];
int LA[25][25];
int P[25][25];
int Cur[25], n;

bool gen (int v)
{
  if (v==n)
  {
    //cerr<<"!!!! "<<endl;
    bool fl=1;
    int i, j, it;
    for (it=0; it<2; it++)
    {
      //cerr<<it<<"   "<<n<<endl;
      memset(Cur,0,sizeof(Cur));
      for (i=0; i<n; i++)
        for (Cur[i]=1, j=0; j<i; j++)
          if (P[n][i]>P[n][j])
            Cur[i]=max(Cur[i],Cur[j]+1);
      //cerr<<"TTTT"<<endl;
      for (i=0; i<n; i++)
      {
        if (it==0 && A[i]!=Cur[i])
          fl=0;
        if (it==1 && B[n-i-1]!=Cur[i])
          fl=0;
      }
      reverse(P[n],P[n]+n);
    }
    //cerr<<"??? "<<endl;
    return fl;
  }
  int lb=0, rb=v, j;
  for (j=0; j<v; j++)
  {
    if (A[j]>=A[v])
      rb=min(rb,P[v][j]);
    if (B[j]<=B[v])
      lb=max(lb,P[v][j]+1);
  }
  if (A[v]>1)
    lb=max(lb,LA[v][A[v]-1]+1);
  while (rb>=lb)
  {
    P[v+1][v]=rb;
    for (j=0; j<v; j++)
    {
      P[v+1][j]=P[v][j];
      if (P[v][j]>=P[v+1][v])
        P[v+1][j]++;
      LA[v+1][A[j]]=P[v+1][j];
    }
    LA[v+1][A[v]]=P[v+1][v], rb--;
    if (gen(v+1))  
      return 1;
  }
  return 0;
}

int main()
{
  int tst, cnt, i;
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  scanf("%d", &tst);
  for (cnt=1; cnt<=tst; cnt++)
  {
    cerr<<cnt<<endl;
    printf("Case #%d:", cnt);
    scanf("%d", &n);
    for (i=0; i<n; i++)
      scanf("%d", &A[i]);
    for (i=0; i<n; i++)
      scanf("%d", &B[i]);
    assert(gen(0));
    for (i=0; i<n; i++)
      printf(" %d", P[n][i]+1);
    printf("\n"); 
  }
  return 0;
}
