#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void solve(int ind) {
    // input
    int Nd;
    cin >> Nd;
    vector<int> pans(Nd);
    for (int i = 0; i < Nd; ++i) {
        cin >> pans[i];
    }
    sort(pans.begin(), pans.end());

    // process
    // 1. you can always complete dining with 0 special minutes, in max(pans[i]) mins
    int minMins = pans[Nd - 1];
    // 2. you can try to complete in N normal minutes, if you can make all plates have <= N pancakes. but add best # of moves to it
    for (int N = 2; N < minMins; ++N) {
        int nMoves  = 0;
        for (int i = Nd - 1; i >= 0; --i) {
            int np = (pans[i] - 1) / N;
            if (np == 0) break;
            nMoves += np;
        }
        minMins = min<int>(minMins, N + nMoves);
    }
    
    // output
    cout << "Case #" << ind << ": " << minMins << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        solve(i);
    }
}