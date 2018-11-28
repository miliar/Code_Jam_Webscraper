#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
//#include<cctype>
#include<climits>
#include<iostream>
#include<string>
#include<vector>
#include<map>
//#include<list>
#include<queue>
#include<deque>
#include<algorithm>
//#include<numeric>
#include<utility>
//#include<memory>
#include<functional>
#include<cassert>
#include<set>
#include<stack>
#include<random>

const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, -1, 0, 1};
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int, int> pii;

struct UnionFind {
    vector<int> par;
    int n, cnt;
    UnionFind(const int& x = 0) {init(x);}
    void init(const int& x) {par.assign(cnt=n=x, -1);}
    inline int find(const int& x) {return par[x] < 0 ? x : par[x] = find(par[x]);}
    inline bool same(const int& x, const int& y) {return find(x) == find(y);}
    inline bool unite(int x, int y) {
        if ((x = find(x)) == (y = find(y))) return false;
        --cnt;
        if (par[x] > par[y]) swap(x, y);
        par[x] += par[y];
        par[y] = x;
        return true;
    }
    inline int count() const {return cnt;}
    inline int count(int x) {return -par[find(x)];}
};

const int MAXN = 1111;
int X[MAXN], Y[MAXN], Z[MAXN];
int Vx[MAXN], Vy[MAXN], Vz[MAXN];

const double INF = 1e9;
double dp[MAXN], d[MAXN][MAXN];

inline int square(int x) {return x*x;}

void solve() {
    int N, S;
    cin >> N >> S;
    for (int i = 0; i < N; i++) {
        cin >> X[i] >> Y[i] >> Z[i] >> Vx[i] >> Vy[i] >> Vz[i];
    }
    for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) {
        d[i][j] = sqrt(square(X[i]-X[j]) + square(Y[i]-Y[j]) + square(Z[i]-Z[j]));
    }
    double low = 0, high = INF;
    for (int i = 0; i < 100; i++) {
        const double med = (low+high)/2;
        UnionFind uf(N);
        for (int j = 0; j < N; j++) for (int k = j+1; k < N; k++) {
            if (d[j][k] < med) uf.unite(j, k);
        }
        if (uf.same(0, 1)) high = med;
        else low = med;
    }
    printf("%.10lf\n", high);
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": " ;
        solve();
    }
    return 0;
}
