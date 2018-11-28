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
int sum(int p[],int m,int n){
   int ans=0;
   FORN(i,n)
      ans+=((p[i]-1)/m);
   return ans;
}

int solve(){
   int d,p[1005];
   cin>>d;
   FORN(i,d)cin>>p[i];
   int ans=0;
   FORN(i,d)ans=max(ans,p[i]);
   int m=2;
   while(m<ans){
      int sum=0;
      FORN(i,d)sum+=((p[i]-1)/m);
      ans=min(ans,sum+m);
      m++;
   }
   return ans;
}

int main(){
   //freopen("B-large.in","r",stdin);
   //freopen("B-large.out","w",stdout);
   FASTIO
   int tc;
   cin>>tc;
   REP(c,1,tc){
      cout<<"Case #"<<c<<": "<<solve()<<ENDL;
   }
   
   return 0;
}
/*
1
5
1 2 3 4 5

3
1
3
4
1 2 1 2
1
4

*/