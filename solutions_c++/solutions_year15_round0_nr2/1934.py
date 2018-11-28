#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<ctime>
#include<assert.h>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<limits.h>

using namespace std;

#define MAX(a,b) ((a)>(b) ? (a) : (b))
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define EPS 1e-9
#define asdf exit(0);
#define AB(a) ((a)<(0) ? (-(a)) : (a))
#define EQ(a,b) ( (fabs((a)-(b))<EPS) ? (1) : (0))



typedef long long LL;
//typedef __int64 LL;



int vals[20200];
int n;


int get(int val)
{
  int i,k,j;

  int ret=0;
  for(i=0;i<n;i++)
  {
    if(vals[i]>val)
    {
      if(vals[i]%val==0)
      {
        ret+=(vals[i]/val)-1;
      }
      else
      {
        ret+=(vals[i]/val);
      }
    }
  }
  return ret;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j,k;

    int T;
    scanf("%d",&T);
    for(int cs=1;cs<=T;cs++)
    {
       scanf("%d",&n);


       int mx=0;
       for(i=0;i<n;i++)
       {
         scanf("%d",&vals[i]);
         mx=max(mx,vals[i]);
       }

       int ans=mx;
       int temp;

       for(i=1;i<=mx;i++)
       {
         temp=i+get(i);
         ans=min(ans,temp);
       }



       printf("Case #%d: %d\n",cs,ans);
    }



    return 0;
}
