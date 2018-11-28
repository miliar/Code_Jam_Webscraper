#include <iostream>
#include <queue>
using namespace std;

int main() {
    int t; cin >> t;
    for (int i = 1; i <= t; i++) {
        int d; cin >> d;
        int p[d];
        for (int j = 0; j < d; j++)
            cin >> p[j];

        int res = 1001;
        for (int j = 1; j <= 1000; j++) {
            int s = j;
            for (int k = 0; k < d; k++) {
                s += (p[k]-1)/j;
            }
            if (s < res) res = s;
        }

        cout << "Case #" << i << ": " << res << endl;

    }
    return 0;
}
