#include <iostream>
#include <cstdio>

using namespace std;

void preprocess() {
}

void solve() {
    int K, C, S;
    cin >> K >> C >> S;
    int kk;
    for (kk=1; kk<K; ++kk) {
        cout << kk << " ";
    }
    cout << K;
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

