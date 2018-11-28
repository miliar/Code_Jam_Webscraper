#include<iostream>
#include<cstdlib>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<ctime>
#include<algorithm>
#include<list>
#include<queue>
#include<stack>
#include<vector>
#include<set>
#include<map>
#include<string>
#define REP(it,end) for (int it = 1; it <= (end); it++)
#define FOR(it,begin,end) for (int it = (begin); it <= (end); it++)
#define ROF(it,begin,end) for (int it = (begin); it >= (end); it--)
using namespace std;

double noi[1002],ken[1002];

int main()
{int t,n,i,timu=0,x,y,nf,ne,kf,ke;
 freopen("D-large.in","r",stdin);
 freopen("ans.out","w",stdout);
 scanf("%d",&t);
 while(t--)
 {timu++;
  x=y=0;
  scanf("%d",&n);
  for(i=0;i<n;i++)scanf("%lf",&noi[i]);
  for(i=0;i<n;i++)scanf("%lf",&ken[i]);
  sort(noi,noi+n);sort(ken,ken+n);
  //for(i=0;i<n;i++)cout <<noi[i]<<" ";cout <<endl;for(i=0;i<n;i++)cout <<ken[i]<<" ";cout <<endl;
  nf=kf=0;
  ne=ke=n-1;
  while(nf<=ne)
  {if(noi[nf]>ken[kf]){x++;nf++;kf++;}
   else {nf++;ke--;}
  }
  nf=kf=0;
  ne=ke=n-1;
  y=n;
  while(nf<=ne)
  {
   if(ken[ke]>noi[ne]){y--;ke--;ne--;}
   else {kf++;ne--;}
  }
  printf("Case #%d: %d %d\n",timu,x,y);
 }
 return 0;
}
