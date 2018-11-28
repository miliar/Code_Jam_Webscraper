#include <iostream>
#include <string>
using namespace std;

int solve(const string &s) {
    int need=0, stood=0;
    for (int i=0, N=s.size(); i<N; ++i) {
        if (need + stood < i) {
            ++ need;
        }
        stood += s[i]-'0';
    }
    return need;
}

int main() {
    int T; cin >> T;
    for (int i=1; i<=T; ++i) {
        int max;
        string s;
        cin >> max >> s;
        cout << "Case #" << i << ": " << solve(s) << endl;
    }
    return 0;
}
