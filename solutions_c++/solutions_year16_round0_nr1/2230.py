#include <iostream>
#include <unordered_set>

using namespace std;

int solve(int n) {
    if (n == 0)
        return -1;
    unordered_set<int> digits;
    int k = n;
    while (true) {
        int t = k;
        while (t) {

            digits.insert(t % 10);
            t /= 10;
        }
        if (digits.size() == 10)
            return k;
        k += n;
    }
}

int main() {
    int T, N, R;
    cin >> T;
    for (int c = 1; c <= T; c++) {
        cin >> N;
        R = solve(N);
        if (R < 0)
            cout << "Case #" << c << ": INSOMNIA" << endl;
        else
            cout << "Case #" << c << ": " << R << endl;
    }

    return 0;
}