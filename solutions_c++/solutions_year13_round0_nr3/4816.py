#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cmath>

using namespace std;

int digits[25];

bool isPalindrome(long long number) {
    int cnt = 0;
    while (number > 0) {
        digits[cnt++] = number % 10;
        number /= 10;
    }

    int len = cnt;
    int halflen = len >> 1;
    for (int i = 0; i < halflen; i++) {
        if (digits[i] != digits[len - i - 1]) {
            return false;
        }
    }

    return true;
}

bool isDoublePalindrome(long long number) {
    return isPalindrome(number) && isPalindrome(number * number);
}

vector < int > palindromes;
void gen_palindromes() {
    for (int i = 1; i <= 10000000; i++) {

        if (isDoublePalindrome((long long)i)) {
            palindromes.push_back(i);
        }
    }

    //cout << palindromes.size() << endl;
}

int solve() {
    long long a, b;
    cin >> a >> b;

    int res = 0;
    for (int i = 0; i < (int) palindromes.size(); i++) {
        long long number = palindromes[i] * palindromes[i];
        if (a <= number && number <= b) {
            res++;
        }
    }

    return res;
}

int main() {
    gen_palindromes();

    int tests;
    cin >> tests;

    for(int i = 0; i < tests; i++) {
        cout << "Case #" << i + 1 << ": " << solve() << endl;
    }

    return 0;
}
