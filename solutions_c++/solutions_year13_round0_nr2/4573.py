#include <iostream>

using namespace std;

#define FOR(i,n) for(int i=0;i<(n);i++)

int R, C;
int A[128][128];
int r[128], c[128];

bool do_case() {
    cin >> R >> C;
    FOR(i,R) FOR(j,C) cin >> A[i][j];
    FOR(i,R) {
        r[i] = 0;
        FOR(j,C) r[i] = max(r[i],A[i][j]);
    }
    FOR(i,C) {
        c[i] = 0;
        FOR(j,R) c[i] = max(c[i],A[j][i]);
    }
    FOR(i,R) FOR(j,C) if(A[i][j] != min(r[i],c[j])) return false;
    return true;
}

int main() {
    int T;
    cin >> T;
    FOR(it,T) cout << "Case #" << it+1 << ": " << (do_case() ? "YES" : "NO") << endl;
    return 0;
}

