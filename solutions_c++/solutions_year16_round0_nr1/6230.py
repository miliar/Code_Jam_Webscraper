#include <bits/stdc++.h>

using namespace std;

int main() {
    int t, n, q, mask, i, tt = 1;
    cin >> t;

    while(t--) {
        cin >> n;
        if (n == 0) {
            cout << "Case #" << tt++ << ": " << "INSOMNIA" << endl;
            continue;
        }
        mask = 0;
        i = 1;
        while(mask != 1023) {
            q = n*i;
            while (q) {
                mask |= 1 << (q % 10);
                q /= 10;
            }
            i++;
        }
        cout << "Case #" << tt++ << ": " << n * (i-1) << endl;

    }
    return 0;
}
