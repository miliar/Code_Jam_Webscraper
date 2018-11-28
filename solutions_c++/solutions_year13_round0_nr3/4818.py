#include <iostream>
#include <sstream>
#include <cmath>
using namespace std;
typedef unsigned long long int llu;

bool is_palindrome(llu x) {
    ostringstream oss;
    oss << x;
    string s = oss.str();

    for(int head = 0, tail = s.length() - 1; head <= tail; ++head, --tail) {
        if(s[head] != s[tail]) return false;
    }
    return true;
}

int main(void) {
    int t;
    cin >> t;

    for(int n = 1; n <= t; ++n) {
        llu a, b;
        cin >> a >> b;

        int sum = 0;
        llu sqrt_a = ceil(sqrt(a)), sqrt_b = floor(sqrt(b));
        for(llu i = sqrt_a; i <= sqrt_b; ++i) {
            if(is_palindrome(i) &&
               a <= i * i && i * i <= b &&
               is_palindrome(i * i)) {
                ++sum;
            }
        }

        cout << "Case #" << n << ": " << sum << endl;
    }
    return 0;
}
