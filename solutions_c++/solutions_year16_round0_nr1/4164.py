#include <iostream>
#include <cstdio>
#include <cstring>

#define ll long long
#define rep(i, j, k) for(int i = j; i < k; ++i)
using namespace std;

const int N = 1e6+1;

ll s[N];
bool dg[10];

void init() {
    memset(s, -1, sizeof s);
    rep(i, 1, N) {
//int i = 11;
        ll v = (ll)i, k; bool f = 0;
        memset(dg, 0, sizeof dg);
        int cnt = 0;
        rep(j, 1, 100000) {
            k = v * j;
            while(k) {
                if(dg[k%10] == 0) ++cnt, dg[k%10] = 1; k /= 10;
            }
//        printf("k: %lld  j:%d\n", k, j);
//        rep(q, 0, 10) printf("%d ", dg[q]); puts("");
            if(cnt == 10) {
                s[i] = j*v; f = 1;
                break;
            }
        }
        if(f == 0) s[i] = -1;
    }
    //rep(i, 0, N)  printf("%d %lld\n", i, s[i]);
}

int main()
{
    #ifdef PIT
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    #endif // PIT
    init();

    int T;
    scanf("%d", &T);
    int ic = 1;
    int n;
    while(T--) {
        scanf("%d", &n);
        if(s[n] == -1)  printf("Case #%d: INSOMNIA\n", ic++);
        else printf("Case #%d: %lld\n", ic++, s[n]);
    }

    return 0;
}
