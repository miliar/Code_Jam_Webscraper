#include <iostream>
#include <climits>
#include <list>
#include <vector>
#include <algorithm>
using namespace std;

long long next_special(long long n) {
    auto k = n;
    int digits = 0;
    while (k > 0) {
        digits += 1;
        k /= 10;
    }
    long long result = n;
    for (int i = digits / 2; i >= 1; --i) {
        result /= 10;
    }
    for (int i = digits / 2; i >= 1; --i) {
        result *= 10;
    }
    result += 1;
    return result;
}

long long reverse(long long n) {
    long long result = 0;
    while (n > 0) {
        result = result * 10 + n % 10;
        n /= 10;
    }
    return result;
}

long long solve(long long n) {
    if (n == 1) {
        return 1;
    }
    auto n1 = next_special(n);
    if (n1 < n) {
        return n - n1 + solve(n1);
    }
    else if (n1 == n) {
        auto rn = reverse(n);
        if (rn < n) {
            return 1 + solve(rn);
        }
    }
    return 1 + solve(n - 1);
}

int main() {
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        long long n;
        cin >> n;
        cout << "Case #" << t << ": " << solve(n) << "\n";
    }
    return 0;
}
