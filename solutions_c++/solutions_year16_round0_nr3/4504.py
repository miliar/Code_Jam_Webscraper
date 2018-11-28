#include<bits/stdc++.h>
#define ALL(X)        X.begin(),X.end()
#define FOR(I,A,B)    for(int (I) = (A); (I) <= (B); (I)++)
#define FORW(I,A,B)   for(int (I) = (A); (I) < (B);  (I)++)
#define FORD(I,A,B)   for(int (I) = (A); (I) >= (B); (I)--)
#define CLEAR(X)      memset(X,0,sizeof(X))
#define SIZE(X)       int(X.size())
#define CONTAINS(A,X) (A.find(X) != A.end())
#define PB            push_back
#define MP            make_pair
#define X             first
#define Y             second
using namespace std;
typedef signed long long slong;
typedef long double ldouble;
const slong INF = 1000000100;
const ldouble EPS = 1e-9;

#define N 16
#define K 50

void read_data() {
}

slong divisor(slong n) {
    for(slong d = 2; d*d <= n; ++d) {
        if(n % d == 0) {
            return d;
        }
    }
    return -1;
}

vector<slong> ret;

void solve() {
    int result_size = 0;
    for(slong i = (1LL<<(N-1)) + 1; i < (1LL<<(N)); i += 2) {
        if(result_size == K) break;
        string s = bitset<N>(i).to_string();
        bool ok = true;
        ret.clear();
        FOR(b,2,10) {
            slong t = stoll(s, nullptr, b);
            slong d = divisor(t);
            if(d == -1) {
                ok = false;
                break;
            } else {
                ret.PB(d);
            }
        }
        if(ok) {
            printf("%s ", s.c_str());
            for(slong r: ret) printf("%lld ", r);
            printf("\n");
            ++result_size;
        }
    }
}

int main() {
    int z;
    scanf("%d", &z);
    FOR(test_id,1,z) {
        printf("Case #%d:\n", test_id);
        read_data();
        solve();
    }
}
