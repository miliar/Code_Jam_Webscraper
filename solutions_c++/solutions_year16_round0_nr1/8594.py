#include <bits/stdc++.h>

using namespace std;

int f[10];

int rem = 0;

void decomp(int n) {
    do {
        if(f[n % 10] == 0)
            rem--;
        f[n % 10]++;
        n /= 10;
    }while(n > 0);
}

int main() {
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": ";
        int n;
        cin >> n;
        memset(f, 0, sizeof(f));

        int now = n;
        rem = 10;
        bool ok = 0;
        for(int j = 0; j < 1000; ++j) {
            decomp(now);
            if(rem == 0) {
                cout << now << "\n";
                ok = 1;
                break;
            }
            now += n;
        }
        if(!ok) {
            cout << "INSOMNIA\n";
        }
    }

    return 0;
}
