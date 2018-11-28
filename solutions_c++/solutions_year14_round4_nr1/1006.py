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
const int MAXN();

void solve(int test){

    multiset<int>s;
    multiset<int>::iterator it;

    multiset<int,greater<int> >s2;
    multiset<int,greater<int> >::iterator it2;

    int n,m;
    S("%d%d",&n,&m);
    REP(i,n)
    {
        int x;
        S("%d",&x);
        s.insert(x);
        s2.insert(x);
    }

    int ans = 0;

    while(!s.empty())
    {
        int num = *s.begin();
        s.erase(s.begin());

        it2 = s2.lower_bound(num);
        s2.erase(it2);

        it2 = s2.lower_bound(m-num);

        if(it2 != s2.end())
        {
            num = *it2;
            s2.erase(it2);

            it = s.lower_bound(num);
            s.erase(it);
        }

        ans++;
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
