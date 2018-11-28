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

int f[1010], a[11];
pair<int, int> p[1050];


void solve()
{
    int n;
    cin >> n;
    REP(i,n)cin>>f[i];
    REP(i,n)--f[i];

    int mx = 1 << n;
    REP(i,mx)
    {
        int bc = 0, m = i;
        while(m)++bc,m&=m-1;

        p[i].first = bc;
        p[i].second = i;
    }

    sort(p,p+mx);
    reverse(p,p+mx);

    REP(t,mx)
    {
        int sz = 0, mask = p[t].second;
        REP(i,n)if(mask&(1<<i))a[sz++]=i;

        sort(a,a+sz);
        do
        {
            char ok = 1;

            REP(i,sz)
            {
                int prev = (sz+i-1)%sz, next = (i+1)%sz;
                if (f[a[i]] != a[prev] && f[a[i]]!=a[next])
                {
                    ok=0;
                    break;
                }
            }

            if(ok)
            {
                cout << sz << endl;
                return;
            }
        }
        while (next_permutation(a,a+sz));
    }
}


int main()
{
    //freopen("../input.txt", "r", stdin);
    freopen("../data/C-small-attempt0.in", "r", stdin);
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
