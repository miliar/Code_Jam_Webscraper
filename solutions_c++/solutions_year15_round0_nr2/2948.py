#include<bits/stdc++.h>

typedef long long ll;
typedef std::pair<int,int> PII;
typedef std::pair<ll,ll> PLL;

template<class T> inline T pr(T x) { return --x; }
template<class T> inline T nx(T x) { return ++x; }

const int maxn = 1010;
int n,a[maxn];

int main() {
    int i,j,k,t,tt,T,Test;
    scanf("%d",&Test);
    for (T=1; T<=Test; ++T) {
        scanf("%d",&n);
        for (i=1; i<=n; ++i) scanf("%d",a+i);
        std::sort(a+1,a+n+1,[](int a,int b){return a>b;});
        int ans = ~0U>>1;
        for (k=1; k<=a[1]; ++k) {
            t = 0;
            for (i=1; i<=n; ++i)
                t += (a[i]-1)/k;
            ans = std::min(ans,t+k);
        }
        printf("Case #%d: %d\n",T,ans);
    }

    return 0;
}
