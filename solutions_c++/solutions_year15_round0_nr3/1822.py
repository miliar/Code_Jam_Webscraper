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
const int MAXN(10005);

char a[MAXN];

int last[MAXN];

int b[4][4] = {1, 2, 3, 4,
               2,-1, 4,-3,
               3,-4,-1, 2,
               4, 3,-2,-1};

int num(char x){
    return x-'i'+1;
}

void solve(int test){

    int n,m;
    S("%d%d%s",&n,&m,a);

    string s = "";
    REP(i,m)
        s += a;

    int K = 1, ck = 1;

    FORD(i,n*m-1,1)
    {
        K = b[num(s[i])][K-1];

        if(K < 0)
        {
            K *= -1;
            ck *= -1;
        }

        last[i] = K*ck;
    }

    int I = 1, ci = 1;

    REP(i,n*m)
    {
        I = b[I-1][num(s[i])];

        if(I < 0)
        {
            I *= -1;
            ci *= -1;
        }

        if(I*ci == 2)
        {
            int J = 1, cj = 1;

            FOR(j,i+1,n*m-2)
            {
                J = b[J-1][num(s[j])];

                if(J < 0)
                {
                    J *= -1;
                    cj *= -1;
                }

                if(J*cj == 3 && last[j+1] == 4)
                {
                    P("Case #%d: YES\n",test);
                    return;
                }
            }
        }
    }

    P("Case #%d: NO\n",test);
}

int main(){

    freopen("1input.txt","r",stdin);
    freopen("1output.txt","w",stdout);

    int t;
    S("%d",&t);
    FOR(i,1,t)
        solve(i);

}
