#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

void solve(long long cas) {
    cout << "Case #" << cas << ": ";

    long long N;
    cin >> N;

    if (N == 0) {
        cout << "INSOMNIA" << endl;
        return;
    }

    vector<bool> seen(10, 0);
    const long long add = N;
    while (std::count(seen.begin(), seen.end(), 0) > 0) {
        long long tmp = N;
        while (tmp) {
            seen[tmp % 10] = true;
            tmp /= 10;
        }
        N += add;
    }

    cout << N-add << endl;
}

int main() {
    long long T;
    cin >> T;
    for (long long i = 0; i < T; ++i) {
        solve(i+1);
    }
}
