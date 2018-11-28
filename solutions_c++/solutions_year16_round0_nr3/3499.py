#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#define log(...) fprintf(stderr, __VA_ARGS__)
using namespace std;
typedef long long ll;

ll bases[11];
ll add[11][14];

ll notprime(ll x) {
    if ( x % 2 == 0 ) return 2;
    for ( ll i = 3; i * i <= x; i+= 2 ) {
        if ( x % i == 0 ) 
            return i;
    }
    return -1;
}

int main() {
    
    int N, J, T;
    scanf("%d %d %d", &T, &N, &J);
    printf("Case #1:\n");
    for ( int i = 2; i <= 10; i++ ) {
        bases[i] = 1;
        for ( int j = 0; j < N-1; j++ ) 
            bases[i] *= i;
        bases[i] += 1;
        ll b = 1;
        for ( int j = 0; j < 14; j++ ) {
            b *= i;
            add[i][j] = b;
        }
    }
    int cnt = 0;
    ll mask = 0;
    while ( cnt < J ) {
        vector<ll> d;
        //log("Trying: %s\n", s.c_str());
        for ( int i = 2; i <= 10; i++ ) {
            ll val = bases[i];
            ll m = mask;
            for ( int j = 0; j < N-2 && m; j++, m>>=1 ) {
                if ( m & 1 ) val += add[i][j];
            }
            ll p = notprime(val);
            //log("\tBase %d: %lld (%s)\n", i, val, p == -1 ? "prime":"not prime");
            if ( p == -1 ) break;
            d.push_back(p);
        }
        if ( d.size() == 9 ) {
            string s = "1";
            for ( int i = N-3; i >= 0; i-- ) {
                s.push_back((mask & (1<<i)) ? '1' : '0');
            }
            s.push_back('1');    
            printf("%s", s.c_str());
            for ( int i = 0; i < d.size(); i++ ) {
                printf(" %lld", d[i]);
            }
            putchar('\n');
            cnt++;
        }
        mask++;
    }
    return 0;
}
