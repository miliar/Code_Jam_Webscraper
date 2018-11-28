#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool isPalindrom (long long x) {
    vector<int> digits;
    while (x > 0) {
        digits.push_back(x % 10);
        x /= 10;
    }
    vector<int> rDigits(digits.rbegin(), digits.rend());
    
    return digits == rDigits;
}

const long long N = 1e7 + 10;
vector<long long> goodPalindromes;

void precalc () {
    goodPalindromes.clear();
    for (long long i = 1; i < N; ++i) {
        if (isPalindrom(i) && isPalindrom(i * i)) {
            goodPalindromes.push_back(i);
        }
    }
}

long long countGoodSquares (long long x) {
    if (x <= 0) {
        return 0;
    }
    
    int left = 0, right = goodPalindromes.size();
    while (left + 1 < right) {
        int middle = (left + right) / 2;
        long long y = goodPalindromes[middle];
        if (y * y > x) {
            right = middle;
        }
        else {
            left = middle;
        }
    }
    return right;
}

void solveCase (int caseNum) {
    long long left, right;
    cin >> left >> right;
    cout << "Case #" << caseNum + 1 << ": " << countGoodSquares(right) - countGoodSquares(left - 1) << "\n";
}

int main () {
    precalc();
    
    int testsCount;
    cin >> testsCount;
    for (int i = 0; i < testsCount; ++i) {
        solveCase(i);
    }
    
    
    return 0;
}
