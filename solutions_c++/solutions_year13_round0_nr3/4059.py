#include <cstdio>
#include <cstring>
#include <utility>
#include <vector>

using namespace std;

#define FILEIN "input.txt"
#define FILEOUT "output.txt"
#define TMAX 10005

typedef long long ll;

vector<ll> V;

int pal(ll x) {
    ll inv = 0;
    ll x1 = x;
    while(x != 0) {
        inv = inv * 10 + x % 10;
        x /= 10;
    }
    return (inv == x1);
}

int main() {
    freopen(FILEIN,"r",stdin);
    freopen(FILEOUT,"w",stdout);
    ll x;
    ll x2;
    int i;
    for ( i = 1; i <= 2001002; ++i){
        ll tmp = (ll)i*i;
        if(pal(i) && pal(tmp)){
            V.push_back(tmp);
        }
    }
    int T, j, count;
    ll a, b;
    scanf("%d", &T);
    for ( i = 1; i <= T; ++i) {
        scanf("%lld %lld", &a, &b);
        count = 0;
        for ( j = 0; j < V.size(); ++j) {
            if(V[j] >= a && V[j] <= b) {
                ++count;
            }
        }
        printf("Case #%d: %d\n", i, count);
    }
    return 0;
}
