#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <cstring>
#include <array>

using namespace std;

typedef unsigned long long ll;
bitset<10> digits;
ll n;

void mark() {
    ll x = n;
    while(x>0) {
        int d = x%10;
        x = x/10;
        digits.set(d);
    }
}

int main(int argc, const char * argv[]) {
    freopen(argv[1], "r", stdin);
    
    int T; scanf("%d",&T);
    for (int t = 1; t<=T; ++t) {
        ll s; scanf("%lld",&s);
        if (s==0) {printf("Case #%d: INSOMNIA\n",t); continue;}
        n = s;
        digits.reset();
        mark();
        while(!digits.all()) {
            n += s;
            mark();
        }
        printf("Case #%d: %lld\n", t, n);
    }

    return 0;
}
