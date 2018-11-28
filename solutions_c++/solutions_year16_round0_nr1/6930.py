#include <iostream>
#include <cstring>

using namespace std;
bool v[10];

bool check() {
    for (int i = 0; i < 10; i++)
        if (!v[i]) return false;
    return true;
}

int main() {
    int tt, n, ttt = 0;

    cin >> tt;
    while (ttt++ < tt) {
        cin >> n;
        cout << "Case #" << ttt << ": ";
        if (n == 0)
            cout << "INSOMNIA\n";
        else {
            memset(v, 0, sizeof(v));
            for (long long i = n; ; i += n) {
                for (long long j = i; j; j /= 10) {
                    v[j % 10] = true;
                }
                if (check()) {
                    cout << i << endl;
                    break;
                }
            }
        }
    }
}

