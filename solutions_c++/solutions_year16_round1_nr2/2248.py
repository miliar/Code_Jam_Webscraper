#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define RFOR(i,a,b) for(int i=(a);i>=(b);--i)
typedef long long LL;

vector<vector<int> > mm, mat;
vector<int> res;
bool found;

#define MAXN 110
int cnt;

bool isvalid(vector<vector<int> > mat, int N) {
    /*REP(i, N) {
        FOR(j, 1, N - 1) {
            if (mat[i][j] <= mat[i][j - 1]) return false;
        }
    }*/

    REP(j, N) {
        FOR(i, 1, N - 1) {
            if (mat[i][j] <= mat[i - 1][j]) return false;
        }
    }

    return true;
}

void dummy(int* a, int n){
    mat.clear();
    REP(i, n) mat.push_back(mm[a[i] - 1]);
    sort(mat.begin(), mat.end());

    if (!isvalid(mat, n)) return;

    set<int> si;
    REP(i, n) si.insert(a[i] - 1);
    set<vector<int> > sv;
    REP(i, n * 2 - 1) {
        if (si.find(i) == si.end()) sv.insert(mm[i]);
    }
    int missing = 0;
    vector<int> r;
    REP(j, n) {
        vector<int> tmp;
        REP(i, n) tmp.push_back(mat[i][j]);
        if (sv.find(tmp) == sv.end()) {
            r = tmp;
            ++missing;
            if (missing >= 2) break;
        }
    }

    if (missing == 1) {
        found = true;
        res = r;
    }
}

void _gen_comb(int* a, int s, int e, int m, int& cnt, int* temp){
    if (found) return;
    int i;
    if (!m)
        dummy(temp, cnt);
    else {
        for (i = s; i <= e - m + 1; i++){
            temp[cnt++] = a[i];
            _gen_comb(a, i + 1, e, m - 1, cnt, temp);
            cnt--;
        }
    }
}

void gen_comb(int n, int m){
    int a[MAXN], temp[MAXN], cnt = 0, i;
    for (i = 0; i<n; i++)
        a[i] = i + 1;
    _gen_comb(a, 0, n - 1, m, cnt, temp);
}

void run() {
    int N;
    cin >> N;
    mm.clear();
    REP(i, N * 2 - 1) {
        vector<int> tmp(N);
        REP(j, N) cin >> tmp[j];
        mm.push_back(tmp);
    }

    found = false;
    gen_comb(N * 2 - 1, N);

    REP(i, N) cout << " " << res[i];
    cout << endl;
}

int main() {
    int k;
    cin >> k;
    FOR(c,1,k) {
        cout << "Case #" << c << ":";
        run();
    }
    return 0;
}
