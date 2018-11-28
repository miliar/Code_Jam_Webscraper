#include <iostream>
#include <vector>

using namespace std;

int main() {
    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t) {
        unsigned long N;
        cin >> N;
        if (N == 0) {
            cout << "Case #" << t << ": INSOMNIA\n";
            continue;
        }
        vector<bool> seen(10, false);
        int numSeen = 0;
        unsigned long currN = N;
        while (true) {
            unsigned long n = currN;
            while (n > 0) {
                int digit = n % 10;
                if (!seen[digit]) {
                    seen[digit] = true;
                    numSeen++;
                }
                n /= 10;
            }
            if (numSeen == 10) {
                break;
            }
            currN += N;
        }
        cout << "Case #" << t << ": " << currN << "\n";
    }
    return 0;
}
