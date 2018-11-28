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

int a[15], K;

bool isPrime(long long p){

    FOR(i,2,p-1)
    {
        if(i*1ll*i > p) break;
        if(p%i == 0)
        {
            K = i;
            return false;
        }
    }

    return true;

}

void solve(int test){

    int n,m;
    S("%d%d",&n,&m);

    P("Case #%d:\n",test);

    int now = 0;

    REP(i,1<<(n-2))
    {
        int d = i*2;

        bool fail = false;

        FOR(j,2,10)
        {
            long long num = 0, p = 1;

            REP(k,n)
            {
                if(k == 0 || k == n-1)
                {
                    num += p;
                }

                else if(d&(1<<k))
                {
                    num += p;
                }

                p *= j;
            }

            if(isPrime(num))
            {
                fail = true;
                break;
            }

            a[j] = K;

        }

        if(!fail)
        {
            P("1");

            FORD(j,n-2,1)
            {
                if(d&(1<<j)) P("1");
                else P("0");
            }

            P("1");

            FOR(j,2,10)
                P(" %d",a[j]);
            P("\n");

            if(++now == m) break;
        }

    }

}

int main(){

    freopen("1input.txt","r",stdin);
    freopen("1output.txt","w",stdout);

    int t;
    S("%d",&t);

    FOR(i,1,t)
        solve(i);

}
