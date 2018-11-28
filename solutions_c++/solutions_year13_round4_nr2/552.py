#include <cstdio>
#include <cmath>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);

    for(int z = 1; z <= t; z++) {
        int n;
        long long p;
        scanf("%d %lld", &n, &p);

        if(p == (1LL<<n)) {
            printf("Case #%d: %lld %lld\n", z, (1LL<<n)-1, (1LL<<n)-1);
            continue;
        }

        p--;
        long long lo = 0, hi = (1LL<<n)-1;
        while(lo < hi) {
            long long mid = (lo+hi+1)/2;
            long long above = mid;
            long long pre_p = 0;

            for(int j = n-1; above > 0; j--) {
                pre_p |= 1LL<<j;
                above = (above-1)/2;
            }

            if(pre_p > p) hi = mid-1;
            else lo = mid;
        }
        long long guaranteed = lo;

        lo = 0, hi = (1LL<<n)-1;
        while(lo < hi) {
            long long mid = (lo+hi+1)/2;
            long long below = (1LL<<n)-mid-1;
            bool ok = false;

            for(int j = n-1; below > 0; j--) {
                below = (below-1)/2;
                if((1LL<<j)-1 <= p)
                    ok = true;
            }

            if(!ok) hi = mid-1;
            else lo = mid;
        }
        long long can = lo;

        printf("Case #%d: %lld %lld\n", z, guaranteed, can);
    }
}
