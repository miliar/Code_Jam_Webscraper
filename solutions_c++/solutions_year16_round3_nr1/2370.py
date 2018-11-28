#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

void solve (int a) {
    int p[a];
    int sum = 0;

    for (int i = 0; i < a; i++) {
        cin >> p[i];
        sum += p[i];
    }

    do {
        int pp = 0;
        int maxI = 0;
        int maxI2 = 0;
        bool f = false;
        if (p[0] > 0) pp++;
        for (int i = 1; i < a; i++) {
            if (p[i] > p[maxI]) {
                maxI = i;
                f = false;
            } else if (p[i] == p[maxI]) {
                f = true;
                maxI2 = i;
            }
            if (p[i] > 0) pp++;
        }
        if (f) {
            if(pp > 2) {
                cout << (char)(65 + maxI) << ' ';
                p[maxI]--;
                sum-=1;
            } else {
                cout << (char)(65 + maxI) << (char)(65 + maxI2) << ' ';
                p[maxI]--;
                p[maxI2]--;
                sum -= 2;
            }
        } else {
            cout << (char)(65 + maxI) << " ";
            p[maxI]--;
            sum -= 1;
        }
    } while(sum > 0);
    cout << "\n";
}

int main () {
    int T;
    int a;
    cin >> T;

    for (int i = 1; i <= T; ++i) {
        cin >> a;
        cout << "Case #" << i << ": ";
        solve(a);
    }

    return 0;
}
