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
#include<list>
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
#define mp make_pair
#define sz size()
#define eps 1e-8

const int MOD(1000000007);
const int INF((1<<30)-1);
const int MAXN(1005);

int a[MAXN],b[MAXN],dp[MAXN][MAXN],d[MAXN][MAXN];

map<int,int>p;

void solve(int test){

    int n;
    S("%d",&n);
    FOR(i,1,n)
    {
        S("%d",&a[i]);
        b[i] = a[i];
        p[a[i]] = i;
    }

    FOR(i,0,n)
        FOR(j,0,n)
            dp[i][j] = INF;

    sort(b+1,b+1+n);

    FOR(i,1,n)
    {
        int cnt = 0;

        FOR(j,1,i-1)
        {
            if(p[b[j]] < p[b[i]]) cnt++;
            d[i][j] = cnt;
            //P("%d %d %d\n",b[i],j,d[i][j]);
        }
    }

    dp[0][0] = 0;

    FOR(i,0,n)
        FOR(j,0,n)
        {
            if(i+j >= n) continue;

            int pos = i+j+1, k = d[pos][i+j];

            //P("%d %d\n",b[pos],p[b[pos]],k);

            if(k > i) k = p[b[pos]] - (k-i);
            else if(k < i) k = p[b[pos]] + (i-k);
            else k = p[b[pos]];

            //P("%d %d %d\n",i,j,dp[i][j]);

            dp[i+1][j] = min(dp[i+1][j], dp[i][j] + (k-i-1));
            dp[i][j+1] = min(dp[i][j+1], dp[i][j] + (n-j-k));
        }

    int best = INF;
    FOR(i,0,n)
    {
        //P("-> %d %d %d\n",i,n-i,dp[i][n-i]);
        best = min(best, dp[i][n-i]);
    }


    P("Case #%d: %d\n",test,best);
}

int main(){

    freopen("1input.txt","r",stdin);
    freopen("1output.txt","w",stdout);

    int t;
    S("%d",&t);
    FOR(i,1,t)
        solve(i);
}
