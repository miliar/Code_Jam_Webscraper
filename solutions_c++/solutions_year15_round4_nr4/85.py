#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)
#define EACH(it,a) for(__typeof(a.begin()) it = a.begin(); it != a.end(); ++it)

#define DEBUG(x) { cout << #x << " = "; cout << (x) << endl; }
#define PR(a,n) { cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl; }
#define PR0(a,n) { cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl; }

#define sqr(x) ((x) * (x))
using namespace std;

int m, n;
int res;

int a[11][11];
const int di[] = {-1,1,0,0};
const int dj[] = {0,0,-1,1};

bool check(int i, int j, bool fin=false) {
    if (!a[i][j]) {
        if (fin) return false;
        return true;
    }
    int good = 0, can = 0;
    REP(dir,4) {
        int ii = i + di[dir];
        if (ii < 1 || ii > m) continue;

        int jj = j + dj[dir]; if (jj == 0) jj = n; if (jj > n) jj = 1;

        if (a[ii][jj] == a[i][j]) ++good;
        else if (a[ii][jj] == 0) ++can;
    }
    if (fin) return good == a[i][j];
    else return good <= a[i][j] && good+can >= a[i][j];
}

#define next next__
#define prev prev__

int next(int j) {
    if (j == n) return 1;
    else return j+1;
}

int prev(int j) {
    if (j == 1) return n;
    else return j-1;
}

set< vector<int> > all;

void attempt(int i, int j) {
    if (i > m) {
        FOR(i,1,m) FOR(j,1,n) if (!check(i, j, true)) return ;

        vector<int> hash;
        FOR(j,1,n) {
            int cur = 0;
            FOR(i,1,m) cur = cur * 4 + a[i][j];
            
            hash.push_back(cur);
        }
        vector<int> min_hash = hash;
        FOR(rot,1,n) {
            rotate(hash.begin(), hash.begin()+1, hash.end());
            min_hash = min(min_hash,hash);
        }
        all.insert(min_hash);
        ++res;
        return ;
    }
    int ii = i, jj = j + 1;
    if (jj > n) jj = 1, ++ii;

    FOR(val,1,3) {
        a[i][j] = val;
        if (check(i, j)
                && (i == 1 || check(i-1, j))
                && (i == m || check(i+1, j))
                && check(i, next(j))
                && check(i, prev(j)))
            attempt(ii, jj);
        a[i][j] = 0;
    }
}

int result[11][11];

int main() {
    ios :: sync_with_stdio(false);
    FOR(i,2,6) FOR(j,3,6) {
        all.clear();
        m = i; n = j;
        res = 0;
        attempt(1, 1);
//        cout << i << ' ' << j << ' ' << res << ' ' << all.size() << endl;
        result[i][j] = all.size();
    }
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        int m, n; cin >> m >> n;
        cout << "Case #" << test << ": " << result[m][n] << endl;
    }
    return 0;
}

