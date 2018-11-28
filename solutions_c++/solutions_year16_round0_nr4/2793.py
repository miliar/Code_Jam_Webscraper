#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("D-small-attempt0.in", "r", stdin);
//    freopen("D-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t)
    {
        int k, c, s;
        cin >> k >> c >> s;

        cout << "Case #" << t << ":";
        if(s < k) {
            cout << " IMPOSSIBLE";
        } else {
            for(int i = 1; i <= k; ++i) {
                cout << " " << i;
            }
        }
        cout << endl;
    }

    return 0;
}
