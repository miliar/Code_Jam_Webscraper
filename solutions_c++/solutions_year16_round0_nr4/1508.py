#include <bits/stdc++.h>

using namespace std;

int t;

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int i = 1; i <= t; ++i){
        int k, c, s;
        cin >> k >> c >> s;
        if (s >= k){
            cout << "Case #" << i << ": ";
            for (int j = 1; j <= s; ++j) cout << j <<  " ";
            cout << endl;
        } else {
            cout << "Case #" << i << ": IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
