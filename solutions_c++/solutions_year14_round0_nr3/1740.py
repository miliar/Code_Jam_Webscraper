#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <ctime>
using namespace std;
#define FOR(i,a,b) for(int i=a; i<=b; i++)
#define REP(i,a,b) for(int i=a; i>=b; i--)
#define FORAD(i,u) for(int i=0; i < (int)u.size(),i++)
#define BUG(x) cout << x << endl
#define ll long long
#define fi first
#define sd second
#define pb push_back
#define two(i) 1 << i
#define sz(x) (int)x.size()
#define e 1e-12
#define bit(s,i) ((s >> (i-1)) & 1)
#define Nmax 100100
const double pi = acos(-1);
typedef vector<int> vi ;
typedef pair<int,int> pii ;

int R, C, M, SL ;
int a[100][100], d[100][100], dd[100][100], b[100][100];
bool ok;

void BFS(int i, int j) {
    SL++;
    dd[i][j] = 1;
    if (d[i][j] == 1) return;
    FOR(u, max(1,i-1), min(R,i+1))
    FOR(v, max(1,j-1), min(C,j+1)) if (dd[u][v] == 0)
    BFS(u, v);
}

void check() {

    FOR(i, 1, R) FOR(j, 1, C) {
        d[i][j] = 0;
        dd[i][j] = a[i][j];
    }
    SL = 0;
    FOR(i, 1, R) FOR(j, 1, C) if (a[i][j] == 1) {
        FOR(u, max(1,i-1), min(R,i+1))
        FOR(v, max(1,j-1), min(C,j+1)) d[u][v] = 1;
    }
    //FOR(i, 1, 2) FOR(j, 1, 2) cout << d[i][j] ; cout << endl;
    FOR(i, 1, R) FOR(j, 1, C) if (d[i][j] + a[i][j] == 0) {
        BFS(i, j);
        if (SL == R*C - M) {
                ok = true;
                FOR(u, 1, R) FOR(v, 1, C) b[u][v] = a[u][v];
                b[i][j] = 2;
        }
        return;
    }
}

void Try(int i, int j, int dem) {
   // cout << i << ' ' << j << endl;
    if (j == C + 1) {
        i++;
        j = 1;
    }
    if (i == R + 1) {
        if (dem == M) check();
        return;
    }
    a[i][j] = 0;
    Try(i, j + 1, dem);
    if (ok) return;
    a[i][j] = 1;
    Try(i, j + 1, dem + 1);
    a[i][j] = 0;
}

int main() {
     freopen("in.inp","r",stdin);
     freopen("ans.out","w",stdout);
    int test;
    scanf("%d", &test);
    FOR(t, 1, test) {
        printf("Case #%d:\n", t);
        scanf("%d%d%d", &R, &C, &M);
        ok = false;
        FOR(i, 1, R) FOR(j, 1, C) a[i][j] = 0;
        if (M != R*C - 1) Try(1, 1, 0); else {
            ok = true;
            FOR(i, 1, R) FOR(j, 1, C) b[i][j] = 1;
            b[1][1] = 2;
        }

        if (ok) {
            FOR(i, 1, R) FOR(j, 1, C) {
                if (b[i][j] == 0) cout << '.'; else if (b[i][j] == 1) cout << '*'; else cout << 'c';
                if (j == C) cout << endl;
            }
        } else cout << "Impossible" << endl;
    }
     return 0;
}
