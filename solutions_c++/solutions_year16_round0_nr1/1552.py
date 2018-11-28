#include <iostream>
using namespace std;

long long T, N;
bool digits[10];

void cleardigits() {
    for (int i = 0; i < 10; i++)
        digits[i] = false;
}

bool checkdigits() {
    for (int i = 0; i < 10; i++)
        if (!digits[i]) return false;
    return true;
}

void markdigits(long long N) {
    while (N) {
        int i = N % 10;
        N /= 10;
        digits[i] = true;
    }
}


long long solve(long long N) {
    cleardigits();
    long long M = N;
    while (true) {
        markdigits(M);
        if (checkdigits()) return M;
        M += N;
    }
}

int main() {
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cin >> N;
        /* for (int j = 0; j <= 1000000; j++) { N = j; */
        if (!N) cout << "Case #" << i << ": INSOMNIA" << endl;
        else cout << "Case #" << i << ": " << solve(N) << endl;
        /* } */
    }
}
