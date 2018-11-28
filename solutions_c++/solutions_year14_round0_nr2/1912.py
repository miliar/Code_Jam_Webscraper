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

int main()
{double now,c,f,x,ans,per;
 int t,i,timu=0;
 freopen("B-large.in","r",stdin);
 freopen("ans.out","w",stdout);
 scanf("%d",&t);
 while(t--)
 {now=0.0;per=2.0;timu++;
  scanf("%lf %lf %lf",&c,&f,&x);
  ans=x/per;
  for(i=1;;i++)
  {
   now+=c/per;
   per+=f;
   if(now+x/per>ans)break;
   else ans=now+x/per;
  }
  printf("Case #%d: %.7lf\n",timu,ans);
 }

 return 0;
}
