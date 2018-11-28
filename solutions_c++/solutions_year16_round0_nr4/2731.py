#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
int main(int argc, char **argv)
{
    freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);
    ULL T;
    cin >> T;
    for (ULL t = 1; t <= T; ++t) {
        ULL K, C, S;
        cin >> K >> C >> S;
        cout << "Case #" << t << ": ";
        for (ULL i = 1; i < K; ++i) 
            cout << i << " ";
        cout << K << endl;
    }
    return 0;
}
