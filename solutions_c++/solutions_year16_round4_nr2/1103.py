#include<iostream>
#include<cstdio>
#include<algorithm>
#include<set>
#define forn(a,b) for(int a = 0; a < int(b); ++a)
#define forr(a,c,b) for(int a = int(c); a < int(b); ++a)
using namespace std;
typedef double ld;
const ld DELTA = 1e-6;
const int maxn = 256;

int T, N, K;
ld P[maxn], Chosen[maxn];

ld prob(int i, int A, int B){
    if( A < 0 or B < 0) return 0.0;
    if( !A and !B ) return 1.0;
    return Chosen[i] * prob(i+1, A-1, B) + (1.0 - Chosen[i]) * prob(i+1, A, B-1);
}

ld pick(int i, int j){
    if( j == K ) return prob(0, K/2, K/2);
    if( i == N ) return 0.0;
    ld ans = 0.0;
    Chosen[j] = P[i];
    ans = pick(i+1, j+1);
    ans = max( ans, pick(i+1, j));
    return ans;
}

int main(){
    freopen("small.txt", "r", stdin);
    freopen("salida.txt", "w", stdout);
    int x;
    ld p;

    scanf("%d", &T);
    forn(t, T){
        scanf("%d%d", &N, &K);
        forn(i, N)
            scanf("%lf", P+i);
        printf("Case #%i: %.12f\n", t+1, pick(0, 0));
    }

    return 0;
}
