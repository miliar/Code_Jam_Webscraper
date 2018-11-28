#include <bits/stdc++.h>
using namespace std;

#undef DEBUG
#ifdef DEBUG
#define D(x...) fprintf(stderr,x)
#else
#define D(x...)
#endif

#define M(x) (((x%MOD)+MOD)%MOD)

typedef pair<int,int> pii;

char buf[105];
map<int,bool> cache[100];

bool go(int N, int m) {
    if(cache[N].count(m) == 0) {
        cache[N][m] = true;
        if(m > 0) {
            for(int i=0;i<N*N;i++) {
                if((m & (1<<i))) {
                    int mm = 0;
                    for(int k=0;k<N;k++) {
                        if(k == i/N) continue;
                        int kk = k;
                        if(k > i/N) {
                            kk--;
                        }
                        for(int l=0;l<N;l++) {
                            if(l == i%N) continue;
                            int ll = l;
                            if(l > i%N) {
                                ll--;
                            }
                            if(m & (1<<(k*N+l))) {
                                mm |= (1<<(kk*(N-1)+ll));
                            }
                        }
                    }
                    D("N=%d,m=%d,i=%d,mm=%d\n",N,m,i,mm);
                    if(!go(N-1,mm)) {
                        cache[N][m] = false;
                        break;
                    }
                }
            }
        } else {
            cache[N][m] = false;
        }
    }
    return cache[N][m];
}

int main() {
    int T;
    scanf("%d",&T);

    cache[1][1] = true;
    for(int z=1;z<=T;z++) {
        printf("Case #%d: ",z);

        int N;
        scanf("%d",&N);

        int m = 0;
        for(int i=0;i<N;i++) {
            scanf(" %s ",buf);
            for(int j=0;j<N;j++) {
                if(buf[j] == '1') {
                    m |= (1 << (i*N+j));
                }
            }
        }

        int ans = (1<<29);
        for(int i=0;i<(1<<(N*N));i++) {
            if((i & m) == m && go(N, i)) {
                ans = min(ans, __builtin_popcount(i^m));
            }
        }
        printf("%d\n",ans);
    }

    return 0;
}
