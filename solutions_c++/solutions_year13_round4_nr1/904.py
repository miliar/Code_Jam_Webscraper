#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <map>
#include <limits>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
typedef long long LL;

LL mm[105];
int N, M;

void run() {
    memset(mm, 0, sizeof(mm));
    cin >> N >> M;
    LL cost = 0;
    REP(i,M) {
        int o, e, p;
        cin >> o >> e >> p;
        FOR(j,o-1,e-2) {
            mm[j] += p;
        }
        int num = e - o;
        cost += (N * num - (num - 1) * num / 2) * p;
    }

    LL res = 0;
    while (true) {
        int idx = 0;
        while (idx < N && mm[idx] == 0) {
            ++idx;
        }
        if (idx == N) break;

        LL t = mm[idx];
        FOR(i,idx,N-1) {
            if (mm[i] == 0) {
                LL num = i - idx;
                res += (N * num - (num - 1) * num / 2) * t;
                FOR(j,idx,i-1) mm[j] -= t;
                break;
            }
            t = min(t, mm[i]);
        }
    }

    LL diff = cost - res;
    cout << diff << endl;
}

int main() {
    int k;
    cin >> k;
    FOR(c,1,k) {
        cout << "Case #" << c << ": ";
        run();
    }
    return 0;
}
