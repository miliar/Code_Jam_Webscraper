#include <iostream>

using namespace std;

int t, n, x;
int q[1000];

int main() {
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> n >> x;
        for (int j = 1; j <= x; j++) q[j] = 0;
        for (int j = 0; j < n; j++) {
            int a;
            cin >> a;
            q[a]++;
        }
        int c = 0;
        while (true) {
            int v = -1;
            for (int j = x; j >= 1; j--) {
                if (q[j]) {
                    q[j]--;
                    v = j;
                    break;
                }
            }
            if (v == -1) break;
            c++;
            for (int j = x; j >= 1; j--) {
                if (q[j] && v+j <= x) {
                    q[j]--;
                    break;
                }
            }
        }
        cout << "Case #" << i << ": " << c << "\n";
    }
}
