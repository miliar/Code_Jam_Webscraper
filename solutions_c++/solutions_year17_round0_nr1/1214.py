/*
  ------------------------- Hachiikung ---------------------------------
  ---------------------- Worrachate Bosri ------------------------------
  ------ Faculty of Computer Engineering Chulalongkorn University ------
*/
#include <bits/stdc++.h>
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
const int MAXN();

void solve(int test){

    string a;
    int k;
    cin >> a >> k;

    int ans = 0;

    REP(i,a.sz)
    {
        if(i+k-1 >= a.sz) break;

        if(a[i] == '-')
        {
            ans++;

            FOR(j,i,i+k-1)
            {
                if(a[j] == '-') a[j] = '+';
                else a[j] = '-';
            }
        }
    }

    P("Case #%d: ",test);

    REP(i,a.sz)
    {
        if(a[i] == '-')
        {
            P("IMPOSSIBLE\n");
            return;
        }
    }

    P("%d\n",ans);

}

int main(){

    freopen("1input.txt","r",stdin);
    freopen("1output.txt","w",stdout);

    int t;
    S("%d",&t);
    FOR(i,1,t)
        solve(i);

}
