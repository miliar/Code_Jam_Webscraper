#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iterator>
using namespace std;

vector<long long> palindromes;

bool is_palindome(long long a) {
    vector<int> digits;
    while (a > 0) {
        digits.push_back(a % 10);
        a /= 10;
    }
    for (int i = 0; i < digits.size() / 2; i++) {
        if (digits[i] != digits[digits.size() - i - 1]) {
            return false;
        }
    }
    return true;
}

int solve(long long a, long long b) {
    int ans = 0;
    for (int i = 0; i < palindromes.size(); i++) {
        long long cur = palindromes[i];
        if (cur * cur >= a && cur * cur <= b) {
            if (is_palindome(cur * cur)) {
                ans++;
            }
        }
    }
    return ans;
}


void fill_palindromes() {
    for (long long i = 1; i < 10000000; i++) {
        if (is_palindome(i)) {
            palindromes.push_back(i);
        }
    }
}

int main()
{
    fill_palindromes();
    // std::copy(palindromes.begin(), palindromes.end(), std::ostream_iterator<long long>(cout, ", "));
    int t;
    cin >> t;
    for (size_t test = 0; test < t; test++)
    {
        long long a, b;
        cin >> a >> b;
        cout << "Case #" << test + 1 << ": " << solve(a, b) << "\n";
    }
    return 0;
}