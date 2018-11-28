#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
int main()
{
    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        cout << "Case #" << i + 1 << ": ";

        ll K, C, S;

        cin >> K >> C >> S;

        if (C == 1 && S < K)
        {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        if (C == 1)
        {
            for (int i = 1; i <= S; i++)
                cout << i << " ";
            cout << endl;
            continue;
        }

        if (S < (K + 1)/2)
        {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        ll qual = 2;
        if (K % 2)
            cout << K << " ";
        ll pw = 1;
        for (int i = 0; i < C - 1; i++)
            pw *= K;
        while (qual <= K)
        {
            cout << (qual - 2) * pw + qual << " ";
            qual += 2;
        }
        cout << endl;
    }
}
