#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <fstream>

using namespace std;
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) (int)(a).size()
#define FOR(i,s,n) for(int i=(s);i<(n);++i)
#define REP(i,n) FOR(i,0,(n))
#define PB(x) push_back((x))
#define CLR(a,v) memset((a),(v),sizeof((a)))
typedef long long ll;

string res;
string curr;
int MXI;

bool m_less(char c1, char c2)
{
    if(c1=='P')return c2=='S';
    if(c1=='S')return c2=='R';
    if(c1=='R')return c2=='P';
    throw "XXX";
}

bool can(int i, char c, const string& s = curr)
{
    if(i%2==0)return true;
    if(s[i-1]==c)return false;

    string ss((i+1)/2, 'X');
    REP(j,SZ(ss)-1)
    {
        char c1 = s[2*j], c2=s[2*j+1];
        if(m_less(c1, c2))ss[j]=c2;
        else if(m_less(c2, c1)) ss[j]=c1;
        else return false;
    }
    ss.back()=m_less(c, s[i-1]) ? s[i-1] : c;

    return can(SZ(ss)-1, ss.back(), ss);
}

bool f(int p, int r, int s, int i)
{
    if (p && can(i, 'P'))
    {
        curr[i] = 'P';
        if (f(p-1,r,s,i+1))return true;
    }

    if (r && can(i, 'R'))
    {
        curr[i] = 'R';
        if (f(p,r-1,s,i+1))return true;
    }

    if (s && can(i, 'S'))
    {
        curr[i] = 'S';
        if (f(p,r,s-1,i+1))return true;
    }

    return i == MXI;
}



void solve()
{
    res = "IMPOSSIBLE";

    int n,r,p,s;
    cin>>n>>r>>p>>s;
    MXI=r+p+s;

    curr.assign(' ', r+p+s);

    if(f(p, r, s, 0))res=curr.substr(0, MXI);

    cout << res << endl;
}

#include <sys/resource.h>

int main()
{
//    const rlim_t kStackSize = 1024L * 1024L * 1024L;   // min stack size = 64 Mb
//    struct rlimit rl;
//    getrlimit(RLIMIT_STACK, &rl);
//    rl.rlim_cur = rl.rlim_max;
//    setrlimit(RLIMIT_STACK, &rl);
//    getrlimit(RLIMIT_STACK, &rl);


    //freopen("../input.txt", "r", stdin);
    freopen("../data/A-small-attempt0.in", "r", stdin);
    //freopen("../data/A-large.in", "r", stdin);

    freopen("../output.txt", "w+", stdout);

    int T;
    scanf("%d", &T);
    REP(i, T)
    {
        printf("Case #%d: ", i+1);
        solve();
    }

    return 0;
}
