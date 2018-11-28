#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    long long int T, n, N;
    cin >> T;
    for (long long int t = 1 ; t <= T ; t++) {
        cin >> N;
        if (N == 0) {
            cout << "Case #" << t << ": INSOMNIA" << endl;
            continue;
        }
        n = N;
        int count = 0, a[10] = {0};
        while (count != 10) {
            long long int tmp = n;
            while (tmp) {
                if (a[tmp % 10] == 0) {
                    count++;
                    a[tmp % 10] = 1;
                }
                tmp = tmp / 10;
            }
            if (count != 10)
                n += N;
        }
        cout << "Case #" << t << ": " << n << endl;
    }
    return 0;
}
