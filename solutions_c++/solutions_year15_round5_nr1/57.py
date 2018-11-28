/*
 * dnkywin's template
 */
#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef stringstream ss;

#define sz(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()
#define mset(t,v) memset((t),(v),sizeof(t))
#define print(a) cout << #a << ": " << a << endl;
#define print_arr(a,n) rep(_##i, n) cout << #a << "[" << _##i << "]: " << a[_##i] << endl

#define rep(i,n) for(int i=0,_##i=(n);i<_##i;++i)
#define repr(i,n) for(int i=(n);--i>=0;)
#define rep2(i,l,r) for(int i=(l),_##i=(r);i<_##i;++i)
#define repr2(i,l,r) for(int i=(r),_##i=(l);--i>=_##i;)

#define vt(args...) vector<tuple<args>>
#define mp make_pair
#define pb push_back
#define eb emplace_back
#define em emplace

int m, n;
int d;
const int MAXN = 1048576;
int par[MAXN];
int s[MAXN];
vector<int> adj[MAXN * 2];
vector<pii> events;

void dfs(int i, int mi, int ma) {
    mi = min(mi, s[i]);
    ma = max(ma, s[i]);
    if (ma - mi <= d) {
        events.eb(ma, 1);
        events.eb(mi + d + 1, -1);
    }
    for (int child: adj[i]) dfs(child, mi, ma);
}

void solve_case(int test_case) {
    cout << "Case #" << test_case << ": ";
    /* %%% */
    ll ss, as, cs, rs, mm, am, cm, rm;
    cin >> n >> d >> ss >> as >> cs >> rs >> mm >> am >> cm >> rm;
    rep(i, n) {
        adj[i].clear();
    }
    events.clear();

    rep(i, n) {
        s[i] = ss;
        if (i) {
            par[i] = mm % i;
            adj[par[i]].pb(i);
        }
        ss = (ss * as + cs) % rs;
        mm = (mm * am + cm) % rm;
    }
    dfs(0, 1000000000, -1000000000);

    sort(all(events));
    int ans = 1;
    int tmp = 0;
    for(auto ev: events) {
        tmp += ev.second;
        ans = max(ans, tmp);
    }    
    cout << ans << "\n";
}

int main(){
    const rlim_t kStackSize = 128 * 1024 * 1024;   // min stack size = 16 MB
        struct rlimit rl;
            int result;

                result = getrlimit(RLIMIT_STACK, &rl);
                    if (result == 0)
                            {
                                        if (rl.rlim_cur < kStackSize)
                                                    {
                                                                    rl.rlim_cur = kStackSize;
                                                                                result = setrlimit(RLIMIT_STACK, &rl);
                                                                                            if (result != 0)
                                                                                                            {
                                                                                                                                fprintf(stderr, "setrlimit returned result = %d\n", result);
                                                                                                                                            }
                                                                                                    }
                                            }
    int T;
    cin >> T;
    rep(tt, T) solve_case(tt + 1);
    return 0;
}

