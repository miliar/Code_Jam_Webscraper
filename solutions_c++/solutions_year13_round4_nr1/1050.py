#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cctype>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>

#define REP(i,n) for(int i=0;i<(n);i++)
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))

#define MP make_pair
#define PB push_back

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

using namespace std;

const int MOD = 1000002013;

int N, M;
map<int,int> mp;

int calc(int l, int r) {
    LL b = (LL)r - l;
    LL a = (LL)N + N - b + 1;
    if (a % 2 == 0) return a / 2 * b % MOD;
    assert(b % 2 == 0);
    return b / 2 * a % MOD;
}

void solve(int cas)
{
    printf("Case #%d: ", cas);
    cin >> N >> M;
    mp.clear();
    vector<PII> q;
    int ori = 0;
    for (int i = 1; i <= M; ++i) {
        int u, v, p;
        scanf("%d%d%d", &u, &v, &p);
        mp[u] += p;
        q.PB(MP(v, p));
        ori = (ori + 1ll * calc(u, v) * p % MOD) % MOD;
    }
    SORT(q);
    int cur = 0;
    REP(i, q.size()) {
        while (q[i].second) {
            map<int,int>::iterator it = mp.upper_bound(q[i].first);
            --it;
            int p = min(q[i].second, it->second);
            cur = (cur + 1ll * calc(it->first, q[i].first) * p % MOD) % MOD;
            q[i].second -= p;
            it->second -= p;
            if (it->second == 0) mp.erase(it);
        }
    }
    //cout << ori << "," << cur << endl;
    cout << ((LL)ori - cur + MOD) % MOD << endl;
}

int main()
{
    int T;
	//freopen("A.in","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
//	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
    scanf("%d", &T);
    for (int i=1; i<=T; ++i) solve(i);
    return 0;
}
