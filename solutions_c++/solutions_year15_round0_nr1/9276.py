#include <bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int t;
    cin >> t;
    int k = 1;
    while (t--)
    {
        int n;
        cin >> n;
        string str;
        cin >> str;
        if (n == 0) {
            cout << "Case #" << k << ": " << 0 << endl;
            k++;
            continue;
        }

        int cnt = 0;
        int tot_stand = 0;
        int len = str.length();
        cnt = 0;
        tot_stand = tot_stand + (str[0] - '0');

        for (int i = 1 ; i < len ; i++) {
            if (tot_stand >= i) {
                tot_stand = tot_stand + (str[i] - '0');
            } else if (tot_stand < i) {
                cnt = cnt + i - tot_stand;
                tot_stand = i + (str[i] - '0');
            }
        }
        cout << "Case #" << k << ": " << cnt << endl;
        k++;
    }
    return 0;
}
