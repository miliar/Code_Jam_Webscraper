#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int tst = 0; tst < T; tst++) {
        int n;
        cin >> n;

        map <string, int> left;
        map <string, int> right;
        vector <pair <int, int> > A(n);
        int res = 0;

        for (int i = 0; i < n; i++) {
            string s1, s2;
            cin >> s1 >> s2;

            if (!left.count(s1)) {
                int num = int(left.size());
                left[s1] = num;
            }
            if (!right.count(s2)) {
                int num = int(right.size());
                right[s2] = num;
            }
            A[i] = make_pair(left[s1], right[s2]);
        }
        int sz1 = int(left.size());
        int sz2 = int(right.size());

        for (int i = 0; i < (1 << n); i++) {
            int mask1 = 0, mask2 = 0;

            for (int j = 0; j < n; j++) {
                if ((i >> j) & 1) {
                    mask1 |= (1 << A[j].first);
                    mask2 |= (1 << A[j].second);
                }
            }

            if (mask1 == (1 << sz1) - 1 && mask2 == (1 << sz2) - 1) {
                res = max(res, n - __builtin_popcount(i));
            }
        }
        cout << "Case #" << tst + 1 << ": " << res << '\n';
    }
    return 0;
}
