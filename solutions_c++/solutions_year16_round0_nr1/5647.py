#include <iostream>
#include <map>
#include <stdio.h>
#include <cstddef>
#include <sstream>
#include <vector>
#include <stdexcept>
#include <fstream>

using namespace std;

int solve(int n)
{
    if (!n) {
        return -1;
    }
    vector <bool> was(10, false);
    int remain = 10, fn = n;
    while (remain) {
        int tmp = n;
        while (tmp) {
            if (!was[tmp % 10]) {
                remain--;
                was[tmp % 10] = true;
            }
            tmp /= 10;
        }
        n += fn;
    }
    return n - fn;
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int n;
        cin >> n;
        int ans = solve(n);
        cout << "Case #" << i + 1 << ": ";
        if (ans == -1) {
            cout << "INSOMNIA" << endl;
        } else {
            cout << ans << endl;
        }
    }
    return 0;
}
