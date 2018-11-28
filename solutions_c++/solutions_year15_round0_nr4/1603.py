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
int x,r,c;
string solve(){
   cin>>x>>r>>c;
   bool ans=true;
   if(x>r and x>c)ans=false;
   else if(r*c%x!=0)ans=false;
   else if((x+1)/2>min(r,c))ans=false;
   else if(x!=4)ans=true;
   else if(x==4)ans=min(r,c)>2;
   return ans?"GABRIEL":"RICHARD";
}
int main(){
   //freopen("D-small-attempt1.in","r",stdin);
   //freopen("D-small-attempt1.out","w",stdout);
   FASTIO
   int tc;
   cin>>tc;
   REP(c,1,tc){
      cout<<"Case #"<<c<<": "<<solve()<<ENDL;
   }
   
   return 0;
}
/*
4
2 2 2
2 1 3
4 4 1
3 2 3

*/