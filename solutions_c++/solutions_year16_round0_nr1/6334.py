#include <iostream>
#include <cstdio>
#include <climits>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

bool digit[10];

int getDigit(long long n) {
    int cnt = 0;

    while (n) {
        int d = n % 10;
        n /= 10;

        if (digit[d] == false) cnt++;
        digit[d] = true;
    }

    return cnt;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";

        long long n;
        cin >> n;

        if (n == 0)  {
            cout << "INSOMNIA" << endl;
            continue;
        }

        if (n < 0) n = -n;

        int total = 0;
        for (int i = 0; i < 10; ++i) digit[i] = false;

        long long ans = 0;
        do {
            ans += n;
            total += getDigit(ans);
        } while (total < 10);

        cout << ans << endl;
    }

    return 0;
}
