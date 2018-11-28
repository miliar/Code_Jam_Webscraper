#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int T, N;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> N;
        int a[1000];
        for (int i = 0; i < N; i++) cin >> a[i];
        int y = 0;
        int max_diff = 0;
        for (int i = 1; i < N; i++) {
            y += max(0, a[i - 1] - a[i]);
            max_diff = max(max_diff, a[i - 1] - a[i]);
        }
        int z = 0;
        for (int i = 1; i < N; i++) {
            z += min(max_diff, a[i - 1]);
        }
        cout << "Case #" << t << ": " << y << " " << z << endl;
    }
}
