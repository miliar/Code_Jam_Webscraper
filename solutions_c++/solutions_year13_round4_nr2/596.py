#include <cstdio>

typedef unsigned long long ull;

ull largest_can_win(int n, ull p) {
    if (p==0)return -1;
    if (p==(1ULL<<n))return (1ULL<<n)-1;
    if (p > (1ULL<<(n-1))) return (1ULL<<n)-2;
    // in the next pool, we know that the ith largest person can win
    // that means we want to send the greatest ith person possible
    // we have to send 0, so we may as well kill 1, can't hurt.
    // we have to send 2, so we may as well kill 3, can't hurt.
    // etc.
    // so the next pool contains 0,2,4,...
    return largest_can_win(n-1,p) << 1;
}

int main() {
    int cases;
    scanf("%d",&cases);
    for(int nocases=1;nocases<=cases;nocases++) {
        printf("Case #%d: ",nocases);

        int n;
        long long aoeu;
        scanf("%d %lld",&n,&aoeu);
        ull p=aoeu;

        // 0 == 2**n-1, 1 == 2**n-1-1, 2 == 2**n-1-2 etc. in an isomorphic game
        // where we want to lose everything.
        ull smallest_can_lose=(1ULL<<n)-1-largest_can_win(n,(1ULL<<n)-p);
        printf("%lld ", (long long)(smallest_can_lose-1));
        printf("%lld\n", (long long)largest_can_win(n,p));
    }
    return 0;
}
