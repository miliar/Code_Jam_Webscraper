#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int T;
double C, F, X;

void solve() {
    double res = 0;
    double curF = 2;
    while ((C / curF + X / (curF + F)) < X / curF) {
        res += C / curF;
        curF += F;
    }
    res += X / curF;
    printf("%.7f\n", res);
}

int main() {
    //freopen("b.input", "r", stdin);
    cin >> T;
    for (int caseId = 1; caseId <= T; ++caseId) {
        cin >> C >> F >> X;
        cout << "Case #" << caseId << ": ";
        solve();
    }
    return 0;
}
