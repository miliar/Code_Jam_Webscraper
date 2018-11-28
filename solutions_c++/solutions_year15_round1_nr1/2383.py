#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>

#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

int main() {
    ifstream cin("src/in.txt");
    ofstream cout("src/out.txt");
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        int n;
        cin >> n;
        long long m[n];
        for (int j = 0; j < n; ++j) {
            cin >> m[j];
        }
        cout << "Case #" << (i + 1) << ": ";
        // 1
        long long ans1 = 0;
        for (int j = 1; j < n; ++j) {
            ans1 += m[j - 1] - m[j] > 0 ? m[j - 1] - m[j] : 0;
        }
        // 2
        long long ans2 = 0, rate = 0;
        for (int j = 1; j < n; ++j) {
            rate = max(rate, m[j - 1] - m[j]);
        }
        for (int j = 0; j < n - 1; ++j) {
            ans2 += min(rate, m[j]);
        }
        cout << ans1 << " " << ans2 << endl;
    }
}
