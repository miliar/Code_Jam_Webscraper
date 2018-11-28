#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>
using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T, n, x, tot;
    cin >> T;
    vector<int> s;
    for (int task = 1; task <= T; task++) {
        cin >> n >> x;
        s.clear();
        for (int i = 0; i < n; i++) {
            int num;
            cin >> num;
            s.push_back(num);
        }
        sort(s.begin(), s.end());
        tot = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] != -1) {
                for (int j = n - 1; j > i; j--) {
                    if (s[j] != -1 && s[i] + s[j] <= x) {
                        s[j] = -1;
                        break;
                    }
                }
                s[i] = -1;
                tot++;
            }
        }
        printf("Case #%d: %d\n", task, tot);
    }
    
    return 0;
}
