#include<iostream>
#include<cstdio>
#include<algorithm>
#define forn(a,b) for(int a = 0; a < int(b); ++a)
#define forr(a,c,b) for(int a = int(c); a < int(b); ++a)
using namespace std;
typedef long long ll;

int T;
ll N;

int main(){
    freopen("entrada.txt", "r", stdin);
    freopen("salida.txt", "w", stdout);

    scanf("%i", &T);
    forn(t, T){
        scanf("%lld", &N);
        if( !N ){
            printf("Case #%i: INSOMNIA\n", t+1);
            continue;
        }
        ll M = 0; int digits = 0;
        do{
            M += N;
            for(ll R = M; R; R /= 10)
                digits |= 1<<(R % 10);
        }while( digits + 1 != (1<<10) );
        printf("Case #%i: %lld\n", t+1, M);
    }

    return 0;
}
