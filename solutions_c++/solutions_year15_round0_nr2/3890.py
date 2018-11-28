#include <cstdio>
#include <vector>
#include <cassert>
#include <cmath>
#include <map>
#include <set>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int te;
    cin >> te;

    for (int t = 1; t <= te; t++) {
        int n;
        cerr << "Solving " << t << endl;
        cin >> n;
        vector <int> v(n);
        for (int i = 0; i < n; i++) {
            cin >> v[i];
        }

        int ans = *max_element(v.begin(), v.end());
        for (int i = 1; i < 2000; i++) {
            int cur = i;
            for (int x : v) {
                if (x > i) {
                    cur += (x + i - 1) / i - 1;
                }
            }
            ans = min(ans, cur);
        }

        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}
