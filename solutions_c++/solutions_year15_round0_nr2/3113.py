#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <map>
#include <string>
using namespace std;
const int MAXN=1000+10;
int cnt[MAXN],maxx;
int jd(int i)
{
   int c=0;
   for(int x=i+1;x<=maxx;x++)
   {
      c+=cnt[x]*(x/i-1+(x%i?1:0));

   }
   return c;
}
int main()
{
//   freopen("in.txt","r",stdin);
//   freopen("out.txt","w",stdout);
    int t,kcase=0;
    cin>>t;
    while(t--)
   {
      int D;
      memset(cnt,0,sizeof(cnt));
      cin>>D;
      int ex=0;
      maxx=0;
      for(int i=0;i<D;i++)
      {
         int x;
         scanf("%d",&x);
         cnt[x]++;
         maxx=max(maxx,x);
      }
      int ans=maxx;
      for(int i=1;i<=maxx;i++)
            ans=min(i+jd(i),ans);
      printf("Case #%d: %d\n",++kcase,ans);
   }
    return 0;
}
