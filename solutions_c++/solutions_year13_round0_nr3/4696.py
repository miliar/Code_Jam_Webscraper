#include <cstdio>

#define ll __int64

int N;
ll FS[100];

bool fair(ll x) {
    ll newx = 0, aux = x;
    
    while (aux) {
        newx = 1LL * newx * 10 + aux % 10;
        aux /= 10;
    }
    
    if (newx == x)
        return true;
    return false;
}

void fair_and_square() {
    for (ll i = 1; i <= 10000000; i++)
        if (fair(i) && fair(1LL * i * i))
            FS[++N] = 1LL * i * i;
            
/*    printf("%d\n", N);
    for (int i = 1; i <= N; i++)
        printf("%I64d\n", FS[i]);*/
}

int main() {
    
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    
    fair_and_square();
    
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ", i);
        ll A, B;
        scanf("%I64d %I64d", &A, &B);
        
        int cnt = 0;
        for (int j = 1; j <= N; j++)
            if (A <= FS[j] && FS[j] <= B)  
                cnt++;
                
        printf("%d\n", cnt);
    }
    
    return 0;    
}
