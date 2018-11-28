#include <iostream>
#include <string>
using namespace std;

int B(int);

int A(int n) { // +-+- even
    return n <=1 ? 0 : 1+B(n-1);
}

int B(int n) { // -+-+- odd
    return n <= 1 ? n : 1+A(n-1);
}

int solve(const string &s) {
    int x = 1;
    for (int i=1, N=s.size(); i<N; ++i) {
        if (s[i] != s[i-1]) ++x;
    }

    if (s[0] == '+') return (x & 1) ? A(x-1) : A(x);
    else return (x & 1) ? B(x) : B(x-1);
}

int main() {
    int T; cin >> T;
    for (int i=1; i<=T; ++i) {
        string s; cin >> s;
        int ans = solve(s);
        cout << "Case #" << i << ": " << ans << endl;
    }
    return 0;
}
