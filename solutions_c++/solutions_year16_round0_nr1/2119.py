#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solve(int n) {
    if (n == 0)return -1;
    vector<bool> was(10);
    int wascnt = 0;
    int cur = n;
    int res = 0;
    for (; ;) {
        res++;
        int t = cur;
        while (t) {
            if (!was[t % 10]) wascnt++;
            was[t % 10] = true;
            t /= 10;
        }
        if (wascnt == 10) {
            return res*n;
        }
        cur+=n;
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tcs;
    cin >> tcs;
    for (int tc = 1; tc <= tcs; tc++) {
        int n;
        cin >> n;
        int res = solve(n);
        cout << "Case #" << tc << ": ";
        if (res == -1) {
         cout << "INSOMNIA" << endl;
        } else {
            cout << res << endl;
        }
    }


    return 0;
}