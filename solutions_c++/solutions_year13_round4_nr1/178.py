#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<map>
#include<queue>
using namespace std;
const int N = 1020;

const long long mod = 1000002013LL;

struct Node {
    int pos, n;
    Node () {}
    Node ( int vv, int kk ) : pos ( vv ), n ( kk ) {}
};
bool cmp ( Node a, Node b ) {
    return a.pos > b.pos;
}
struct Heap {
    Node vv[N];
    int size;
    void push ( Node a ) {
        vv[size++] = a;
        if ( size > 1 ) push_heap ( vv, vv + size, cmp );
    }
    void pop() {
        pop_heap ( vv, vv + size, cmp );
        --size;
    }
    Node top() {
        return vv[0];
    }
    void init() {
        size = 0;
    }
}H;

long long fee ( long long n, long long d ) {
    long long ret = ( ( n + ( n - d + 1 ) ) * d / 2 ) % mod;
    return ret;
}

Node start[N], end[N];
void solve() {
    int n, m;
    scanf ( "%d%d", &n, &m );
    long long total = 0;
    for ( int i = 0;i < m;++i ) {
        int s, t, p;
        scanf ( "%d%d%d", &s, &t, &p );
        start[i].pos = s, start[i].n = p;
        end[i].pos = t, end[i].n = p;
        total +=  ( fee ( n, t - s ) * p ) % mod;
        total %= mod;
    }
    sort ( start, start + m, cmp );
    sort ( end, end + m, cmp );

    H.init();
    long long cost = 0;
    for ( int i = 0, j = 0;i < m;++i ) {
        while ( j<m && end[j].pos >= start[i].pos  ) {
            H.push ( end[j] );
            ++j;
        }
        while ( start[i].n ) {
            Node top = H.top();
            H.pop();
            if ( top.n > start[i].n ) {
                cost += ( fee ( n, top.pos - start[i].pos ) * start[i].n ) % mod;
                cost %= mod;
                top.n -= start[i].n;
                H.push ( top );
                start[i].n = 0;
            } else {
                cost += ( fee ( n, top.pos - start[i].pos ) * top.n ) % mod;
                cost %= mod;
                start[i].n -= top.n;
                top.n = 0;
            }
        }
    }
    printf ( " %lld\n", ( ( total - cost ) % mod + mod ) % mod );
    return;
}

int main() {
    int T;
    scanf ( "%d", &T );
    for ( int t = 1;t <= T;++t ) {
        printf ( "Case #%d:", t );
        solve();
    }
    return 0;
}