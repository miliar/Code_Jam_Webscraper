#include <cstdio>
#include <algorithm>
#include <utility>
using namespace std;

#define D(x...) fprintf(stderr, x)
#define D(x...)

typedef long long ll;
typedef pair<ll,ll> pll;

const int MAX_N = 3000005;
const ll INF = (1ll << 60);

int N;
int TT;
ll D;
ll par[MAX_N];
ll sal[MAX_N];
pll valid[MAX_N];
int done[MAX_N];
ll cnt[MAX_N];

void proc(int u) {
    if(done[u] != TT && u != 0) {
        D("proc(%d)\n",u);
        done[u] = TT;
        proc(par[u]);
        if(valid[par[u]].first <= valid[par[u]].second) {
            valid[u].first = max(valid[u].first, valid[par[u]].first);
            valid[u].second = min(valid[u].second, valid[par[u]].second);
        } else {
            valid[u].first = 5;
            valid[u].second = 2;
        }
    }
}

int main() {
    int T;
    scanf("%d",&T);

    for(int z=1;z<=T;z++) {
        for(int i=0;i<MAX_N;i++) {
            cnt[i] = 0ll;
        }

        TT = z;
        scanf("%d %lld",&N,&D);

        ll A, C, R;
        scanf("%lld %lld %lld %lld",&sal[0],&A,&C,&R);
        ///D("s, a, c, r = %lld %lld %lld %lld\n",sal[0],A,C,R);
        for(int i=1;i<N;i++) {
            sal[i] = ((sal[i-1] * A + C)%R+R)%R;
            //D("sal[%d] = %lld\n",i,sal[i]);
        }

        ll p;
        scanf("%lld %lld %lld %lld",&p,&A,&C,&R);
        for(int i=1;i<N;i++) {
            p = (((p * A + C)%R+R)%R);
            par[i] = p%i;
            D("par[%d] = %lld\n",i,par[i]);
        }

        for(int i=0;i<N;i++) {
            //valid[i] = make_pair(max(0ll, sal[i]-D), min(MAX_N-2ll, sal[i]+D));
            valid[i] = make_pair(max(0ll, sal[i]-D), sal[i]);
        }

        for(int i=0;i<N;i++) {
            proc(i);
        }

        for(int i=0;i<N;i++) {
            D("valid[%d] = [%lld,%lld]\n",i,valid[i].first,valid[i].second);
            if(valid[i].first <= valid[i].second) {
                cnt[valid[i].first]++;
                cnt[valid[i].second+1]--;
            }
        }

        ll cur = 0ll;
        ll best = 0ll;
        for(int i=0;i<MAX_N;i++) {
            if(cnt[i]) {
                D("cur = %d, cnt = %lld\n",i,cnt[i]);
            }
            cur += cnt[i];
            best = max(best, cur);
        }

        printf("Case #%d: %lld\n",z,best);
    }

    return 0;
}
