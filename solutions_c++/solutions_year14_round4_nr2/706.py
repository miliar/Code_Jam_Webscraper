#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>
#include <climits>
using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T, n, num[1000], cnt, ans;
    cin >> T;
    for (int task = 1; task <= T; task++) {
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> num[i];
        }
        ans = 0;
        for (int i = 0; i < n; i++) {
            int p = 0;
            for (int j = 1; j < n; j++) {
                if (num[j] < num[p]) {
                    p = j;
                }
            }
            int cnt = 0;
            for (int i = 0; i < p; i++) {
                if (num[i] != INT_MAX) {
                    cnt++;
                }
            }
            if (n - 1 - i - cnt < cnt) {
                cnt = n - 1 - i - cnt;
            }
            ans += cnt;
            num[p] = INT_MAX;
        }
        printf("Case #%d: %d\n", task, ans);
    }
    
    return 0;
}
