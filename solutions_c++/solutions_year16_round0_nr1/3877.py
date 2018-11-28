#include <iostream>

using namespace std;

int main() {

    int t; cin >> t;

    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        int n; cin >> n;
        if (n == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }

        int m = 0;
        int toGo = 10; 
        bool seen[10];
        for (int i = 0; i < 10; ++i) seen[i] = false;
        while (toGo) {
            m += n;
            int oldm = m;
            while (oldm) {
                int d = oldm % 10;
                oldm /= 10;
                if (!seen[d]) {
                    --toGo;
                    seen[d] = true;
                }
            }
        }
        cout << m << endl;
    }

    return 0;
}
