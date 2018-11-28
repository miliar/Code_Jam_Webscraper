#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pb push_back
#define ii pair<int,int>
#define vi vector<int>
#define _(A,v) memset(A,v,sizeof(A))
#define all(A) (A).begin(),(A).end()
#define forn(i,n)for(int i=0;i<n;i++)
#define foreach(it,A) for(__typeof((A).begin())it=(A).begin();it!=(A).end();it++)
#define endl '\n'
#define dbg(xD) cerr<<" >"<<__LINE__<<": "<<#xD<<" = "<<xD<<endl
#define fast_io ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

int solve(int n){
   if(n==0)return -1;
   int mask=0,t=(1<<10)-1,m,x;
   for(int i=n;;i+=n){
      m=i;
      while(m!=0){
         x=m%10;
         m/=10;
         mask|=(1<<x);
      }
      if(mask==t)return i;
   }
}

int main(){
   freopen("A-large.in","r",stdin);
   freopen("A-large.out","w",stdout);
   int tc,n;
   scanf("%d",&tc);
   for(int i=1;i<=tc;i++){
      scanf("%d",&n);
      int ans=solve(n);
      printf("Case #%d: ",i);
      if(ans==-1)
         printf("INSOMNIA\n");
      else
         printf("%d\n",ans);
   }
   return 0;
}