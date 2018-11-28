#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int n, x;
    int t;
    cin >> t;
    int tc = 1;

    while (cin >> n >> x) {
        vector<int> v(n);

        for (int i = 0; i < n; i++)
            cin >> v[i];

        sort(v.begin(), v.end());

        int f = 0, l = v.size() - 1;

        int ans = 0;

        while (f <= l) {
            ans++;

            if (f == l) {
                break;
            }

            if (v[l] + v[f] <= x) {
                l--;
                f++;
            } else {
                l--;
            }
        }

        cout << "Case #" << tc++ << ": " << ans << '\n';
    }
    return 0;
}
