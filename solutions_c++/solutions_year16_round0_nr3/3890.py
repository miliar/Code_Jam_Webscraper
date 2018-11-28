#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <math.h>
typedef long long ll;
using namespace std;
int tt;
ll isPrime(ll N) {
    if(N < 2) return 0;
    if((N == 2) || (N == 3)) return 1;
    if((N % 2) == 0) return 0;
    for(ll i = 3; ll(i) * i <= N; i += 2) {
        if(N % i == 0) return i;
    }
    return 0;
}
ll A[105]; int S[105];
ll isJam(ll N) {
    ll two = 0, three = 0, four = 0, five = 0, six = 0, seven = 0, eight = 0, nine = 0, ten = 0;
    int pos = 0;
    while(N) {
        int bit = N & 1; if(bit) {
            two = two + powl(2, pos);
            three = three + powl(3, pos);
            four = four + powl(4, pos);
            five = five + powl(5, pos);
            six = six + powl(6, pos);
            seven = seven + powl(7, pos);
            eight = eight + powl(8, pos);
            nine = nine + powl(9, pos);
            ten = ten + powl(10, pos);
        } pos++;
        N >>= 1LL;
    }
    ll p =isPrime(two); if(p) A[2] = p; else return 0;
    p =isPrime(three); if(p) A[3] = p; else return 0;
    p =isPrime(four); if(p) A[4] = p; else return 0;
    p =isPrime(five); if(p) A[5] = p; else return 0;
    p =isPrime(six); if(p) A[6] = p; else return 0;
    p =isPrime(seven); if(p) A[7] = p; else return 0;
    p =isPrime(eight); if(p) A[8] = p; else return 0;
    p =isPrime(nine); if(p) A[9] = p; else return 0;
    p =isPrime(ten); if(p) A[10] = p; else return 0;

    //int x = (isPrime(two) || isPrime(four) || isPrime(six) || isPrime(eight) || isPrime(ten));
    //return (!x);
}
ll get(int N, int J) {
    for(int i = 2; i < 11; i++) A[i] = 2;
    ll total = 1LL << (N - 2), offset = 1LL << (N - 1);
    int cnt = 0;
    for(ll i = 0; i < total; i++) {
        ll num = i << 1LL;num |= offset; num |= 1;
        if(cnt >= J) return 0;
        if(isJam(num)) {
            cnt = cnt + 1;
            int start = 0;
            while(num) S[start++] = num & 1LL, num >>= 1LL;
            for(int j = start - 1; j >= 0; j--) printf("%d", S[j]); printf(" ");
            for(int j = 2; j <= 10; j++) printf("%lld ", A[j]);
            printf("\n");
        };
    }
    return 0;
}
void solve() {
    int N, J;scanf("%d %d", &N, &J);
    printf("Case #%d:\n", tt);
    ll ans = get(N, J);
    //printf("%lld\n", ans);
}
int main() {
    int t = 1; scanf("%d", &t);
    for(tt = 1; tt <= t; tt++) solve();
}
