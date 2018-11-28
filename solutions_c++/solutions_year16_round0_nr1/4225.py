#include <cstdio>

typedef long long int ll;

int solve(int N) {
    if(N==0)
        return -1;
    
    bool seen[10];
    for(int d=0; d<10; d++)
        seen[d] = false;
        
    for(ll i=1;; i++) {
        ll v = i*N;
        for(ll c=1; c<=v; c*=10) {
            seen[(v/c)%10] = true;
        }
        bool all = true;
        for(int d=0; d<10; d++) {
            fprintf(stderr, "%c", seen[d] ? '*' : '.');
            all = seen[d] && all;
        }
        fprintf(stderr, "\n");
        if(all)
            return v;
    }
}

int main() {

    int T;
    scanf("%d", &T);
    for(int t=1; t<=T; t++) {
        int N;
        scanf("%d", &N);
        printf("Case #%d: ", t);
        int S = solve(N);
        if(S >= 0) {
            printf("%d", S);
        } else {
            printf("INSOMNIA", S);
        }
        printf("\n");
    }
}
