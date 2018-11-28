#include <iostream>
#include <cstdio>
using namespace std;

bool ima[10];

bool check(int x) {
    while (x) {
        ima[x%10] = true;
        x /= 10;
    }
    bool ret = 1;
    for (int i = 0; i < 10; i++)
        if (!ima[i])
            ret = 0;
    return ret;
}

int main () {
    int T; cin >> T;
    int t = T;
    while (T--) {
        int n; cin >> n;
        for (int i = 0; i < 10; i++)
            ima[i] = 0;
        if (n == 0) {
            cout << "Case #" << t - T <<": " <<  "INSOMNIA" << endl;
            continue;
        }
        for (int j = 1; j < 100; j++) {
            if (check(n * j)) {
                cout<< "Case #" << t - T <<": " <<  n * j << endl;
                break;
            }
        }
    }
    return 0;
}
