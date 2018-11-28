#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

int T, N;;
double nao[1001], ken[1001];

void solve() {
    int war = N, dwar = 0;
    sort(nao, nao + N);
    sort(ken, ken + N);
    bool *flag = new bool[N];
    memset(flag, false, N);
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (nao[j] > ken[i] && !flag[j]) {
                ++dwar; 
                flag[j] = true;
                break;
            }
        }
    }
    memset(flag, false, N);
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (ken[j] > nao[i] && !flag[j]) {
                --war; 
                flag[j] = true;
                break;
            }
        }
    }
    cout << dwar << " " << war << endl;
}

int main() {
    //freopen("d.input", "r", stdin);
    cin >> T;
    for (int caseId = 1; caseId <= T; ++caseId) {
        cin >> N;
        for (int i = 0; i < N; ++i) {
            cin >> nao[i];
        }
        for (int i = 0; i < N; ++i) {
            cin >> ken[i];
        }
        cout << "Case #" << caseId << ": ";
        solve();
    }
    return 0;
}
