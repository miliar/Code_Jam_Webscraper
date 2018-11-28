#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T, k, c, s;
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    cin >> T;
    for (int K = 1; K <= T; K++)
    {
        cin >> k >> c >> s;

        cout << "Case #" << K << ": ";
        if (s < k)
            cout << "IMPOSSIBLE" << endl;
        else
            for (int i = 1; i <= s; i++)
                cout << i << (i == s ? '\n' : ' ');
    }
    return 0;
}
