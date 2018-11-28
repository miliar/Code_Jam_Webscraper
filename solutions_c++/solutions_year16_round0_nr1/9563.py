#include<iostream>
#include<cstdio>
#include<algorithm>
#define forn(a,b) for(int a = 0; a < int(b); ++a)
#define forr(a,c,b) for(int a = int(c); a < int(b); ++a)
using namespace std;
typedef long long ll;

int T;
ll caca;

int main(){
    freopen("entrada.in", "r", stdin);
    freopen("salida.txt", "w", stdout);

    scanf("%i", &T);
    forn(t, T){
        scanf("%lld", &caca);
        if( !caca ){
            printf("Case #%i: INSOMNIA\n", t+1);
            continue;
        }
        ll M = 0; int vulva = 0;
        do{
            M += caca;
            for(ll R = M; R; R /= 10)
                vulva |= 1<<(R % 10);
        }while( vulva + 1 != (1<<10) );
        printf("Case #%i: %lld\n", t+1, M);
    }

    return 0;
}
