#include <stdio.h>

int N=16, J=50;

int state[35];

int ptr=1;

long long isnotPrime(long long x){
    //printf("%lld\n", x);
    for(long long i=2; i*i <= x; i++){
        if(x%i == 0) return i;
    }
    return 0;
}

void check(){
    if(ptr > J) return;
    for(int base=2; base<=10; base++){
        long long cur = 1;
        long long sum = 0;
        for(int i=1; i<=N; i++){
            if(state[i]) sum += cur;
            cur *= base;
        }
        if(!isnotPrime(sum)) return;
    }
    for(int i=N; i>=1; i--) printf("%d", state[i]);
    for(int base=2; base<=10; base++){
        long long cur = 1;
        long long sum = 0;
        for(int i=1; i<=N; i++){
            if(state[i]) sum += cur;
            cur *= base;
        }
        printf(" %lld", isnotPrime(sum));
    }
    printf("\n");
    ptr++;
    return;
}

void solve(int n){
    if(ptr > J) return;
    if(n == N){
        check();
        return;
    }
    state[n] = 1;
    solve(n+1);
    state[n] = 0;
    solve(n+1);
    return;
}

int main(){
    printf("Case #1: \n");
    state[1] = 1;
    state[N] = 1;
    solve(2);
}