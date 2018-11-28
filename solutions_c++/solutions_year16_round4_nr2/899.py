#include <bits/stdc++.h>
using namespace std;

#undef DEBUG
#ifdef DEBUG
#define D(x...) fprintf(stderr,x)
#else
#define D(x...)
#endif

#define M(x) (((x%MOD)+MOD)%MOD)

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef long double rl;

const ll MOD = (ll)(1e9)+7ll;

const int MAX_N = 205;

int N, K;
int p[MAX_N];
rl pr[MAX_N];
rl cache[MAX_N][MAX_N];
bool can[MAX_N][MAX_N*MAX_N];
int pre[MAX_N][MAX_N*MAX_N];
vector<rl> prob;

int main() {
    int T;
    scanf("%d",&T);

    for(int z=1;z<=T;z++) {
        printf("Case #%d: ",z);

//        for(int i=0;i<MAX_N;i++) {
//            for(int j=0;j<MAX_N*MAX_N;j++) {
//                can[i][j] = false;
//            }
//        }
//        can[0][0] = true;
//
        scanf("%d %d",&N,&K);
        for(int i=0;i<N;i++) {
            scanf("%Lf",&pr[i]);
            p[i] = round(pr[i]*100.0);
        }
//
//        for(int i=0;i<N;i++) {
//            for(int k=K;k>=1;k--) {
//                for(int j=100*K+5;j>=p[i];j--) {
//                    if(can[k-1][j-p[i]]) {
//                        can[k][j] = true;
//                        D("can[%d][%d] = %d\n",k,j,p[i]);
//                        pre[k][j] = i;
//                    }
//                }
//            }
//        }
//
//        int tot = K*50;
//        int work = 0;
//        for(int i=0;i<=tot;i++) {
//            for(int j=-1;j<=1;j+=2) {
//                int h = tot+i*j;
//                if(can[K][h]) {
//                    work = h;
//                    goto done;
//                }
//            }
//        }
//done:
//        prob.clear();
//        for(int kk=K;kk>0;kk--) {
//            D("kk=%d, work =%d\n",kk,work);
//            prob.push_back(pr[pre[kk][work]]);
//            D("adding %Lf\n",prob.back());
//            work -= p[pre[kk][work]];
//        }
        rl ans = 0.0;
        for(int i=0;i<(1<<N);i++) {
            if(__builtin_popcount(i) == K) {
                prob.clear();
                for(int j=0;j<N;j++) {
                    if(i & (1<<j)) {
                        prob.push_back(pr[j]);
                    }
                }

                for(int i=K;i>=0;i--) {
                    for(int k=0;k<=K/2;k++) {
                        if(i==K) {
                            if(k) {
                                cache[i][k] = 0.0;
                            } else {
                                cache[i][k] = 1.0;
                            }
                        } else {
                            cache[i][k] = 0.0;
                            rl here = (1.0 - prob[i]) * cache[i+1][k];
                            if(k) {
                                here += prob[i] * cache[i+1][k-1];
                            }
                            cache[i][k] += here;
                        }
                        D("cache[%d][%d] = %Lf [p=%Lf]\n",i,k,cache[i][k],prob[i]);
                    }
                }
                ans = max(ans, cache[0][K/2]);
            }
        }
        printf("%.9Lf\n",ans);
    }

    return 0;
}
