#include <bits/stdc++.h>
using namespace std;

bool check(long long n) {
    int a = 0, b = 0;
    for (int i = 0; i < 32; ++i) {
        if ((1LL<<i)&n) {
            a+=i%2;
            b+=(i+1)%2;
        }
    }
    if ((a+b)%6 == 0 && a == b && n%2 != 0 && (n&(1LL<<31))) return 1;
    return 0;
}

string to_str(long long i) {
    string ans = "";
    while (i > 0) {
        ans += to_string(i%2);
        i /= 2;
    }
    reverse(ans.begin(), ans.end());
    return ans;
}

int main() {
    cout << "Case #1:" << endl;
    int n = 32, j = 500;
    cerr << check((1LL<<31) + 31) << endl;
    for (long long i = 0; j > 0 && i < (1LL << n); ++i) {
        long long t = i|(1LL<<31);
        if (check(t)) {
            j--;
            cout << to_str(t) << " ";
            cout << "3 2 3 2 7 2 3 2 3" << endl;
        }
    }
    return 0;
}