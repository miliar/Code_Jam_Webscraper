/// This code is a pure govnocode
#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl;
using namespace std;
const int MAXN = -1;

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);

    int T;
    cin >> T;

    for (int _t = 1; _t <= T; _t++)
    {
        int K, C, S;
        cin >> K >> C >> S;
        cout << "Case #" << _t << ": ";
        for (int i = 1; i <= K; i++)
            cout << i << " ";
        cout << endl;
    }

    return 0;
}
