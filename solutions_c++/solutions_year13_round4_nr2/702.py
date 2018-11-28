#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

#undef DEBUG
#ifdef DEBUG
#define D(x...) fprintf(stderr,x)
#else
#define D(x...)
#endif

typedef long long ll;

int R; // rounds 
ll N; // 1<<R
ll P;

ll run(ll pos, int y) {
    if(y == 0) {
        int numLoss = 0;
        for(int i=0;i<R;i++) {
            if(pos < (1ll << (i+1))-1) {
                break;
            } else {
                numLoss++;
            }
        }
        D("numLoss = %d\n",numLoss);
        return N-1ll - ((1ll << (R-numLoss)) - 1ll);
    } else {
        int numWin = 0;
        for(int i=0;i<R;i++) {
            if(pos > N - (1ll << (i+1))) {
                break;
            } else {
                numWin++;
            }
        }
        D("numWin = %d\n",numWin);
        return (1ll << (R-numWin))-1ll;
    }
}

int main() {
    int T;
    scanf("%d",&T);

    for(int z=1;z<=T;z++) {
        scanf("%d %lld",&R,&P);
        N = (1ll << R);

        ll bestGuar = 0ll;
        ll bestChance = 0ll;

        for(int y=0;y<2;y++) {
            D("* y = %d\n",y);
            ll lo = 0ll;
            ll hi = N-1ll;

            while(lo <= hi) {
                ll mid = (lo+hi)/2ll;

                ll pos = run(mid, y);
                D("[%lld..%lld], mid=%lld, pos = %lld\n",lo,hi,mid,pos);

                if(pos < P) {
                    D("YAY\n");
                    if(y == 0) {
                        bestGuar = max(bestGuar, mid);
                    } else {
                        bestChance = max(bestChance, mid);
                    }
                    lo = mid + 1ll;
                } else {
                    hi = mid - 1ll;
                }
            }
        }

        printf("Case #%d: %lld %lld\n",z, bestGuar, bestChance);
    }

    return 0;
}

