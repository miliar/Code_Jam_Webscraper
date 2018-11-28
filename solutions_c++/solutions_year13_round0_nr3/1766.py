#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

bool isPalin(string s) {
    for (int i = 0; i < s.size() / 2; i++) {
        if (s[i] != s[s.size() - i - 1])
            return false;
    }
    return true;
}

long long a, b;
vector<string> S;

string toStr(long long x){
    stringstream ss;
    ss << x;
    string s;
    ss >> s;
    return s;
}

long long toNum(string s) {
    stringstream ss;
    ss << s;
    long long x = 0;
    ss >> x;
    return x;
}

bool valid(long long x) {
    if (x > 100000000LL) return false;
    long long y = x * x;
    if (y < a || b < y) return false;
    string s = toStr(y);
    return isPalin(s);
}

void solve() {
    long long res = 0;
    cin >> a >> b;
    for (int i = 1; i <= 9999; i++) {
        string s, sr;
        s = S[i]; sr = s;
        reverse(sr.begin(), sr.end());
        s += sr;
        long long x = toNum(s);
        if (valid(x)) {
//            cout << s << endl;
            ++res;
        }

        s.erase(s.size() / 2, 1);
        x = toNum(s);
        if (valid(x)) {
//            cout << s << endl;
            ++res;
        }
    }
    cout << res << endl;
}

int T;

int main() {

    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);

    for (int i = 0; i <= 10000; i++) {
        string s = toStr(i);
        S.push_back(s);
    }
    cin >> T;
    int test = 0;
    while (T > 0) {
        ++test;
        cout << "Case #" << test << ": ";
        solve();
        --T;
    }

}
