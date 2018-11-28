#include <cstdio>

using namespace std;
#define ll long long
    
ll getBest(int n, ll poz) {
    
    ll new_below;
    if(poz == 0) 
        new_below = 0;
    else new_below = (poz >> 1) + poz % 2;
    
    if(poz == (1LL << n) - 1) {
        return (1LL << n);
    }

    return getBest(n - 1, new_below);
}

ll getWorst(int n, ll poz) {
    
    ll new_below;
    if(poz == 0)
        return 1;

    new_below = ((poz - 1) >> 1);

    return (1LL << (n - 1)) + getWorst(n - 1, new_below);
}

int main() {
    
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    
    int t; scanf("%d",&t);

    for(int t_case = 1; t_case <= t; ++t_case) {
        int n; ll p; scanf("%d %lld",&n,&p);
    
        ll firstans = 0, secondans = 0;
    
        for(ll step = (1LL << (n - 1)); step > 0; step >>= 1)
            if(getBest(n, firstans + step) <= p)
                firstans += step;
        
        for(ll step = (1LL << (n - 1)); step > 0; step >>= 1)
            if(getWorst(n, secondans + step) <= p)
                secondans += step;

        printf("Case #%d: %lld %lld\n", t_case, secondans, firstans);
    }

    return 0;
}   
