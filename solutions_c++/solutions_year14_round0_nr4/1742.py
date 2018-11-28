#include <iostream>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <algorithm>
using namespace std;

int main() {
    freopen("D-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T, n, ans1, ans2;
    vector<double> a, b;
    cin >> T;
    for (int task = 1; task <= T; task++) {
        a.clear();
        b.clear();
        cin >> n;
        for (int i = 0; i < n; i++) {
            double num;
            cin >> num;
            a.push_back(num);
        }
        for (int i = 0; i < n; i++) {
            double num;
            cin >> num;
            b.push_back(num);
        }
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());
        for (ans1 = n; ans1 >= 0; ans1--) {
            bool c = true;
            for (int i = 0; i < ans1; i++) {
                if (b[i] > a[n - ans1 + i]) {
                    c = false;
                    break;
                }
            }
            if (c) {
                break;
            }
        }
        ans2 = n;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (b[j] > 0 && b[j] > a[i]) {
                    b[j] = -1;
                    ans2--;
                    break;
                }
            }
        }
        cout << "Case #" << task << ": " << ans1 << " " << ans2 << endl;
    }
    
    return 0;
}
