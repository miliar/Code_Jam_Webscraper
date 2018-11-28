#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cstring>
#include <vector>


using namespace std;

int N, K;
double val[17]={0};
double P[16];

double choose(int k, int i = 0) {
    if (k == 0) {
        return val[K/2];
    }
    if (i == N) return 0;
    double vv[16];
    memcpy(vv, val, sizeof(vv));
    for (int j = N; j >= 0; --j) {
        val[j] = val[j] * (1-P[i]) + (j ? val[j-1] * P[i] : 0);
    }
    double r = choose(k-1, i+1);
    memcpy(val, vv, sizeof(vv));
    return max(r, choose(k, i+1));
}

void tc() {
    cin >> N >> K;
    memset(val, 0, sizeof(val));
    val[0] = 1;
    for (int i =0 ;i < N; ++i) cin >> P[i];
    static int cas = 1;
    cout << "Case #" << cas++ << ": " << fixed << setprecision(8) << choose(K) << endl;
}

int main() {
    int T;
    cin >> T;
    while (T--) tc();
}
