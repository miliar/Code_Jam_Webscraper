#include <iostream>
#include <string>

using namespace std;

void solve(int N) {
    if (N == 0) {
        cout << "INSOMNIA" << endl;
        return;
    }
    bool used[10];
    memset(used, 0, sizeof(used));
    int k = 1;
    while (1) {
        int p = k * N;
        while (p > 0) {
            used[p % 10] = 1;
            p /= 10;
        }
        bool sleep = true;
        for (int i=0; i< 10; ++i)
            if (!used[i]) {
                sleep = false;
                break;
            }
        if (sleep) {
            cout << k * N << endl;
            return;
        }
        ++k;
    }
}

int main() {
    int T;
    cin >> T;
    for (int i=0; i<T; ++i) {
        int N;
        cin >> N;
        cout << "Case #" << i + 1 << ": ";
        solve(N);
    }
    return 0;    
}