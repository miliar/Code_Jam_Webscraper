#include <iostream>
#include <string>

#include <cmath>

using namespace std;

long long make_p(long long n, bool b)
{
    string s = to_string(n);
    s.reserve(2 * s.size());
    int length = s.size() - b;
    for (int i = 0; i < length; ++i) {
        s.push_back(s[i]);
    }
    return atoi(s.c_str());
}

bool is_palindrome(long long n)
{
    string s = to_string(n);
    for (int i = 0; i < s.size() / 2; ++i) {
        if (s[i] != *(s.end() - i - 1)) return false;
    }
    return true;
}

long long solve()
{
    long long a, b;
    cin >> a >> b;
    long long cnt = 0;
    for (bool x: {true, false}) {
        for (long long current = 0;; ++current) {
            const long long p = make_p(current, x);
            const long long sqr = p * p;
            if (sqr < a) continue;
            if (sqr > b) break;
            if (is_palindrome(sqr)) ++cnt;
        }
    }
    return cnt;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": " << solve() << endl;
    }
    return 0;
}
