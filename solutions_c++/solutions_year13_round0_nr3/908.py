#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>

typedef long long ll;

using namespace std;

bool is_p(ll x) {
    vector<int> a, b;
    for(;x; x /= 10) a.push_back(x % 10);

    b = a;
    reverse(b.begin(), b.end());
    return a == b;
}

vector< ll > v;
ll           a, b;

int main() {

    int tc;
    
    for(int i=1; i<=10000000; ++i) 
        if (is_p(i) && is_p((ll)i*i) ) {
            printf("%i\n", i);
            v.push_back( i );
        }
    
    freopen("C-large-1.in", "r", stdin);
    freopen("C-large-1.out", "w", stdout);

    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt) {
        scanf("%I64d %I64d", &a, &b);        
        //printf("%I64d %I64d\n", a, b);
        int cnt = 0;
        for(int i=0; i<v.size(); ++i) if ( a <= v[i]*v[i] && v[i]*v[i] <= b) cnt++;
        printf("Case #%i: %i\n", tt, cnt);
    }
}