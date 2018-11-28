#include <cstdio>

const int MAX_T = 100;
const int MAX_N = 1000000;

typedef long long ll;

int T, N;
int A[15];

int counted_all(){
    for(int i=0; i<10; i++){
        if(A[i] == 0) return 0;
    }
    return 1;
}

void solve(){
    if(N == 0){
        printf("INSOMNIA");
        return;
    }
    for(int i=0; i<10; i++) A[i] = 0;
    int i;
    for(i=1; !counted_all(); i++){
        ll x = ll(i) * ll(N);
        while(x > 0){
            A[x%10] = 1;
            x /= 10;
        }
    }
    printf("%lld", ll(N) * ll(i-1));
}

int main(){
    scanf("%d", &T);
    for(int i=1; i<=T; i++){
        scanf("%d", &N);
        printf("Case #%d: ", i);
        solve();
        printf("\n");
    }
    return 0;
}
