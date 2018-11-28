#include <iostream>
#include <vector>
#include <limits>

using namespace std;

int main() {
    int T; cin >> T;

    for (int test = 1; test <= T; ++test) {
        int D; cin >> D;
        vector<int> count(1001, 0);
        for (int i = 0; i < D; ++i) {
            int x; cin >> x;
            ++count[x];
        }

        int answer = numeric_limits<int>::max();
        for (int i = 1000; i > 0; --i) {
            int prec = 0;
            for (int j = 1000; j > i; --j) {
                prec += count[j] * ((j - 1) / i);
            }
            answer = min(answer, prec + i);
        }

        cout << "Case #" << test << ": " << answer << "\n";
    }
}
