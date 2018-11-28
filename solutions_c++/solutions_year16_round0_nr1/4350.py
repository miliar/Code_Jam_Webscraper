#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int a[10];
    long long t, n;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> n;
        cout << "Case #" << i << ": ";
        if (n == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }
        int num = 0;
        memset(a, 0, sizeof a);
        long long old = n;
        while (true) {
            long long tmp = n;
            while (tmp > 0) {
                int now = tmp % 10;
                a[now]++;
                if (a[now] == 1) {
                    num++;
                }
                tmp /= 10;
            }
            if (num >= 10) {
                cout << n << endl;
                break;
            }
            n += old;
        }
    }
    return 0;
}
