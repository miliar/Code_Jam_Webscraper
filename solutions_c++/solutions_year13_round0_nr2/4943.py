#include <algorithm>
#include <iostream>
#include <cstring>

#define REP(i,a) for(int i=0;i<(a);i++)

using namespace std;


int main() {
    int T, M, N;
    cin >> T;
    REP(cas,T) {
        cin >> M >> N;
        int maxh[M], maxv[N];
        int a[M][N];
        REP(i,M) REP(j,N) cin >> a[i][j];
        REP(i,M) {
            int h = -1;
            REP(j,N) h = max(h, a[i][j]);
            maxh[i] = h;
        }
        REP(j,N) {
            int v = -1;
            REP(i,M) v = max(v, a[i][j]);
            maxv[j] = v;
        }
        cout << "Case #" << (cas+1) << ": ";
        REP(i,M) REP(j,N) {
            if (a[i][j]!=maxh[i] && a[i][j]!=maxv[j]) {
                cout << "NO";
                goto exit;
            }
        }
        cout << "YES";
        exit:
        cout << endl;
    }
    return 0;
}
