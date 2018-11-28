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
template<typename T, typename U> ostream& operator << (ostream& os, const pair<T, U> &_p) { return os << "(" << _p.X << "," << _p.Y << ")"; }
template<typename T> ostream& operator << (ostream &os, const vector<T>& _V) { bool f = true; os << "["; for(auto v: _V) { os << (f ? "" : ",") << v; f = false; } return os << "]"; }
template<typename T> ostream& operator << (ostream &os, const set<T>& _S) { bool f = true; os << "("; for(auto s: _S) { os << (f ? "" : ",") << s; f = false; } return os << ")"; }
template<typename T, typename U> ostream& operator << (ostream &os, const map<T, U>& _M) { return os << set<pair<T, U>>(ALL(_M)); }
typedef signed long long slong;
typedef long double ldouble;
const slong INF = 1000000100;
const ldouble EPS = 1e-9;

const int MAXN = 10;
bool A[MAXN][MAXN];
char T[MAXN][MAXN];
int N;

void read_data() {
    scanf("%d", &N);
    FOR(i,1,N) scanf("%s", T[i]+1);
    FOR(i,1,N) FOR(j,1,N) A[i][j] = T[i][j] - '0';
}

bool go() {
    FOR(v,1,N) {
        set<int> S;
        FOR(u,1,N) if(A[v][u]) S.insert(u);
        set<int> Q;
        for(int u: S) FOR(w,1,N) if(A[w][u]) Q.insert(w);
        Q.erase(v);
        if(SIZE(Q) >= SIZE(S)) return false;
    }
    return true;
}

void solve() {
    int result = INF;
    FORW(m,0,1<<(N*N)) {
        int t = 0;
        bool ok = true;
        FOR(i,1,N) FOR(j,1,N) {
            if(((1<<t)&m) != 0 and A[i][j]) ok = false;
            ++t;
        }
        if(!ok) continue;
        if(__builtin_popcount(m) > result) continue;
        t = 0;
        FOR(i,1,N) FOR(j,1,N) {
            if(((1<<t)&m) != 0) {
                A[i][j] = 1;
            }
            ++t;
        }
        if(go()) {
            result = min(result, __builtin_popcount(m));
        }
        t = 0;
        FOR(i,1,N) FOR(j,1,N) {
            if(((1<<t)&m) != 0) {
                A[i][j] = 0;
            }
            ++t;
        }
    }
    printf("%d\n", result);
}

int main() {
    int z;
    scanf("%d", &z);
    FOR(_,1,z) {
        printf("Case #%d: ", _);
        read_data();
        solve();
    }
}
