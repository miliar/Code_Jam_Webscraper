#include <iostream>

using namespace std;

int f[10];
int T;
int N;

int main() {
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    cin >> T;
    for (int i = 1; i < T + 1; i++) {
        cin >> N;
        for (int j = 0; j < 10; j++) {
            f[j] = 0;
        }

        if (N == 0) {
            cout << "Case #" << i << ": INSOMNIA" << endl;
            continue;
        }

        bool ok = false;
        int K = N;
        while (!ok) {
            int x = K;
            while (x) {
                // cerr << x << endl;
                f[x % 10] ++;
                x /= 10;
            }

            ok = true;
            for (int j = 0; j < 10; j++) {
                // cerr << f[j] << " ";
                ok = ok && (f[j] > 0);
            }
            // cerr << endl;

            K = K + N;
        }

        cout << "Case #" << i << ": " << K - N << endl;
    }

    return 0;
}
