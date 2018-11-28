#include <iostream>
#include <cmath>

using namespace std;

bool isPalindrome(long long N) {
    long long a = 0, b = N, r;
    while (b > 0) {
        r = b % 10;
        a = a * 10 + r;
        b = b / 10;
    }
    return a == N;
}

long long getNumberOfFairAndSquareNumbers(long long A, long long B) {
    long long L = sqrt(B);
    long long total = 0;

    for (long long n = 1; n <= L; n++) {
        if (isPalindrome(n)) {
            long long ns = n * n;
            if (isPalindrome(ns) && ns >= A && ns <= B)
                total++;
        }
    }

    return total;
}

int main() {
    int T;
    long long A, B;

    cin >> T;
    for (int i = 1; i <= T; i++) {
        cin >> A >> B;
        cout << "Case #" << i << ": " << getNumberOfFairAndSquareNumbers(A, B) << endl;
    }

    return 0;
}
