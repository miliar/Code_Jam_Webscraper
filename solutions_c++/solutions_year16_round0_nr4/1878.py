#include <bits/stdc++.h>

using namespace std;


#define pb push_back
#define ll long long
#define mp make_pair
#define f first
#define s second
#define pii pair < int, int >
#define pll pair < ll, ll >
#define all(s) s.begin(), s.end()
#define sz(s) (int) s.size()
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it++)
#define vi vector < int >

const int inf = (int)1e9;
const int mod = (int) 1e9 + 7;

int T;
int K, C, S;

int main () {
    #ifdef LOCAL
    freopen ("a.in", "r", stdin);
    freopen ("a.out", "w", stdout);
    #endif


    scanf("%d", &T);
    for (int ii=1;ii<=T;ii++){
        scanf("%d%d%d", &K, &C, &S);
        printf("Case #%d:", ii);
        if (C == 1){
            if (S == K){
                for (int i=1;i<=K;i++){
                    printf(" %d", i);
                }
                printf("\n");
            }
            else {
                printf(" IMPOSSIBLE\n");
            }
            continue;
        }
        if ((K+1)/2 > S){
            printf(" IMPOSSIBLE\n");
            continue;            
        }
        vector < ll > ans;
        for (int i=2;i<=K;i+=2){
            ll pos = i;
            for (int j=2;j<=C;j++){
                pos = K * (pos-2) + i;
            }
            ans.pb(pos);
        }
        if (K%2 == 1){
            ll pos = 1;
            for (int j=1;j<=C;j++){
                pos *= K;
            }
            ans.pb(pos);
        }

        forit(it, ans)
            printf(" %lld", *it);
        printf("\n");
    }


    #ifdef LOCAL
    cerr << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
    #endif
    return 0;
}
