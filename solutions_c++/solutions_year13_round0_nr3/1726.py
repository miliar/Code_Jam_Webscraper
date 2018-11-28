#include <iostream>
#include <sstream>
#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long int64;

using namespace std;

bool is_palindrome(int64 n) {
    stringstream ss;
    ss << n;
    string s = ss.str();
    string s_rev = s;
    reverse(all(s_rev));
    return s == s_rev;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int64 n = 10000100;
    vector<int64> res(n, 0);
    for (int64 i = 1; i < n; ++i) {
        if (is_palindrome(i) && is_palindrome(i * i))
            ++res[i];
        res[i] += res[i - 1];
    }        
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        int64 a, b;
        cin >> a >> b;
        int64 sqrt_a = (int64)sqrt(a - 1);
        while (sqrt_a * sqrt_a < a)
           ++sqrt_a;
        int64 sqrt_b = (int64)sqrt(b + 1);
        while (sqrt_b * sqrt_b > b)
           --sqrt_b;
        int64 ans = res[sqrt_b] - res[sqrt_a - 1];
        cout << "Case #" << test << ": " << ans << endl;
    }
    return 0;
}
