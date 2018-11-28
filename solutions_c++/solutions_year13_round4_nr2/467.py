#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>

#define ll long long int

using namespace std;

ll T, C=1ll;
ll P, N, n;
ll S1[2048], S2[2048];

int main() {

    for(scanf("%lld",&T);T--;) {
        scanf("%lld %lld",&N, &P);
        n = (1ll<<N);
        printf("Case #%lld: ",C++);
        if (P == n) {
            printf("%lld %lld\n",n-1,n-1);
            continue;
        }
        if (P==1) {
            printf("0 0\n");
            continue;
        }
        S1[0] = 0;
        ll atu = 2;
        for (ll i=1;i<2048;i++) {
            S1[i] = S1[i-1] + atu;
            atu *= 2;
        }
        ll k=1;
        ll soma=(1ll<<(N-k));
        S2[0] = 0;
        S2[k] = soma;
        //while (P > soma) {
        while (k < 2048) {
            k++;
            soma += (1ll<<(N-k));
            S2[k] = soma;
        }
        k = 1;
        soma = (1ll<<(N-k));
        while (P > soma) {
            k++;
            soma += (1ll<<(N-k));
        }
        printf("%lld ",S1[k-1]);

        soma = 1;
        k = 0;
        while (P > soma) {
            k++;
            soma += (1ll<<k);
        }

        printf("%lld\n", S2[k]);

    }

    return 0;
}
