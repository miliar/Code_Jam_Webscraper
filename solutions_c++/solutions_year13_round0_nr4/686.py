#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <memory.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

#define pb push_back
#define mp make_pair
#define sz(a) int((a).size())
#define forn(i, n) for (int i=0; i<(n); ++i)

typedef map<int,int> state;

int f[1<<20];
state a[32];
int t[32];
state s;
int n;

void add(state& a, const state& b) {
    state::const_iterator it;
    for (it=b.begin(); it!=b.end(); ++it)
        a[it->first] += it->second;
}

state get_cur(int m) {
    state cur = s;
    forn (i, n) if (m&(1<<i)) {
        cur[t[i]]--;
        add(cur, a[i]);
    }
    return cur;
}

void print(int m, state& s) {
  printf("["); forn (i, n) if (m&(1<<i)) printf("%d", i); printf("] ");
  state::iterator it;
  for (it=s.begin(); it!=s.end(); ++it)
      if (it->second > 0) printf("%d:%d ", it->first, it->second);
  puts("");
  fflush(stdout);
}


int func(int m) {
    if (m == (1<<n)-1) return 1;
    int& res = f[m];
    if (res != -1) return res;
    res = 0;
    state cur = get_cur(m);
   // print(m, cur);
    forn (i, n) if (~m&(1<<i)) if (cur[t[i]] > 0) {
        if (func(m|(1<<i))) return res = 1;
    }
    return res;
}

state read(int k) {
    state res;
    forn (i, k) {
        int x; cin >> x;
        res[x]++;
    }
    return res;
}



int main()
{
    freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);

    int tc; scanf("%d", &tc);
    for (int tt=1; tt<=tc; ++tt) {
        int k;
        scanf("%d %d", &k, &n);
        s = read(k);
        forn (i, n) {
            scanf("%d %d", t+i, &k);
            a[i] = read(k);
        }
        memset(f, 0xff, sizeof(f));
        if (!func(0)) {
            printf("Case #%d: IMPOSSIBLE\n", tt);
            continue;
        }
        vector<int> ans;
        int m = 0;
        for (;;) {
            if (m == (1<<n)-1) break;
            
            state cur = get_cur(m);
            forn (i, (1<<n)) if (~m&(1<<i)) if (cur[t[i]] > 0) {
                if (func(m|(1<<i))) {
                    ans.pb(i+1);
                    m |= 1<<i;
                    break;
                }
            }
        }
        printf("Case #%d:", tt);
        forn (i, sz(ans)) printf(" %d", ans[i]);
        puts("");
    }

    return 0;
}
