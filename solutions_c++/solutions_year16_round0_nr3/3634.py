#include <cstdio>

typedef long long int ll;

ll finddiv(ll n) {
    for(ll d=2; d*d<=n; d++) {
        if(n%d == 0)
            return d;
    }
    return -1;
}

ll tobase(ll n, ll b) {
    if(n==0)
        return 0;
    return tobase(n/2,b)*b + (n%2);
}

void pbin(ll n) {
    if(n==0)
        return;
    pbin(n/2);
    printf("%d", n%2);
}

int solve(int N, int J) {
    int found = 0;
    
    for(ll c = (1<<(N-1))+1; found < J; c+=2) {
        bool good = true;
        ll D[11];
        for(int b = 2; b<=10; b++) {
            D[b] = finddiv(tobase(c,b));
            if(D[b]<0) {
                good = false;
            }
        }
        if(!good) continue;
        
        found++;
        pbin(c);
        for(int b = 2; b<=10; b++) {
            printf(" %lld", D[b]);
        }
        printf("\n");
    }
}

int main() {

    int T;
    scanf("%d", &T);
    for(int t=1; t<=T; t++) {
        int N, J;
        scanf("%d %d", &N, &J);
        printf("Case #%d:\n", t);
        solve(N, J);
    }
}
