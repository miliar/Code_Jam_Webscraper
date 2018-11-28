#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pb push_back
#define ff first
#define ss second
#define ii pair<int,int>
#define vi vector<int>
#define vvi vector<vi>
#define vii vector<ii>
#define vvii vector<vii>
#define _(A,v) memset(A,v,sizeof(A))
#define sz(c) (int)(c).size()
#define ALL(A) (A).begin(),(A).end()
#define INF 1000000000
#define FOR(i,a,b)for(int i=int(a);i<int(b);i++)
#define ROF(i,a,b)for(int i=int(a)-1;i>=int(b);i--)
#define REP(i,a,b)for(int i=int(a);i<=int(b);i++)
#define PER(i,a,b)for(int i=int(a);i>=int(b);i--)
#define FORN(i,n)FOR(i,0,n)
#define DBG(xD) cout<<__LINE__<<": "<<#xD<<" = "<<xD<<ENDL
#define FOREACH(it,A) for(__typeof((A).begin())it=(A).begin();it!=(A).end();it++)
#define FASTIO ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define ENDL '\n'
int solve(){
   int n,ans=0;
   string s;
   cin>>n>>s;
   int sum=(s[0]-'0');
   for(int i=1;i<=n;i++){
      if(i>sum){
         ans+=(i-sum);
         sum+=(i-sum);
      }
      sum+=(s[i]-'0');
   }
   return ans;
}
int main(){
   //freopen("A-large.in","r",stdin);
   //freopen("A-large.out","w",stdout);
   
   int tc;
   cin>>tc;
   REP(c,1,tc){
      printf("Case #%d: %d\n",c,solve());
   }
   
   return 0;
}
