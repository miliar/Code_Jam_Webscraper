#include <bits/stdc++.h>

#define cin fin
#define cout fout

using namespace std;

ifstream fin("D-small-attempt0.in");
ofstream fout("D-small-attempt0.out");

int T, K, C, S;  /// test cases, original length, complexity, tiles to recover

int main()
{
    cin >> T;

    for (int t=1; t<=T; t++) {
        cout << "Case #" << t << ": ";
        cin >> K >> C >> S;

        if (C == 1) { /// we need K tiles
            if (S < K) cout << "IMPOSSIBLE\n";
            else for (int i=1; i<=K; i++) cout << i << " \n"[i == K];
        } else {
            if (S < K-1) cout << "IMPOSSIBLE\n";
            else {
                if (K == 1) cout << "1\n";
                else for (int i=2; i<=K; i++) cout << i << " \n"[i == K];
            }
        }
    }

    return 0;
}
