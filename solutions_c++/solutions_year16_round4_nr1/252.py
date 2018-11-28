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

int N, A, B, C;

void read_data() {
    scanf("%d %d %d %d", &N, &A, &B, &C);
}

bool V[20][300];
string DP[20][300];

string rec(int level, char outcome) {
    if(level == N) {
        V[level][int(outcome)] = true;
        return DP[level][int(outcome)] = string(1, outcome);
    }
    if(V[level][int(outcome)]) {
        return DP[level][int(outcome)];
    }
    V[level][int(outcome)] = true;
    if(outcome == 'R') return DP[level][int(outcome)] = min(rec(level+1, 'R') + rec(level+1, 'S'), rec(level+1, 'S') + rec(level+1, 'R'));
    if(outcome == 'P') return DP[level][int(outcome)] = min(rec(level+1, 'P') + rec(level+1, 'R'), rec(level+1, 'R') + rec(level+1, 'P'));
    if(outcome == 'S') return DP[level][int(outcome)] = min(rec(level+1, 'S') + rec(level+1, 'P'), rec(level+1, 'P') + rec(level+1, 'S'));
    assert(false);
}

string FAIL = "ZFAILZZZ";

string ok_rec(char outcome) {
    string s = rec(0, outcome);
    map<char, int> M1, M2;
    M1['R'] = M1['S'] = M1['P'] = 0;
    for(char c: s) M1[c]++;
    M2['R'] = A;
    M2['P'] = B;
    M2['S'] = C;
    return M1 == M2 ? s : FAIL;
}

void solve() {
    FORW(i,0,20) FORW(j,0,300) DP[i][j] = FAIL;
    FORW(i,0,20) FORW(j,0,300) V[i][j] = false;
    string ret = FAIL;
    ret = min(ret, ok_rec('R'));
    ret = min(ret, ok_rec('P'));
    ret = min(ret, ok_rec('S'));
    if(ret == FAIL) {
        printf("IMPOSSIBLE\n");
    } else {
        printf("%s\n", ret.c_str());
    }

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
