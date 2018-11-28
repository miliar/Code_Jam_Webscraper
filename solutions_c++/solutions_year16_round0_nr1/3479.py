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
const int MAXN(1000005);

int ans[MAXN];

int f(int n){

    int num = n, t, c[15] = {0};

    while(true)
    {
        t = num;

        while(t > 0)
        {
            c[t%10] = 1;
            t /= 10;
        }

        bool fail = false;

        REP(i,10)
        {
            if(!c[i])
            {
                fail = true;
                break;
            }
        }

        if(!fail) break;

        num += n;

    }

    return num;

}

void solve(int test){

    int n;
    S("%d",&n);

    if(n == 0) P("Case #%d: INSOMNIA\n",test);

    else P("Case #%d: %d\n",test,f(n));

}

int main(){

    freopen("1input.txt","r",stdin);
    freopen("1output.txt","w",stdout);

    int t;
    S("%d",&t);

    FOR(i,1,t)
        solve(i);

}
