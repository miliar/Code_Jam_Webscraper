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

const int MAXN = 101010;
int N;
int K;
ldouble A[MAXN];

void read_data() {
    scanf("%d", &N);
    scanf("%d", &K);
    FOR(i,1,N) scanf("%Lf", A+i);
}

ldouble DP[202][202];

ldouble go(const vector<ldouble> &W) {
    DP[0][0] = 1;
    FOR(i,1,K) FOR(j,0,min(i, K/2)) {
        DP[i][j] = DP[i-1][j] * (1 - W[i-1]);
        if(j > 0) DP[i][j] += DP[i-1][j-1] * W[i-1];
    }
//    cout << W << " " << DP[K][K/2] << endl;
    return DP[K][K/2];
}

void solve() {
    sort(A+1, A+N+1);
    ldouble result = 0;
    FOR(i,0,K) {
        vector<ldouble> W;
        FORW(j,0,i) W.PB(A[j+1]);
        FORW(j,0,K-i) W.PB(A[N-j]);
        ldouble cand_result = go(W);
        if(cand_result > result) {
            result = cand_result;
        }
    }
    printf("%.10Lf\n", result);
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
