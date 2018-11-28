#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int times = 1; times <= T; ++times) {
        string P;
        int N;
        cin >> P >> N;
        int ans = 0;
        for (int i = 0; i + N <= P.size(); ++i) {
            if (P[i] == '-') {
                for (int j = i; j < i + N; ++j) {
                    if (P[j] == '-') P[j] = '+'; else P[j] = '-';
                }
                ++ans;
            }
        }
        bool flag = true;
        for (int i = 0; i < P.size(); ++i) {
            if (P[i] == '-') flag = false;
        }
        cout << "Case #" << times << ": ";
        if (flag) cout << ans << endl; else cout << "IMPOSSIBLE" << endl;


    }

    return 0;
}