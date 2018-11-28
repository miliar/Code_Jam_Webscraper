#include <cstdio>
#include <algorithm>
#define inf 1000000000

using namespace std;

int T,n,p[1024],sol,d;

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&T);
    for (int t=1; t<=T; t++) {
        scanf("%d",&n);
        for (int i=1; i<=n; i++) scanf("%d",&p[i]);
        sol=inf;
        for (int g=1; g<=1000; g++) {
            d=0;
            for (int i=1; i<=n; i++) d+=p[i]/g+(p[i]%g > 0)-1;
            sol=min(sol,d+g);
        }
        printf("Case #%d: %d\n",t,sol);
    }

    return 0;
}
