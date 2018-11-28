#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define forn(i,a,b) for( int i = (a); i < (b); i++ )
#define rep(i,n) forn(i,0,n)
#define repe(i,n) for( i = 0; i < (n); i++ )
#define pii pair<int,int>
#define pdd pair<double,double>
#define pll pair<ll,ll>

const int MXN = 110;
const int MXK = 20;

int getb( int a, int i ){
    return bool(a & (1<<i));
}

int divs [11];

bool check( int n ){
    forn(base, 2, 11 ){
        ll res = 0;
        ll pw = 1;
        rep(i,16){
            res *= base;
            res += getb(n,15-i);
        }
        bool heh = false;
        for( ll i = 2; i*i <= res; i++ ){
            if(res%i==0){
                heh = true;
                divs[base] = i;
                break;
            }
        }
        if(!heh) return false;
      //  printf("%lld %lld %lld\n", res, res%2, res%3);
    }


    return true;
}

int main() {
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

    int q = 0;

    forn(i,1<<15,1<<16){
        //q++;
        if(i%2==0) continue;

        if(check(i)){
            rep(j,16){
                printf("%d", getb(i,15-j));
            }
        forn(i,2,11)
            printf(" %d", divs[i]);
            printf("\n");
        }
        //if( (q&1023)==0 ) printf("cnt %d\n", q/1024);
    }

    //check(4095);


    return 0;
}
