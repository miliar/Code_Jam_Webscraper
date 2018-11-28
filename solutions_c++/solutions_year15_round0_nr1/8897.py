#include <bits/stdc++.h>

using namespace std;

int main()
{
        freopen("A-large.in", "r", stdin);
        freopen("ansla.out", "w", stdout);
        int t;
        cin >> t;
        string inp;
        int n;

        for (int j = 1; j <= t; j++) {
                cin >> n >> inp;
                int ans = 0;
                int tot_per = inp[0] - '0';
                for (int i = 1; i < inp.size(); i++) {
                        if (tot_per >= i) {
                                tot_per += inp[i] - '0';
                        } else {
                                ans += i - tot_per;
                                tot_per += i - tot_per;
                                tot_per += inp[i] - '0';
                        }
                }

                cout << "Case #" << j << ": " <<  ans << endl;
        }
        return 0;
}
