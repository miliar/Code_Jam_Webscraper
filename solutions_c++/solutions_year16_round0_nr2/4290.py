#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

void preprocess() {
//    string dummy;
//    cin >> dummy;
}

void solve() {
    string S;
    cin >> S;
    int ssz = S.length();
    int ss;
    int res = 0;
    for (ss=ssz-1; ss>=0; --ss) {
        if (S[ss] != '+') break;
    }
    if (ss < 0) {
        cout << res;
	return;
    }
    char prev = S[ss];
    char curr;
    for (--ss; ss>=0; --ss) {
        curr = S[ss];
	if (prev == curr) continue;
	++res; prev = curr;
    }
    ++res;
    cout << res;
}

int main() {
    int T;
    cin >> T;
    preprocess();
    int tt;
    for (tt=1; tt<=T; ++tt) {
   	cout << "Case #" << tt << ": ";
	solve();
   	cout << endl;
    }
    return 0;
}

