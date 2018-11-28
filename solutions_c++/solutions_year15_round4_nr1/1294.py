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
const int MAXN(105);

string a[MAXN];

int row[MAXN], col[MAXN], d[4][2] = {-1,0,0,1,1,0,0,-1};

void solve(int test){

    int n,m;
    S("%d%d",&n,&m);
    REP(i,n)
        cin >> a[i];

    REP(i,n)
        row[i] = 0;
    REP(j,m)
        col[j] = 0;

    REP(i,n)
        REP(j,m)
        {
            if(a[i][j] != '.')
            {
                row[i]++;
                col[j]++;
            }
        }

    int ans = 0;

    REP(i,n)
        REP(j,m)
        {
            if(a[i][j] == '.') continue;

            int k = 0;

            if(a[i][j] == '^') k = 0;
            else if(a[i][j] == '>') k = 1;
            else if(a[i][j] == 'v') k = 2;
            else k = 3;

            int x = i, y = j;

            x += d[k][0];
            y += d[k][1];

            bool bad = true;

            while(x >= 0 && x < n && y >= 0 && y < m)
            {
                if(a[x][y] != '.')
                {
                    bad = false;
                    break;
                }
                x += d[k][0];
                y += d[k][1];
            }

            if(bad)
            {
                ans++;
                if(row[i] == 1 && col[j] == 1)
                {
                    P("Case #%d: IMPOSSIBLE\n",test);
                    return;
                }
            }
        }

    P("Case #%d: %d\n",test,ans);
}

int main(){

    freopen("1input.txt","r",stdin);
    freopen("1output.txt","w",stdout);

    int t;
    S("%d",&t);
    FOR(i,1,t)
        solve(i);

}
