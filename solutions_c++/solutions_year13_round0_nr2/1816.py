/*
  ------------------------- Hachiikung ---------------------------------
  ---------------------- Worrachate Bosri ------------------------------
  ------ Faculty of Computer Engineering Chulalongkorn University ------
*/
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<string>
#include<utility>
using namespace std;
#define REP(i,FN) for(int i=0;i<FN;i++)
#define FOR(i,ST,FN) for(int i=ST;i<=FN;i++)
#define FORD(i,FN,ST) for(int i=FN;i>=ST;i--)
#define FORX(i,c) for(typeof(c.begin())i=c.begin();i!=c.end();i++)
#define pause system("pause")
#define S scanf
#define P printf
#define X first
#define Y second
#define pb push_back
#define PII pair<int,int>
#define sz size()

const int MOD(1000000007);
const int INF((1<<30)-1);
const int MAXN(105);

int n,m,a[MAXN][MAXN];

bool chkrow(int i,int k){
    REP(j,m)
     if( a[i][j]>k )
      return 0;
    return 1;
}

bool chkcol(int j,int k){
    REP(i,n)
     if( a[i][j]>k )
      return 0;
    return 1;
}

int solve(){

    S("%d%d",&n,&m);
    REP(i,n)
     REP(j,m)
      S("%d",&a[i][j]);

    FOR(k,1,100)
    {
        bool ok[MAXN][MAXN]={0};

        REP(i,n)
         if( chkrow(i,k) )
         {
             REP(j,m)
              ok[i][j]=1;
         }

        REP(j,m)
         if( chkcol(j,k) )
         {
             REP(i,n)
              ok[i][j]=1;
         }

        REP(i,n)
         REP(j,m)
          if( a[i][j]<=k && !ok[i][j] )
           return 0;
    }

    return 1;
}

int main(){

    freopen("1input.txt","r",stdin);
    freopen("1output.txt","w",stdout);

    int t;
    S("%d",&t);
    FOR(i,1,t)
    {
        int x=solve();
        P("Case #%d: ",i);
        if(x==1) P("YES\n");
        else P("NO\n");
    }

}










