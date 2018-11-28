#include <cstdio>
#include <cstring>

#define ll long long int

using namespace std;

bool tem[32];
ll T,C=1, n;

int main() {

    for(scanf("%lld",&T);T--;) {
        printf("Case #%lld: ",C++);
        scanf("%lld",&n);
        if (n==0) {
            printf("INSOMNIA\n");
            continue;
        }
        ll ntem=0, k=1;
        memset(tem,false,sizeof(tem));
        while (ntem < 10) {
            ll t = k*n;
            while (t) {
                ll d = t%10;
                if (!tem[d]) {
                    tem[d]=true;
                    ntem++;
                }
                t /= 10;
            }
            k++;
        }
        printf("%lld\n",(k-1)*n);
    }

    return 0;
}
