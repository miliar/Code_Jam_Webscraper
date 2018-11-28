#include <cstdio>
#include <utility>
#include <algorithm>
using namespace std;

#define D(x...) fprintf(stderr, x)

typedef long long ll;
typedef pair<ll,ll> pll;

const int MAX_N = 40005;

int N, K;
ll vals[MAX_N];
ll delta[MAX_N];
ll mnv[MAX_N];
ll mxv[MAX_N];

int main() {
    int T;
    scanf("%d",&T);

    for(int z=1;z<=T;z++) {
        scanf("%d %d",&N,&K);

        for(int i=0;i<K;i++) {
            mnv[i] = 0ll;
            mxv[i] = 0ll;
        }

        for(int i=0;i<N-K+1;i++) {
            scanf("%lld",&vals[i]);
        }

        ll lo = 0;
        for(int i=0;i<K;i++) {
            delta[i] = 0;
            for(int j=i+1;j<N-K+1;j+=K) {
                delta[j+K-1] = vals[j] - vals[j-1] + delta[j-1];
                mnv[i] = min(mnv[i], delta[j+K-1]);
                mxv[i] = max(mxv[i], delta[j+K-1]);
            }
            lo = max(lo, mxv[i]-mnv[i]);
        }

        ll bot = 0ll;
        ll freedom = 0ll;
        for(int i=0;i<K;i++) {
            bot += -mnv[i];
            freedom += lo-mxv[i]+mnv[i];
        }

        ll target = ((vals[0]%K)+K)%K;
        ll diff = (((target-bot)%K)+K)%K;
        ll best;
        if(diff <= freedom) {
            best = lo;
        } else {
            best = lo+1ll;
        }

        printf("Case #%d: %lld\n",z,best);
    }

    return 0;
}
