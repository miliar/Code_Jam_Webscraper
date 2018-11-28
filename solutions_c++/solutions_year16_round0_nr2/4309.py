#include <cstdio>

typedef long long int ll;

#define fprintf(...)

void pbin(ll n, int N) {
    if(N==0)
        return;
    pbin(n/2,N-1);
    fprintf(stderr, "%d", n%2);
}

int flip(int x, int N) {
    if(N == 0)
        return 0;
    int r = flip(x/2,N-1) + (x%2 ? 0 : 1<<(N-1));
    pbin(x,N);
    fprintf(stderr, " -> flip(%2d) -> ", N);
    pbin(r,N);
    fprintf(stderr, "(%d -> %d)\n", x, r);
    return r;
}

int move(int x, int i, int N) {
    int r;
    if(i == N) {
        r = flip(x, N);
    } else {
        r = move(x/2,i,N-1)*2 + x%2;
    }
    
    pbin(x,N);
    fprintf(stderr, " -> move(%2d) -> ", i);
    pbin(r,N);
    fprintf(stderr, " (%d,%d,%d -> %d)\n", x, i, N, r);
    return r;
}

int solve(int N, int S) {
    fprintf(stderr, "solve(%d,%d)...\n", N, S);
    
    int moves[1 << 10];

    for(int x=0; x < (1<<10); x++) {
        moves[x] = (1 << 10) + 1;
    }

    int Qh=0, Qt=1;
    int Q[1 << 10];
    Q[0] = S;
    moves[S] = 0;
    
    while(Qh < Qt) {
        int x = Q[Qh++];
        int m = moves[x];
        for(int i = 1; i <= N; i++) {
            int y = move(x,i,N);
            if(m+1 < moves[y]) {
                moves[y] = m+1;
                Q[Qt++] = y;
            }
        }
    }
    return moves[0];
}

int main() {

    int T;
    scanf("%d ", &T);
    for(int t=1; t<=T; t++) {
        int N = 0;
        size_t len;
        char *s = NULL;
        int S = 0;
        N = getline(&s, &len, stdin) - 1;
        fprintf(stderr, "N: %d, line: %s", N, s);
        
        for(int i = 0; i < N; i++) {
            S *= 2;
            S += (s[i] == '-');
        }
        printf("Case #%d: ", t);
        printf("%d", solve(N,S));
        printf("\n");
    }
}
